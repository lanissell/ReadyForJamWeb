let colors = null;
const localPath = window.location.pathname;

$.ajax({
    url: localPath + 'blockControl',
    method: 'get',
    headers: {'X-CSRFToken': GetCookie('csrftoken')},
    dataType: 'json',
    success: function (data) {
        colors = data.projectColor;
        let buttonParent = $('.jam-block__button-block')[0];
        let timerParent = $('.jam-block__timer-container')[0];
        timerParent.append(GetJamNameHTML(data.jamName));
        if (data.isAuthor) {
            buttonParent.append(GetButtonHtml('update/', 'Изменить'));
            let deleteBtn = GetButtonHtml('', 'Удалить');
            deleteBtn.id = 'delete_button';
            buttonParent.append(deleteBtn);
        } else {
            buttonParent.remove();
        }
        document.querySelector('.load-wrapper').remove();
    }
})

function GetJamNameHTML(jamName) {
    let themeDiv = document.createElement('div');
    themeDiv.append(jamName);
    themeDiv.id = 'timer'
    themeDiv.onclick = function () {
        window.location.href = `/jam/${jamName}`
    }
    themeDiv.style.cursor = 'pointer';
    return themeDiv;
}

function GetButtonHtml(href, title) {
    let btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'jam-block__button';
    btn.insertAdjacentHTML('beforeend', `<div class="button-block__link">${title}</div>`);
    SetActiveBtnStyle(btn);
    if (href !== '') {
        btn.addEventListener('click', function () {
            window.location.href = localPath + href;
        })
    }
    btn.onmouseover = function () {
        btn.style.borderColor = colors.main_text_color;
        btn.style.color = colors.main_text_color;
    }
    btn.onmouseout = function () {
        btn = SetActiveBtnStyle(btn)
    }
    return btn;
}

function SetActiveBtnStyle(btn) {
    btn.style.borderColor = 'rgba(0,0,0,0)';
    btn.style.color = colors.form_color;
    btn.style.background = colors.background_color;
    return btn;
}

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