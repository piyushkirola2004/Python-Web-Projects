document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll(".section");
    const toast = document.getElementById("toast");
    const themeBtn = document.getElementById("themeBtn");

    // ----- Section switching -----
    window.showSection = function (id) {
        sections.forEach(s => s.classList.remove("active"));
        document.getElementById(id).classList.add("active");
    };

    // ----- Form handling -----
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", () => {
            sessionStorage.setItem("added", "true");
        });
    }

    if (sessionStorage.getItem("added")) {
        showToast("✅ Student added successfully!");
        sessionStorage.removeItem("added");
        showSection("view");
    }

    function showToast(msg) {
        toast.textContent = msg;
        toast.style.display = "block";
        setTimeout(() => (toast.style.display = "none"), 2000);
    }

    // ----- Theme toggle -----
    const savedTheme = localStorage.getItem("theme") || "dark";
    document.documentElement.setAttribute("data-theme", savedTheme);
    updateThemeIcon(savedTheme);

    themeBtn.addEventListener("click", () => {
        const current = document.documentElement.getAttribute("data-theme");
        const next = current === "light" ? "dark" : "light";
        document.documentElement.setAttribute("data-theme", next);
        localStorage.setItem("theme", next);
        updateThemeIcon(next);
    });

    function updateThemeIcon(theme) {
        themeBtn.textContent = theme === "light" ? "🌞" : "🌙";
    }
});
