#!/usr/bin/env python3
"""
mini_flow_singlefile.py

Single-file minimal distributed workflow engine.
Features:
- SQLite persistence for DAGs, runs, and task_runs
- DSL-ish DAG registration (via a small Python-based DSL file)
- Scheduler that advances DAG runs and enqueues runnable tasks
- Worker loop that claims and runs tasks (shell & http)
- CLI to init DB, register DAG, trigger runs, run scheduler+worker daemons, list objects, tail logs
- Uses asyncio concurrency, subprocess for shell tasks, urllib for HTTP tasks (standard library)
- All in one file for easy experimentation

Example usage:
    python mini_flow_singlefile.py init-db
    python mini_flow_singlefile.py register-dag example_dag.py
    python mini_flow_singlefile.py trigger 1
    python mini_flow_singlefile.py daemon  # runs scheduler + worker
    python mini_flow_singlefile.py list-dags
    python mini_flow_singlefile.py list-runs
    python mini_flow_singlefile.py tail-logs 1
"""

import argparse
import asyncio
import sqlite3
import json
import os
import sys
import time
import traceback
from datetime import datetime
from typing import Dict, List, Any, Optional
import urllib.request
import threading
import subprocess
import shlex

# ----------------------------
# Configuration
# ----------------------------
DB_FILE = os.environ.get("MINIFLOW_DB", "mini_flow.db")
SCHEDULER_INTERVAL = float(os.environ.get("MINIFLOW_SCHED_INTERVAL", "1.0"))
WORKER_POLL_INTERVAL = float(os.environ.get("MINIFLOW_WORKER_POLL", "1.0"))
WORKER_CONCURRENCY = int(os.environ.get("MINIFLOW_WORKER_CONCURRENCY", "4"))
CLAIM_TIMEOUT = 30  # seconds - not implemented advancedly but for future
DEFAULT_RETRY = 2
DEFAULT_RETRY_BACKOFF = 2.0  # multiplier for exponential backoff

# ----------------------------
# Schema and DB helpers
# ----------------------------
_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS dags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    definition TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dag_id INTEGER NOT NULL,
    task_id TEXT NOT NULL,
    type TEXT NOT NULL,
    params TEXT NOT NULL,
    upstreams TEXT,
    FOREIGN KEY(dag_id) REFERENCES dags(id)
);

CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dag_id INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'PENDING',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    started_at DATETIME,
    finished_at DATETIME,
    FOREIGN KEY(dag_id) REFERENCES dags(id)
);

CREATE TABLE IF NOT EXISTS task_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id INTEGER NOT NULL,
    task_id TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'PENDING',
    attempts INTEGER NOT NULL DEFAULT 0,
    last_error TEXT,
    logs TEXT,
    queued_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    started_at DATETIME,
    finished_at DATETIME,
    next_try_at DATETIME,
    FOREIGN KEY(run_id) REFERENCES runs(id)
);
"""

def get_conn():
    conn = sqlite3.connect(DB_FILE, timeout=30, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    with conn:
        conn.executescript(_SCHEMA_SQL)
    conn.close()
    print(f"Initialized DB at {DB_FILE}")

# ----------------------------
# Simple DAG DSL loader
# ----------------------------
"""
The DSL is a Python file that uses the provided helper classes to declare a DAG.
Example DSL file (example_dag.py):

from mini_flow_dsl import DAG

dag = DAG("example")
dag.task("t1", "shell", {"cmd": "echo hello"})
dag.task("t2", "http", {"url": "https://httpbin.org/get"}, upstreams=["t1"])

# Optionally export a function register(dag_repo) to programmatically register;
# otherwise, this file should define a top-level 'dag' variable.

