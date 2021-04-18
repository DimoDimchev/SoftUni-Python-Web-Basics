let listElements = document.querySelectorAll('li');

listElements.forEach((element) => {
    element.addEventListener('mouseover', () => {
        element.style.color = 'blue';
    });
    
    element.addEventListener('mouseout', () => {
        element.style.color = 'black';
    });
})

