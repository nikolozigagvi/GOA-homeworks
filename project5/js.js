let quantity = 0;

function increase() {
    quantity++;
    document.getElementById("qty").innerText = quantity;
}

function decrease() {
    if (quantity > 0) {
        quantity--;
        document.getElementById("qty").innerText = quantity;
    }
}

function addToCart() {
    if (quantity === 0) {
        alert("Please select quantity first!");
    } else {
        alert(quantity + " item(s) added to cart 🛒");
    }
}

function changeImage(src) {
    document.getElementById("mainImage").src = src;
}