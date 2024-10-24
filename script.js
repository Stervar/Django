// // script.js
// function updateDateTime() {
//     const now = new Date();
//     const options = { 
//         year: 'numeric', 
//         month: 'long', 
//         day: 'numeric', 
//         hour: '2-digit', 
//         minute: '2-digit', 
//         second: '2-digit', 
//         hour12: false 
//     };
//     const formattedDateTime = now.toLocaleString('ru-RU', options);
//     document.getElementById('datetime').textContent = formattedDateTime;
// }

// // Обновляем дату и время каждую секунду
// setInterval(updateDateTime, 1000);

// // Первоначальный вызов для отображения времени сразу
// updateDateTime();