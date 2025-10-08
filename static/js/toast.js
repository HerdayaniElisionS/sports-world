function showToast(message, type = "info") {
    const toast = document.getElementById("toast");
    const text = document.getElementById("toast-message");

    // Set message text
    text.textContent = message;

    // Reset color classes (so it can change each time)
    toast.classList.remove("border-green-500", "border-red-500", "border-blue-500");

    // Add color depending on type (matches tutorial logic)
    if (type === "success") toast.classList.add("border-green-500");
    else if (type === "error") toast.classList.add("border-red-500");
    else toast.classList.add("border-blue-500");

    // Show toast (slide down)
    toast.classList.remove("opacity-0", "-translate-y-5");
    toast.classList.add("opacity-100", "translate-y-0");

    // Hide automatically after 2.5 seconds
    setTimeout(() => {
        toast.classList.remove("opacity-100", "translate-y-0");
        toast.classList.add("opacity-0", "-translate-y-5");
    }, 2500);
}

// ✅ Helper: Get CSRF token
function getCookie(name) {
    const m = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return m ? m.pop() : '';
}
const CSRF = getCookie('csrftoken');

// ✅ Elements
const grid = document.getElementById('productGrid');
const loading = document.getElementById('loading');
const error = document.getElementById('error');
const empty = document.getElementById('empty');
const refreshBtn = document.getElementById('refreshBtn');

// ✅ Load products
async function loadProducts() {
    grid.innerHTML = '';
    loading.classList.remove('hidden');
    error.classList.add('hidden');
    empty.classList.add('hidden');

    try {
        const response = await fetch('/json/');
        if (!response.ok) throw new Error('Request failed');
        const products = await response.json();

        loading.classList.add('hidden');

        if (products.length === 0) {
            empty.classList.remove('hidden');
            return;
        }

        products.forEach(p => {
            const item = document.createElement('div');
            item.className = "bg-white rounded-2xl border border-gray-200 overflow-hidden hover:shadow-lg transition-shadow";
            const data = JSON.parse(p.fields_json || JSON.stringify(p.fields));

            item.innerHTML = `
                <div class="h-48 bg-gray-100 flex items-center justify-center overflow-hidden">
                    ${data.thumbnail ? `<img src="${DOMPurify.sanitize(data.thumbnail)}" class="w-full h-full object-cover" />` : `<div class="text-gray-400 text-sm">No image</div>`}
                </div>
                <div class="p-4">
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">${DOMPurify.sanitize(data.name)}</h3>
                    <p class="text-gray-600 text-sm mb-3">${DOMPurify.sanitize(data.description)}</p>
                    <div class="flex justify-between items-center">
                        <span class="text-lg font-bold text-gray-900">Rp ${data.price}</span>
                        ${data.is_featured ? `<span class="text-xs bg-yellow-100 text-yellow-800 px-3 py-1 rounded-full">Featured</span>` : ""}
                    </div>
                    <div class="mt-3 flex space-x-2">
                        <button onclick="showEditModal(${p.pk}, '${data.name}', '${data.description}', ${data.price}, '${data.category}', '${data.thumbnail}', ${data.is_featured})"
                                class="bg-yellow-500 hover:bg-yellow-600 text-white px-4 py-2 rounded-lg text-sm">Edit</button>
                        <button onclick="deleteProduct(${p.pk})"
                                class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg text-sm">Delete</button>
                    </div>
                </div>
            `;
            grid.appendChild(item);
        });
    } catch (err) {
        console.error(err);
        loading.classList.add('hidden');
        error.classList.remove('hidden');
    }
}

// ✅ Delete product
async function deleteProduct(id) {
    if (!confirm("Are you sure you want to delete this product?")) return;
    const res = await fetch(`/delete-product-ajax/${id}/`, {
        method: 'POST',
        headers: {'X-CSRFToken': CSRF},
    });
    const data = await res.json();
    if (data.status === 'success') {
        showToast('Product deleted', 'success');
        loadProducts();
    } else {
        showToast('Failed to delete product', 'error');
    }
}

// ✅ Create product
async function createProduct(formData) {
    const res = await fetch('/create-product-ajax/', {
        method: 'POST',
        headers: {'X-CSRFToken': CSRF},
        body: formData,
    });
    const data = await res.json();
    if (data.status === 'success') {
        showToast('Product created', 'success');
        closeModal();
        loadProducts();
    } else {
        showToast('Failed to create product', 'error');
    }
}

// ✅ Edit product (simplified)
async function updateProduct(id, formData) {
    const res = await fetch(`/update-product-ajax/${id}/`, {
        method: 'POST',
        headers: {'X-CSRFToken': CSRF},
        body: formData,
    });
    const data = await res.json();
    if (data.status === 'success') {
        showToast('Product updated', 'success');
        closeModal();
        loadProducts();
    } else {
        showToast('Failed to update product', 'error');
    }
}

// ✅ Refresh button
if (refreshBtn) {
    refreshBtn.addEventListener('click', loadProducts);
}

// ✅ Auto-load when page opens
document.addEventListener('DOMContentLoaded', loadProducts);
