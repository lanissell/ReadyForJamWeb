const dropdown = document.querySelector('.dropdown');

// Toggle active class on click
dropdown.addEventListener('click', () => {
    dropdown.classList.toggle('active');
});

// Handle clicking on an icon
const icons = document.querySelectorAll('.dropdown-content a');
icons.forEach(icon => {
    icon.addEventListener('click', () => {
        const selectedIcon = icon.textContent;
        const dropdownIcon = document.querySelector('.dropdown img');
        dropdownIcon.setAttribute('alt', selectedIcon);
        dropdown.classList.remove('active');
    });
});