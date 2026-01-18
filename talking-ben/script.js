const text = document.getElementById("text");
const ben = document.getElementById("ben");

const yesSound = document.getElementById("yesSound");
const noSound = document.getElementById("noSound");
const hohoSound = document.getElementById("hohoSound");
const pickupSound = document.getElementById("pickupSound");

function callBen() {
    pickupSound.play();
    text.textContent = "Ben picked up the phone...";
    ben.style.transform = "rotate(10deg)";
}

function answer(type) {
    text.textContent = "Thinking...";
    ben.style.transform = "scale(1.1)";

    setTimeout(() => {
        ben.style.transform = "scale(1)";

        if (type === "yes") {
            yesSound.play();
            text.textContent = "Yes";
        }

        if (type === "no") {
            noSound.play();
            text.textContent = "No";
        }

        if (type === "hoho") {
            hohoSound.play();
            text.textContent = "Ho ho ho!";
        }
    }, 800);
}
