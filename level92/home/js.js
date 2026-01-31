const p1 = new Promise(resolve => setTimeout(() => resolve('First'), 1000));
const p2 = new Promise(resolve => setTimeout(() => resolve('Second'), 2000));
const p3 = new Promise(resolve => setTimeout(() => resolve('Third'), 1500));

Promise.all([p1, p2, p3]).then(results => {
    console.log(results);
});


async function first() {
    await new Promise(r => setTimeout(r, 1000));
    return 'First';
}

async function second() {
    await new Promise(r => setTimeout(r, 2000));
    return 'Second';
}

async function third() {
    await new Promise(r => setTimeout(r, 1500));
    return 'Third';
}

async function runSequential() {
    const result1 = await first();
    console.log(result1);
    const result2 = await second();
    console.log(result2);
    const result3 = await third();
    console.log(result3);
}

runSequential();
