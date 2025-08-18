let points = 0;

function addPoint() {
  points++;
  updatePointsDisplay();
}
function add100(){
  points + 100
  updatePointsDisplay();
}

function buySword() {
  if (points >= 10) {
    points -= 10;
    updatePointsDisplay();
    document.getElementById("message").innerText = " Sword bought! Mobs will spawn!";
    spawnMob(); 
  } else {
    document.getElementById("message").innerText = " Not enough points!";
  }
}

function updatePointsDisplay() {
  document.getElementById("pointsDisplay").innerText = points;
}

function spawnMob() {
  
  const bug = document.createElement("div");
  bug.innerText = " Mob Spawned!";
  bug.style.fontSize = "24px";
  bug.style.marginTop = "20px";
  document.body.appendChild(bug);
}
