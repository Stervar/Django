const feedbackForm = document.getElementById('feedback-form');

feedbackForm.addEventListener('submit', event => {
    event.preventDefault();
    const formData = new FormData(feedbackForm);
    // Логика отправки формы
});