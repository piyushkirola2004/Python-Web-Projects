let cart = [];

// 🔥 Preload all product images before showing them
function preloadImages(imageList, callback) {
    let loaded = 0;
    const total = imageList.length;

    if (total === 0) {
        callback();
        return;
    }

    imageList.forEach(src => {
        const img = new Image();
        img.src = src;
        img.onload = () => {
            loaded++;
            if (loaded === total) callback();
        };
        img.onerror = () => {
            loaded++;
            if (loaded === total) callback();
        };
    });
}

// ⚙️ Load items dynamically from Python backend
async function loadItems() {
    const res = await fetch('/get_items');
    const items = await res.json();
    const store = document.getElementById('store');

    // Create list of image URLs to preload
    const imagePaths = Object.values(items).map(
        item => `/static/images/${item.name.toLowerCase().trim()}.jpg`
    );

    preloadImages(imagePaths, () => {
        store.innerHTML = ''; // Clear loader or placeholder

        for (let id in items) {
            const item = items[id];
            const imagePath = `/static/images/${item.name.toLowerCase().trim()}.jpg`;

            const card = document.createElement('div');
            card.className = 'item';
            card.innerHTML = `
                <div class="image-container">
                    <img src="${imagePath}" alt="${item.name}">
                </div>
                <div class="info">
                    <h3>${item.name}</h3>
                    <p>Price: ₹${item.price}</p>
                    <input type="number" id="qty-${id}" min="1" value="1" style="width:60px;padding:4px;margin-top:5px;border-radius:8px;border:1px solid #ccc;">
                    <button onclick="addToCart('${item.name}', ${item.price}, ${id})">Add to Cart</button>
                </div>
            `;
            store.appendChild(card);
        }

        // Small fade-in animation when loaded
        store.style.opacity = 0;
        setTimeout(() => (store.style.opacity = 1), 100);
    });
}

// ➕ Add to Cart
function addToCart(name, price, id) {
    const qty = parseInt(document.getElementById(`qty-${id}`).value);
    if (qty < 1) return;
    const total = qty * price;
    cart.push({ name, qty, total });
    updateCart();
    updateCartCount();
}

// 🛒 Update Cart View
function updateCart() {
    const cartDiv = document.getElementById('cart-items');
    cartDiv.innerHTML = '';
    let totalAmount = 0;

    cart.forEach((item, index) => {
        cartDiv.innerHTML += `
            <p>${item.name} × ${item.qty} = ₹${item.total}
            <button style="background:red;color:white;border:none;border-radius:5px;padding:2px 6px;margin-left:8px;cursor:pointer;" onclick="removeItem(${index})">x</button></p>
        `;
        totalAmount += item.total;
    });

    document.getElementById('total').innerText = `Total: ₹${totalAmount}`;
}

// ❌ Remove Item
function removeItem(index) {
    cart.splice(index, 1);
    updateCart();
    updateCartCount();
}

// 💵 Checkout
document.getElementById('checkout').addEventListener('click', async () => {
    if (cart.length === 0) return alert("🛒 Cart is empty!");

    const res = await fetch('/generate_bill', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ purchases: cart })
    });

    const data = await res.json();
    alert(`✅ Bill Generated!\n💰 Total: ₹${data.bill}\n📁 Saved as: ${data.filename}`);
    cart = [];
    updateCart();
    updateCartCount();
});

// 🔢 Floating Cart Count Badge
function updateCartCount() {
    let badge = document.getElementById('cart-count');
    if (!badge) {
        badge = document.createElement('div');
        badge.id = 'cart-count';
        badge.style.position = 'fixed';
        badge.style.bottom = '70px';
        badge.style.right = '25px';
        badge.style.background = 'linear-gradient(90deg, #2575fc, #6a11cb)';
        badge.style.color = 'white';
        badge.style.borderRadius = '50%';
        badge.style.width = '35px';
        badge.style.height = '35px';
        badge.style.display = 'flex';
        badge.style.alignItems = 'center';
        badge.style.justifyContent = 'center';
        badge.style.fontWeight = '600';
        badge.style.boxShadow = '0 4px 15px rgba(0,0,0,0.3)';
        badge.style.transition = 'all 0.3s ease';
        document.body.appendChild(badge);
    }
    badge.textContent = cart.length;
    badge.style.transform = 'scale(1.2)';
    setTimeout(() => (badge.style.transform = 'scale(1)'), 150);
}

// 🌙 Dark Mode Toggle
const toggleBtn = document.getElementById("theme-toggle");
const currentTheme = localStorage.getItem("theme");

if (currentTheme === "dark") {
    document.body.classList.add("dark");
    toggleBtn.textContent = "☀️ Light Mode";
}

toggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    const theme = document.body.classList.contains("dark") ? "dark" : "light";
    localStorage.setItem("theme", theme);
    toggleBtn.textContent = theme === "dark" ? "☀️ Light Mode" : "🌙 Dark Mode";
});

// 🚀 Initialize
loadItems();
