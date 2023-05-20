document.addEventListener('DOMContentLoaded', SetCriteria)

function SetCriteria() {
    let data = null;
    let blockParent = document.querySelector('.jam-block__button-block');
    let xhr = new XMLHttpRequest();
    xhr.open('GET', window.location.pathname.replace('projects/', '') + 'criteria/', true);

    xhr.addEventListener('readystatechange', function () {

        if ((xhr.readyState === 4) && (xhr.status === 200)) {
            data = JSON.parse(xhr.response);
            let cards = document.querySelectorAll('.jam-list__name');
            cards.forEach(card => {
                let criteriaArray = data[card.firstElementChild.innerHTML]
                let table = card.parentElement.querySelector('.jam-list__table').firstElementChild
                let borderColor = table.firstElementChild.style.borderColor;
                criteriaArray.forEach(criteria => {
                    let tr = document.createElement('tr');
                    tr.style.borderColor = borderColor;
                    criteria = JSON.parse(criteria);

                    Object.entries(criteria).forEach(([key, value]) => {
                        let th = document.createElement('th');
                        th.innerHTML = value;
                        tr.insertAdjacentElement('beforeend', th)
                    })
                    table.insertAdjacentElement('beforeend', tr)
                })
            })
        }
    })

    xhr.setRequestHeader("X-CSRFToken", GetCookie('csrftoken'));
    xhr.send();
}