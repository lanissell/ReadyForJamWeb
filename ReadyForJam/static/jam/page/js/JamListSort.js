document.addEventListener('DOMContentLoaded', function () {
    const quantitySortBtn = document.querySelector('#quantity_sort_btn');
    const listParent = document.querySelector('#jam-list');
    let isReverse = true;
    quantitySortBtn.addEventListener('click', function () {
        isReverse = !isReverse;
        let xhr = new XMLHttpRequest();
        xhr.open('POST', window.location.pathname, true);
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
        xhr.addEventListener('readystatechange', function () {
            if ((xhr.readyState === 4) && (xhr.status === 200)) {
                let data = JSON.parse(xhr.response);
                let parser = new DOMParser();
                let doc = parser.parseFromString(data['sort_by_choice'], 'text/html');
                listParent.replaceChildren(doc.querySelector('.list__container'))
                if (isReverse) quantitySortBtn.classList.remove('rotate')
                else quantitySortBtn.classList.add('rotate')
            }
        });
        xhr.setRequestHeader("X-CSRFToken", GetCookie('csrftoken'));
        xhr.send(JSON.stringify({"is_quantity_reverse": isReverse}))
    });
})

function GetCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}