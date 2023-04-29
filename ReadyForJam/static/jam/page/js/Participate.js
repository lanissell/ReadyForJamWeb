document.addEventListener("DOMContentLoaded", function () {
    const btn = document.querySelector("#participate_button");
    console.log(window.location.pathname)
    btn.addEventListener("click", function () {

        let xhr = new XMLHttpRequest();
        xhr.open('GET', window.location.pathname+'participate/', true);

        xhr.addEventListener('readystatechange', function () {
            if ((xhr.readyState === 4) && (xhr.status === 200)) {
                let data = JSON.parse(xhr.response);
                let url = data.url
                if (url)
                    window.location.href = data.url
            }
        })

        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));

        xhr.send();
    })
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}