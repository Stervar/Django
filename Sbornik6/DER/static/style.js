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

document.addEventListener('DOMContentLoaded', function() {
    updateTime();

    const mainContainer = document.querySelector('.main-container');
    const iconSection = document.getElementById('iconSection');
    const showIconBtn = document.getElementById('showIcon');
    const backToTimeBtn = document.getElementById('backToTime');

    showIconBtn.addEventListener('click', function() {
        mainContainer.style.display = 'none';
        iconSection.style.display = 'block';
    });

    backToTimeBtn.addEventListener('click', function() {
        iconSection.style.display = 'none';
        mainContainer.style.display = 'block';
    });
});