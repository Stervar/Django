function updateTime() {
    const clockElement = document.getElementById('clock');
    const dateElement = document.getElementById('date');
    
    function update() {
        const now = new Date();
        
        // Обновляем время
        clockElement.textContent = now.toLocaleTimeString();
        
        // Обновляем дату
        const options = { 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric' 
        };
        dateElement.textContent = now.toLocaleDateString('ru-RU', options);
    }
    
    // Обновляем каждую секунду
    setInterval(update, 1000);
    update(); // Начальное обновление
}

// Запускаем функцию после загрузки страницы
document.addEventListener('DOMContentLoaded', updateTime);