"""

class DSL_DAG:
    def __init__(self, name: str):
        self.name = name
        self.tasks = {}  # task_id -> dict(type, params, upstreams)

    def task(self, task_id: str, type_: str, params: Dict[str, Any] = None, upstreams: List[str] = None):
        if task_id in self.tasks:
            raise ValueError(f"Duplicate task_id {task_id}")
        self.tasks[task_id] = {
            "task_id": task_id,
            "type": type_,
            "params": params or {},
            "upstreams": upstreams or []
        }

def load_dag_from_py(path: str) -> DSL_DAG:
    """
    Load a single DSL-defined DAG from a Python file.
    The file should either expose 'dag' variable (DSL_DAG) or define register(dag_repo) function.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    # We'll execute the file in an isolated namespace with DSL available
    ns = {"DAG": DSL_DAG, "dsl_DAG": DSL_DAG}
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()
    # execute
    exec(compile(code, path, 'exec'), ns)
    if "dag" in ns and isinstance(ns["dag"], DSL_DAG):
        return ns["dag"]
    # If file defines a function 'build' that returns dag
    if "build" in ns and callable(ns["build"]):
        d = ns["build"]()
        if isinstance(d, DSL_DAG):
            return d
    # else try to find any DSL_DAG instances
    for v in ns.values():
        if isinstance(v, DSL_DAG):
            return v
    raise ValueError("No DSL DAG found in file. Define a 'dag' variable (DSL_DAG) or function 'build' that returns one.")

# ----------------------------
# Storage operations
# ----------------------------
def register_dag(dsl: DSL_DAG) -> int:
    conn = get_conn()
    with conn:
        cur = conn.execute("INSERT INTO dags (name, definition) VALUES (?, ?)", (dsl.name, json.dumps({"tasks": dsl.tasks})))
        dag_id = cur.lastrowid
        for t in dsl.tasks.values():
            conn.execute("INSERT INTO tasks (dag_id, task_id, type, params, upstreams) VALUES (?, ?, ?, ?, ?)",
                         (dag_id, t["task_id"], t["type"], json.dumps(t["params"]), json.dumps(t["upstreams"])))
    conn.close()
    print(f"Registered DAG '{dsl.name}' as id {dag_id}")
    return dag_id

def list_dags() -> List[Dict[str, Any]]:
    conn = get_conn()
    cur = conn.execute("SELECT id, name, created_at FROM dags ORDER BY id")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

def get_dag(dag_id: int) -> Optional[Dict[str, Any]]:
    conn = get_conn()
    r = conn.execute("SELECT id, name, definition, created_at FROM dags WHERE id = ?", (dag_id,)).fetchone()
    conn.close()
    return dict(r) if r else None

def get_tasks_for_dag(dag_id: int) -> List[Dict[str, Any]]:
    conn = get_conn()
    cur = conn.execute("SELECT id, task_id, type, params, upstreams FROM tasks WHERE dag_id = ? ORDER BY id", (dag_id,))
    rows = []
    for r in cur.fetchall():
        d = dict(r)
        d["params"] = json.loads(d["params"])
        d["upstreams"] = json.loads(d["upstreams"]) if d["upstreams"] else []
        rows.append(d)
    conn.close()
    return rows

def create_run(dag_id: int) -> int:
    conn = get_conn()
    with conn:
        cur = conn.execute("INSERT INTO runs (dag_id, status) VALUES (?, 'PENDING')", (dag_id,))
        run_id = cur.lastrowid
        # create task_runs
        tasks = get_tasks_for_dag(dag_id)
        for t in tasks:
            conn.execute("INSERT INTO task_runs (run_id, task_id, status, attempts, logs) VALUES (?, ?, 'PENDING', 0, '')", (run_id, t["task_id"]))
    conn.close()
    print(f"Created run {run_id} for dag {dag_id}")
    return run_id

def list_runs() -> List[Dict[str, Any]]:
    conn = get_conn()
    cur = conn.execute("SELECT id, dag_id, status, created_at, started_at, finished_at FROM runs ORDER BY id")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

