let divElements = document.querySelectorAll('.toggle');

divElements.forEach((element) => {
    let contentDiv = element.nextElementSibling;
    element.addEventListener('click', (e) => {
        if (contentDiv.style.display === 'none') {
            contentDiv.style.display = 'block';
        } else {
            contentDiv.style.display = 'none';
        }
    });
});