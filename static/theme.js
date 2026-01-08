const toggle = document.getElementById("theme-toggle");
const root = document.documentElement;

const savedTheme = localStorage.getItem("theme");
if (savedTheme) {
    root.setAttribute("data-theme", savedTheme);
    toggle.textContent = savedTheme === "light" ? "🌙" : "☀️";
}

toggle.addEventListener("click", () => {
    const isLight = root.getAttribute("data-theme") === "light";
    const newTheme = isLight ? "dark" : "light";

    root.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);
    toggle.textContent = newTheme === "light" ? "🌙" : "☀️";
});
