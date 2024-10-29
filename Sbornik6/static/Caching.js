const cache = {};

function getProducts() {
    // Логика получения товаров
    const products = [];
    cache.products = products;
    return products;
}

function getProductDetails(productId) {
    // Логика получения подробной информации о мопеде
    const productDetails = cache.products.find(product => product.id === productId);
    return productDetails;
}