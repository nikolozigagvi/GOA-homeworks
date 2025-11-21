/* ==========================================================
   SITE.JS — Full Interactive Script for RPG Game Website
   Features:
   ✔ Smooth scroll
   ✔ Animated counters
   ✔ Mobile nav toggle
   ✔ FAQ accordion
   ✔ Dynamic screenshots carousel
   ✔ Back-to-top button
   ✔ Dark/Light theme switch
   ✔ Animated typing text
   ========================================================== */

// -----------------------------
// NAV MENU (Mobile Toggle)
// -----------------------------
const menuBtn = document.querySelector(".menu-btn");
const navList = document.querySelector(".nav-list");

menuBtn.addEventListener("click", () => {
    navList.classList.toggle("open");
    menuBtn.classList.toggle("open");
});

// Close menu when clicking link
document.querySelectorAll(".nav-list a").forEach(link => {
    link.addEventListener("click", () => {
        navList.classList.remove("open");
        menuBtn.classList.remove("open");
    });
});

// -----------------------------
// SMOOTH SCROLL
// -----------------------------
document.querySelectorAll("a[href^='#']").forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href"))
            .scrollIntoView({ behavior: "smooth" });
    });
});

// -----------------------------
// BACK TO TOP BUTTON
// -----------------------------
const backTop = document.createElement("button");
backTop.innerText = "⬆";
backTop.id = "backTop";
document.body.appendChild(backTop);

window.addEventListener("scroll", () => {
    backTop.style.display = window.scrollY > 400 ? "block" : "none";
});

backTop.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

// -----------------------------
// ANIMATED TYPING EFFECT
// -----------------------------
const typingText = document.querySelector(".typing");
const words = [
    "A Massive Python RPG Project",
    "500+ Lines of Code",
    "Terminal-Based Combat",
    "Quests, Enemies, Loot, Skills",
    "Your Own RPG Adventure"
];
let wIndex = 0;
let cIndex = 0;
let deleting = false;

function type() {
    let currentWord = words[wIndex];

    if (!deleting) {
        typingText.textContent = currentWord.substring(0, cIndex++);
        if (cIndex === currentWord.length + 1) deleting = true;
    } else {
        typingText.textContent = currentWord.substring(0, cIndex--);
        if (cIndex < 0) {
            deleting = false;
            wIndex = (wIndex + 1) % words.length;
        }
    }
    setTimeout(type, deleting ? 50 : 100);
}
type();

// -----------------------------
// CARDS HOVER EFFECT (Glow)
// -----------------------------
document.querySelectorAll(".card").forEach(card => {
    card.addEventListener("mousemove", e => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        card.style.setProperty("--x", `${x}px`);
        card.style.setProperty("--y", `${y}px`);
    });
});

// -----------------------------
// STATS COUNTER ANIMATION
// -----------------------------
const counters = document.querySelectorAll(".count");
let countersStarted = false;

function startCounters() {
    if (countersStarted) return;

    const section = document.querySelector("#stats");
    const sectionPos = section.getBoundingClientRect().top;

    if (sectionPos < window.innerHeight - 100) {
        counters.forEach(counter => {
            const target = +counter.dataset.target;
            let current = 0;
            const step = target / 100;

            function update() {
                current += step;
                if (current < target) {
                    counter.innerText = Math.floor(current);
                    requestAnimationFrame(update);
                } else {
                    counter.innerText = target;
                }
            }
            update();
        });
        countersStarted = true;
    }
}

window.addEventListener("scroll", startCounters);

// -----------------------------
// FAQ ACCORDION
// -----------------------------
document.querySelectorAll(".faq-item").forEach(faq => {
    faq.addEventListener("click", () => {
        faq.classList.toggle("open");
        const answer = faq.querySelector(".answer");
        answer.style.maxHeight = faq.classList.contains("open")
            ? answer.scrollHeight + "px"
            : "0px";
    });
});

// -----------------------------
// SCREENSHOT CAROUSEL
// -----------------------------
const slides = [
    "img/game1.png",
    "img/game2.png",
    "img/game3.png",
    "img/game4.png"
];

let slideIndex = 0;
const screenshotImg = document.querySelector(".screenshot");

function changeSlide() {
    slideIndex = (slideIndex + 1) % slides.length;
    screenshotImg.src = slides[slideIndex];
}
setInterval(changeSlide, 3000);

// -----------------------------
// DARK / LIGHT MODE
// -----------------------------
const themeBtn = document.querySelector(".theme-btn");
themeBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    themeBtn.textContent =
        document.body.classList.contains("dark") ? "☀ Light Mode" : "🌙 Dark Mode";
});

// -----------------------------
// RANDOM FUN FACT GENERATOR
// -----------------------------
const facts = [
    "The game contains over 500 lines of Python!",
    "All combat is turn-based with custom AI.",
    "You can upgrade 4 different skill stats.",
    "Boss fights have special attack phases.",
    "Loot system uses rarity probability tables."
];

document.querySelector(".fact-btn").addEventListener("click", () => {
    const randomFact = facts[Math.floor(Math.random() * facts.length)];
    document.querySelector(".fact-text").textContent = randomFact;
});

// -----------------------------
// COPY CODE BUTTON (for code samples)
// -----------------------------
document.querySelectorAll(".copy-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        const codeBox = btn.previousElementSibling;
        navigator.clipboard.writeText(codeBox.innerText);
        btn.innerText = "Copied!";
        setTimeout(() => (btn.innerText = "Copy Code"), 1500);
    });
});
