document.addEventListener('DOMContentLoaded', function () {
    const quantitySortBtn = $('#quantity_sort_btn');
    const listParent = $('#jam-list');
    let isReverse = false;
    quantitySortBtn[0].addEventListener('click', function () {
        $.ajax({
            url: window.location.pathname,
            method: 'post',
            dataType: 'json',
            data: JSON.stringify({"is_quantity_reverse": isReverse}),
            headers: {'X-CSRFToken': GetCookie('csrftoken')},
            success: function (data) {
                isReverse = !isReverse;
                let parser = new DOMParser();
                let doc = parser.parseFromString(data['sort_by_choice'], 'text/html');
                listParent[0].replaceChildren(doc.querySelector('.list__container'));
                if (isReverse) quantitySortBtn[0].classList.add('rotate');
                else quantitySortBtn[0].classList.remove('rotate');
            }
        })
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