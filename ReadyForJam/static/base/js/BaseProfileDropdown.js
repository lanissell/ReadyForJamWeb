const dropdown = document.querySelector('.dropdown');
const icons = document.querySelectorAll('.dropdown-content a');
// Toggle active class on click
dropdown.addEventListener('mouseenter', () => {
    dropdown.classList.toggle('active');
});

document.addEventListener('mousemove', function (event){
    let target = event.target;
    if (target.id === 'dropdown_elem') return;
    dropdown.classList.remove('active');
})

// Handle clicking on an icon

icons.forEach(icon => {
    icon.addEventListener('mousemove', () => {
        const selectedIcon = icon.textContent;
        const dropdownIcon = document.querySelector('.dropdown img');
        dropdownIcon.setAttribute('alt', selectedIcon);
    });
});