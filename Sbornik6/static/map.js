const mapElement = document.getElementById('map');

const mapOptions = {
    center: {lat: 43.5993, lng: 39.7323},
    zoom: 15,
};

// Измените имя переменной на mapInstance или другое
const mapInstance = new google.maps.Map(mapElement, mapOptions);

const marker = new google.maps.Marker({
    position: {lat: 43.5993, lng: 39.7323},
    map: mapInstance,
    title: 'Магазин мопедов',
});