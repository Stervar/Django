function showDetails(productId) {
    const productDetails = {
        'product-1': {
description: 'Скутер в отличном состоянии поэтому торга нет! Ремень оригинальный новый! Вариатор оригинальный новый! Ролики оригинал! Сцепление новое оригинальное! Колодки новые оригинальные! Резина перед и зад новая-хорошая, имеется боковая подножка! Пружина на сцеплении — малосси! В горку летит! Скорость по прямой 65км/ч. Вложений не требует! Обмена и рассрочки нет! Торга тоже! Покупал месяц назад! Пробег 7416.',
            rating: 4.5,
            reviews: 12,
        },
        // Добавьте больше информации о мопедах здесь
    };

    const productCard = document.getElementById(productId);
    const productDescription = productCard.querySelector('.description');
    const productRating = productCard.querySelector('.rating');

    productDescription.textContent = productDetails[productId].description;
    productRating.textContent = `★★★★☆ (${productDetails[productId].reviews} отзывов)`;
}