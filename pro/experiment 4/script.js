// Smooth scroll
document.querySelectorAll("a[href^='#']").forEach(anchor => {
    anchor.addEventListener("click", function(e){
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});

// Dark/Light mode toggle
const themeBtn = document.querySelector(".theme-btn");
themeBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    themeBtn.textContent = document.body.classList.contains("dark") ? "☀ Light Mode" : "🌙 Dark Mode";
});

// FAQ accordion
document.querySelectorAll(".faq-item").forEach(item => {
    item.addEventListener("click", () => {
        item.classList.toggle("open");
        const answer = item.querySelector(".answer");
        answer.style.maxHeight = item.classList.contains("open") ? answer.scrollHeight + "px" : "0px";
    });
});

// Appointment form submit
const form = document.getElementById("appointmentForm");
const formMessage = document.getElementById("formMessage");

form.addEventListener("submit", function(e){
    e.preventDefault();
    formMessage.textContent = "Thank you! Your appointment request has been received.";
    form.reset();
});