def get_task_runs(run_id: int) -> List[Dict[str, Any]]:
    conn = get_conn()
    cur = conn.execute("SELECT id, run_id, task_id, status, attempts, last_error, logs, queued_at, started_at, finished_at, next_try_at FROM task_runs WHERE run_id = ? ORDER BY id", (run_id,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

# atomic claim: update where status = 'PENDING' and (next_try_at is null or <= now)
def claim_task(run_id: int) -> Optional[Dict[str, Any]]:
    """
    Claim one PENDING task in a run that has its upstreams satisfied and next_try_at <= now.
    We choose the oldest queued_at (FIFO).
    Returns the task_run row dict if claimed, otherwise None.
    """
    now = datetime.utcnow().isoformat(sep=' ')
    conn = get_conn()
    with conn:
        # Find a candidate pending task whose next_try_at is null or <= now
        cur = conn.execute("""
        SELECT tr.id, tr.run_id, tr.task_id, tr.status, tr.attempts, tr.logs, tr.next_try_at
        FROM task_runs tr
        WHERE tr.run_id = ? AND tr.status = 'PENDING' AND (tr.next_try_at IS NULL OR tr.next_try_at <= ?)
        ORDER BY tr.queued_at ASC
        LIMIT 1
        """, (run_id, now))
        row = cur.fetchone()
        if not row:
            return None
        tr_id = row["id"]
        # Try to claim by updating status -> RUNNING if still PENDING
        res = conn.execute("UPDATE task_runs SET status = 'RUNNING', started_at = CURRENT_TIMESTAMP, attempts = attempts + 1 WHERE id = ? AND status = 'PENDING'", (tr_id,))
        if res.rowcount == 0:
            # race - not claimed
            return None
        # fetch claimed row
        r2 = conn.execute("SELECT id, run_id, task_id, status, attempts, logs, next_try_at FROM task_runs WHERE id = ?", (tr_id,)).fetchone()
        conn.commit()
        d = dict(r2)
    conn.close()
    return d

def update_task_run_status(run_id: int, task_id: str, status: str, error: Optional[str] = None):
    conn = get_conn()
    with conn:
        if status in ("SUCCESS", "FAILED"):
            conn.execute("UPDATE task_runs SET status = ?, last_error = ?, finished_at = CURRENT_TIMESTAMP WHERE run_id = ? AND task_id = ?", (status, error, run_id, task_id))
        else:
            conn.execute("UPDATE task_runs SET status = ?, last_error = ? WHERE run_id = ? AND task_id = ?", (status, error, run_id, task_id))
    conn.close()

def append_task_logs(run_id: int, task_id: str, extra: str):
    conn = get_conn()
    with conn:
        cur = conn.execute("SELECT logs FROM task_runs WHERE run_id = ? AND task_id = ?", (run_id, task_id)).fetchone()
        if not cur:
            return
        current = cur["logs"] or ""
        new = current + extra
        conn.execute("UPDATE task_runs SET logs = ? WHERE run_id = ? AND task_id = ?", (new, run_id, task_id))
    conn.close()

def set_task_next_try(run_id: int, task_id: str, when_iso: Optional[str]):
    conn = get_conn()
    with conn:
        conn.execute("UPDATE task_runs SET next_try_at = ? WHERE run_id = ? AND task_id = ?", (when_iso, run_id, task_id))
    conn.close()

def mark_run_started_if_needed(run_id: int):
    conn = get_conn()
    with conn:
        cur = conn.execute("SELECT started_at, status FROM runs WHERE id = ?", (run_id,)).fetchone()
        if cur and cur["started_at"] is None:
            conn.execute("UPDATE runs SET started_at = CURRENT_TIMESTAMP, status = 'RUNNING' WHERE id = ?", (run_id,))
    conn.close()

def maybe_finish_run(run_id: int):
    conn = get_conn()
    with conn:
        total = conn.execute("SELECT COUNT(*) as c FROM task_runs WHERE run_id = ?", (run_id,)).fetchone()["c"]
        done = conn.execute("SELECT COUNT(*) as c FROM task_runs WHERE run_id = ? AND status IN ('SUCCESS','FAILED')", (run_id,)).fetchone()["c"]
        if total == done and total > 0:
            failed = conn.execute("SELECT COUNT(*) as c FROM task_runs WHERE run_id = ? AND status = 'FAILED'", (run_id,)).fetchone()["c"]
            status = "FAILED" if failed > 0 else "SUCCESS"
            conn.execute("UPDATE runs SET status = ?, finished_at = CURRENT_TIMESTAMP WHERE id = ?", (status, run_id))
    conn.close()

# ----------------------------
# DAG utilities (validation & topological helpers)
# ----------------------------
def load_dag_definition_from_db(dag_id: int) -> Dict[str, Any]:
    dag = get_dag(dag_id)
    if not dag:
        raise ValueError("DAG not found")
    definition = json.loads(dag["definition"])
    return definition

def get_upstream_task_ids(dag_id: int, task_id: str) -> List[str]:
    tasks = get_tasks_for_dag(dag_id)
    for t in tasks:
        if t["task_id"] == task_id:
            return t["upstreams"]
    return []

def tasks_satisfied_for_run(run_id: int, dag_id: int, task_id: str) -> bool:
    """
    Verify that all upstream tasks for this task (in the DAG) have status SUCCESS in this run.
    """
    ups = get_upstream_task_ids(dag_id, task_id)
    if not ups:
        return True
    conn = get_conn()
    cur = conn.execute("SELECT task_id, status FROM task_runs WHERE run_id = ? AND task_id IN ({seq})".format(seq=",".join("?"*len(ups))), (run_id, *ups))
    rows = cur.fetchall()
    conn.close()
    # If any upstream missing or not SUCCESS, return False
    if len(rows) != len(ups):
        return False
    for r in rows:
        if r["status"] != "SUCCESS":
            return False
    return True

# ----------------------------
# Task type handlers
# ----------------------------
# Handlers are async funcs: async def handler(run_id, task_id, params, append_log) -> None (raise on failure)
async def shell_task_handler(run_id: int, task_id: str, params: Dict[str, Any], append_log):
    """
    params:
      - cmd: shell command string
      - timeout: seconds (optional)
    """
    cmd = params.get("cmd")
    if not cmd:
        raise ValueError("shell task requires 'cmd' param")
    timeout = params.get("timeout", None)
    append_log(f"[shell] running: {cmd}\n")
    # Use asyncio subprocess for non-blocking
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    try:
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout) if timeout else await proc.communicate()
    except asyncio.TimeoutError:
        proc.kill()
        await proc.wait()
        append_log(f"[shell] timeout after {timeout}s\n")
        raise RuntimeError("timeout")
    if stdout:
        try:
            append_log(stdout.decode())
        except Exception:
            append_log(str(stdout))
    if stderr:
        try:
            append_log(stderr.decode())
        except Exception:
            append_log(str(stderr))
    if proc.returncode != 0:
        raise RuntimeError(f"Command exited with code {proc.returncode}")

async def http_task_handler(run_id: int, task_id: str, params: Dict[str, Any], append_log):
    """
    params:
      - url: string
      - method: GET/POST
      - timeout: seconds (optional)
    Implementation uses urllib in a thread to avoid external deps.
    """
    url = params.get("url")
    method = (params.get("method") or "GET").upper()
    timeout = params.get("timeout", 10)
    if not url:
        raise ValueError("http task requires 'url' param")
    append_log(f"[http] {method} {url}\n")
    def do_request():
        req = urllib.request.Request(url, method=method)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read(1024*50)  # read up to 50 KB for preview
            code = resp.getcode()
            return code, data
    loop = asyncio.get_event_loop()
    try:
        code, data = await loop.run_in_executor(None, do_request)
    except Exception as e:
        append_log(f"[http] error: {e}\n")
        raise
    append_log(f"[http] status: {code}\n")
    try:
        preview = data.decode(errors="replace")
    except Exception:
        preview = str(data)
    if len(preview) > 1000:
        preview = preview[:1000] + "...(truncated)\n"
    append_log(preview + "\n")
    if code >= 400:
        raise RuntimeError(f"HTTP {code}")

# registry
TASK_HANDLERS = {
    "shell": shell_task_handler,
    "http": http_task_handler
}

# ----------------------------
# Executor: run a claimed task_run
# ----------------------------
async def run_task_run(task_run_row: Dict[str, Any], dag_id: int):
    """
    task_run_row: dict with keys id, run_id, task_id, status, attempts, logs, next_try_at
    dag_id: id of the dag to load task params and type
    """
    run_id = task_run_row["run_id"]
    task_id = task_run_row["task_id"]
    # get task def
    tasks = get_tasks_for_dag(dag_id)
    tdef = None
    for t in tasks:
        if t["task_id"] == task_id:
            tdef = t
            break
    if tdef is None:
        append_task_logs(run_id, task_id, f"[engine] TASK DEFINITION MISSING for {task_id}\n")
        update_task_run_status(run_id, task_id, "FAILED", error="task definition missing")
        maybe_finish_run(run_id)
        return
    handler = TASK_HANDLERS.get(tdef["type"])
    if handler is None:
        append_task_logs(run_id, task_id, f"[engine] No handler for type {tdef['type']}\n")
        update_task_run_status(run_id, task_id, "FAILED", error=f"no handler for {tdef['type']}")
        maybe_finish_run(run_id)
        return
    # mark run started if not already
    mark_run_started_if_needed(run_id)
    # run and capture logs via append_task_logs
    def appender(s: str):
        append_task_logs(run_id, task_id, s)
    attempts = task_run_row.get("attempts", 1)
    append_task_logs(run_id, task_id, f"[engine] START attempt {attempts}\n")
    try:
        await handler(run_id, task_id, tdef["params"], appender)
        append_task_logs(run_id, task_id, "[engine] SUCCESS\n")
        update_task_run_status(run_id, task_id, "SUCCESS", error=None)
    except Exception as e:
        tb = traceback.format_exc()
        append_task_logs(run_id, task_id, f"[engine] EXCEPTION: {e}\n{tb}\n")
        # implement retry/backoff
        # Compute backoff based on attempts: base_backoff * (backoff_multiplier ** (attempts-1))
        base = tdef["params"].get("retry_backoff_base", DEFAULT_RETRY_BACKOFF)
        max_retries = tdef["params"].get("max_retries", DEFAULT_RETRY)
        if attempts <= max_retries:
            backoff = base * (DEFAULT_RETRY_BACKOFF ** (attempts-1))
            next_try = datetime.utcnow().timestamp() + backoff
            next_try_iso = datetime.utcfromtimestamp(next_try).isoformat(sep=' ')
            set_task_next_try(run_id, task_id, next_try_iso)
            update_task_run_status(run_id, task_id, "PENDING", error=str(e))
            append_task_logs(run_id, task_id, f"[engine] Scheduled retry #{attempts} after {backoff:.1f}s (next_try_at {next_try_iso})\n")
        else:
            update_task_run_status(run_id, task_id, "FAILED", error=str(e))
            append_task_logs(run_id, task_id, f"[engine] Failed after {attempts} attempts\n")
    finally:
        maybe_finish_run(run_id)

# ----------------------------
# Scheduler
# ----------------------------
async def scheduler_loop(shutdown_event: asyncio.Event):
    """
    Scheduler responsibilities:
      - For each RUN in status PENDING or RUNNING, find PENDING task_runs whose upstreams are satisfied and whose next_try_at <= now; mark them available (they are stored as PENDING already)
      - For distributed model: we leave tasks in DB as PENDING. Workers claim them for execution.
      - Here we proactively evaluate runs and set run.started_at when first task executes (performed in executor too).
      - We'll also set run to SUCCESS/FAILED when done (maybe_finish_run).
    """
    print("[scheduler] starting")
    while not shutdown_event.is_set():
        try:
            conn = get_conn()
            with conn:
                runs_cur = conn.execute("SELECT id, dag_id, status FROM runs WHERE status IN ('PENDING','RUNNING')").fetchall()
            for r in runs_cur:
                run_id = r["id"]
                dag_id = r["dag_id"]
                # for every PENDING task in this run, check if upstreams satisfied; if so ensure next_try_at <= now (we don't change anything; worker will claim)
                pending = get_task_runs(run_id)
                # iterate tasks and if PENDING and upstreams satisfied and next_try_at is null or <= now -> do nothing (worker will claim)
                for tr in pending:
                    if tr["status"] != "PENDING":
                        continue
                    task_id = tr["task_id"]
                    # ensure upstreams satisfied
                    ok = tasks_satisfied_for_run(run_id, dag_id, task_id)
                    if ok:
                        # nothing to change here. We could reorder queued_at or so, but leave as-is.
                        pass
                maybe_finish_run(run_id)
            conn.close()
        except Exception as e:
            print("[scheduler] exception:", e)
            traceback.print_exc()
        await asyncio.sleep(SCHEDULER_INTERVAL)
    print("[scheduler] stopping")

# ----------------------------
# Worker
# ----------------------------
async def worker_loop(shutdown_event: asyncio.Event, concurrency: int = WORKER_CONCURRENCY):
    """
    Worker repeatedly looks for runs that have runnable tasks (PENDING and upstreams satisfied).
    Claim tasks atomically and run them asynchronously with limited concurrency.
    """
    print("[worker] starting with concurrency", concurrency)
    sem = asyncio.Semaphore(concurrency)
    # We'll maintain a set of running tasks
    running = set()

    async def run_claimed(tr_row: Dict[str, Any], dag_id: int):
        async with sem:
            tkey = (tr_row["run_id"], tr_row["task_id"], tr_row["id"])
            running.add(tkey)
            try:
                await run_task_run(tr_row, dag_id)
            finally:
                running.discard(tkey)

    while not shutdown_event.is_set():
        try:
            # find runs that have PENDING tasks with upstreams satisfied
            conn = get_conn()
            with conn:
                run_candidates = conn.execute("SELECT id, dag_id FROM runs WHERE status IN ('PENDING','RUNNING')").fetchall()
            conn.close()
            claimed_any = False
            for r in run_candidates:
                run_id = r["id"]
                dag_id = r["dag_id"]
                # check for PENDING tasks that have upstream satisfied
                conn = get_conn()
                with conn:
                    # naive: fetch pending task_runs
                    cur = conn.execute("SELECT id, run_id, task_id, status, attempts, logs, next_try_at FROM task_runs WHERE run_id = ? AND status = 'PENDING' ORDER BY queued_at ASC", (run_id,))
                    pending_rows = [dict(rr) for rr in cur.fetchall()]
                conn.close()
                for tr in pending_rows:
                    tid = tr["task_id"]
                    # ensure next_try_at <= now if set
                    if tr["next_try_at"]:
                        try:
                            nxt = datetime.fromisoformat(tr["next_try_at"])
                            if datetime.utcnow() < nxt:
                                continue
                        except Exception:
                            pass
                    if not tasks_satisfied_for_run(run_id, dag_id, tid):
                        continue
                    # Try to claim
                    claimed = claim_task(run_id)
                    if not claimed:
                        # maybe another worker raced
                        continue
                    # claimed is a dict of claimed row
                    claimed_any = True
                    # Launch execution
                    asyncio.create_task(run_claimed(claimed, dag_id))
                # end for tr
            # end for runs
            if not claimed_any:
                # nothing to do -> sleep
                await asyncio.sleep(WORKER_POLL_INTERVAL)
        except Exception as e:
            print("[worker] exception:", e)
            traceback.print_exc()
            await asyncio.sleep(1.0)
    # Wait for outstanding tasks
    print("[worker] shutting down - waiting for running tasks to finish")
    while running:
        await asyncio.sleep(0.2)
    print("[worker] stopped")

# ----------------------------
# CLI & helpers
# ----------------------------
def cmd_init_db(args):
    init_db()

def cmd_register_dag(args):
    dsl = load_dag_from_py(args.path)
    register_dag(dsl)

def cmd_list_dags(args):
    rows = list_dags()
    if not rows:
        print("No dags")
        return
    for r in rows:
        print(f"ID {r['id']}  name='{r['name']}'  created_at={r['created_at']}")

def cmd_show_dag(args):
    dag = get_dag(args.dag_id)
    if not dag:
        print("DAG not found")
        return
    print("DAG:", dag["id"], dag["name"])
    tasks = get_tasks_for_dag(args.dag_id)
    for t in tasks:
        print(f"  - {t['task_id']} (type={t['type']}) upstreams={t['upstreams']} params={t['params']}")

def cmd_trigger(args):
    if not get_dag(args.dag_id):
        print("DAG not found")
        return
    run_id = create_run(args.dag_id)
    print("Triggered run", run_id)

def cmd_list_runs(args):
    rows = list_runs()
    if not rows:
        print("No runs")
        return
    for r in rows:
        print(f"ID {r['id']} dag={r['dag_id']} status={r['status']} created_at={r['created_at']} started_at={r['started_at']} finished_at={r['finished_at']}")

def cmd_show_run(args):
    runs = list_runs()
    found = None
    for r in runs:
        if r["id"] == args.run_id:
            found = r
            break
    if not found:
        print("Run not found")
        return
    print("Run:", found)
    trs = get_task_runs(args.run_id)
    for t in trs:
        print(f"  task {t['task_id']} status={t['status']} attempts={t['attempts']} started_at={t['started_at']} finished_at={t['finished_at']}")
        if t["last_error"]:
            print("    error:", t["last_error"])

def cmd_tail_logs(args):
    # simple polling to print logs for a run
    while True:
        trs = get_task_runs(args.run_id)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Logs for run {args.run_id} (press Ctrl-C to stop)\n")
        for t in trs:
            print(f"--- {t['task_id']}  status={t['status']} attempts={t['attempts']} ---")
            print(t["logs"] or "(no logs)")
            print()
        time.sleep(1.0)

def cmd_daemon(args):
    # run scheduler + worker loops in same process
    loop = asyncio.get_event_loop()
    shutdown = asyncio.Event()
    async def main():
        s = asyncio.create_task(scheduler_loop(shutdown))
        w = asyncio.create_task(worker_loop(shutdown, concurrency=args.concurrency))
        print("Daemon started. Ctrl-C to stop.")
        try:
            await asyncio.wait([s, w], return_when=asyncio.FIRST_COMPLETED)
        finally:
            shutdown.set()
            await asyncio.gather(s, w, return_exceptions=True)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Shutting down daemon...")
    finally:
        loop.stop()
        loop.close()

# ----------------------------
# For testing: small example DAG generator
# ----------------------------
SAMPLE_DAG_PY = r'''
# Example DSL file for mini_flow_singlefile.py
# Save as example_dag.py and then run:
#   python mini_flow_singlefile.py register-dag example_dag.py

dag = DAG("example_pipeline")

dag.task("start", "shell", {"cmd": "echo Starting; sleep 1"})
dag.task("fetch", "http", {"url": "https://httpbin.org/get"}, upstreams=["start"])
dag.task("process", "shell", {"cmd": "echo Processing; sleep 1; echo Done processing"}, upstreams=["fetch"])
dag.task("final", "shell", {"cmd": "echo Final step; sleep 1"}, upstreams=["process"])
'''

def cmd_write_sample(args):
    path = args.path
    with open(path, "w", encoding="utf-8") as f:
        f.write(SAMPLE_DAG_PY)
    print("Wrote sample DAG to", path)

# ----------------------------
# Tests (lightweight)
# ----------------------------
def run_internal_test():
    print("Running quick internal test...")
    # init in-memory DB? use file DB for now but remove after
    tmp_db = "test_mini_flow.db"
    global DB_FILE
    old_db = DB_FILE
    DB_FILE = tmp_db
    if os.path.exists(tmp_db):
        os.remove(tmp_db)
    init_db()
    # write sample dag
    sample_path = "tmp_example_dag.py"
    with open(sample_path, "w", encoding="utf-8") as f:
        f.write(SAMPLE_DAG_PY)
    dsl = load_dag_from_py(sample_path)
    dag_id = register_dag(dsl)
    run_id = create_run(dag_id)
    print("Starting daemon for 8 seconds to execute run...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    shutdown = asyncio.Event()
    async def run_short():
        s = asyncio.create_task(scheduler_loop(shutdown))
        w = asyncio.create_task(worker_loop(shutdown, concurrency=2))
        # let it run 8 seconds
        await asyncio.sleep(8)
        shutdown.set()
        await asyncio.gather(s, w, return_exceptions=True)
    try:
        loop.run_until_complete(run_short())
    finally:
        loop.close()
    print("Run finished. Task runs:")
    trs = get_task_runs(run_id)
    for t in trs:
        print(t["task_id"], t["status"], "attempts=", t["attempts"])
        print("logs:")
        print(t["logs"] or "(no logs)")
    # cleanup
    os.remove(sample_path)
    if os.path.exists(tmp_db):
        os.remove(tmp_db)
    DB_FILE = old_db
    print("Internal test done.")

# ----------------------------
# Argument parser
# ----------------------------
def build_parser():
    p = argparse.ArgumentParser("mini_flow_singlefile")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("init-db", help="Initialize sqlite DB")
    sp.set_defaults(func=cmd_init_db)

    sp = sub.add_parser("register-dag", help="Register DAG from DSL Python file")
    sp.add_argument("path", help="path to DSL python file")
    sp.set_defaults(func=cmd_register_dag)

    sp = sub.add_parser("list-dags", help="List DAGs")
    sp.set_defaults(func=cmd_list_dags)

    sp = sub.add_parser("show-dag", help="Show DAG tasks")
    sp.add_argument("dag_id", type=int)
    sp.set_defaults(func=cmd_show_dag)

    sp = sub.add_parser("trigger", help="Trigger a run for DAG")
    sp.add_argument("dag_id", type=int)
    sp.set_defaults(func=cmd_trigger)

    sp = sub.add_parser("list-runs", help="List runs")
    sp.set_defaults(func=cmd_list_runs)

    sp = sub.add_parser("show-run", help="Show run and task_runs")
    sp.add_argument("run_id", type=int)
    sp.set_defaults(func=cmd_show_run)

    sp = sub.add_parser("tail-logs", help="Tail logs for a run (polling)")
    sp.add_argument("run_id", type=int)
    sp.set_defaults(func=cmd_tail_logs)

    sp = sub.add_parser("daemon", help="Run scheduler + worker loops (daemon)")
    sp.add_argument("--concurrency", type=int, default=WORKER_CONCURRENCY)
    sp.set_defaults(func=cmd_daemon)

    sp = sub.add_parser("write-sample", help="Write a sample DSL file for quick experiments")
    sp.add_argument("path", nargs="?", default="example_dag.py")
    sp.set_defaults(func=cmd_write_sample)

    sp = sub.add_parser("test", help="Run internal quick test")
    sp.set_defaults(func=lambda args: run_internal_test())

    return p

# ----------------------------
# Entry point
# ----------------------------
def main():
    parser = build_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()

if __name__ == "__main__":
    main()
