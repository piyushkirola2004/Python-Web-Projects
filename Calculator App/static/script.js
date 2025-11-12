function toggleQuantile() {
    const operation = document.getElementById("operation").value;
    const box = document.getElementById("quantile-box");
    const addBtn = document.getElementById("add-number-btn");
    const calculateBtn = document.getElementById("calculate-btn");

    box.style.display = (operation === "quantile") ? "block" : "none";

    if (operation === "add" || operation === "multiply") {
        addBtn.style.display = "inline-block";
    } else {
        addBtn.style.display = "none";
    }

    calculateBtn.classList.remove("pulse");
}

// Add new number input dynamically with animation and pulse button
document.getElementById("add-number-btn").addEventListener("click", () => {
    const container = document.getElementById("numbers-container");
    const input = document.createElement("input");
    input.type = "number";
    input.name = "numbers";
    input.placeholder = "Enter number";
    input.step = "any";
    input.required = true;
    input.classList.add("new-number");
    container.appendChild(input);

    const calculateBtn = document.getElementById("calculate-btn");
    calculateBtn.classList.add("pulse");
});

// Initial setup
toggleQuantile();
