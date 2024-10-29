const images = document.querySelectorAll('img');

images.forEach(image => {
    const src = image.getAttribute('data-src');
    image.src = src;
});