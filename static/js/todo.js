let divElements = document.querySelectorAll('.to_do_item');

divElements.forEach((element) => {
    let contentDiv = element.children[1];
    element.addEventListener('click', (e) => {
        if (contentDiv.style.display === 'none') {
            contentDiv.style.display = 'block';
        } else {
            contentDiv.style.display = 'none';

        }
    });
});