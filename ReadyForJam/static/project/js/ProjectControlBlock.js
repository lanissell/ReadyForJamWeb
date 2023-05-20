let colors = null;
const localPath = window.location.pathname;

document.addEventListener('DOMContentLoaded', SetControlBlock)

function SetControlBlock() {
    let data = null;
    let blockParent = document.querySelector('.jam-block__button-block');
    let xhr = new XMLHttpRequest();
    xhr.open('GET', localPath + 'blockControl', true);
    xhr.addEventListener('readystatechange', function () {
        if ((xhr.readyState === 4) && (xhr.status === 200)) {
            data = JSON.parse(xhr.response);
            colors = data.projectColor;
            let parent = document.querySelector('.jam-block__timer-container');
            parent.append(GetJamNameHTML(data.jamName));
            if (data.isAuthor) {
                blockParent.append(GetButtonHtml('update/', 'Изменить'));

                let deleteBtn = GetButtonHtml('', 'Удалить');
                deleteBtn.id = 'delete_button';
                blockParent.append(deleteBtn);
            } else {
                blockParent.remove();
            }
            document.querySelector('.load-wrapper').remove();
        }
    });
    xhr.setRequestHeader("X-CSRFToken", GetCookie('csrftoken'));
    xhr.send();
}

function GetJamNameHTML(jamName) {
    let themeDiv = document.createElement('div');
    themeDiv.append(jamName);
    themeDiv.id = 'timer'
    themeDiv.onclick = function (){
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
    if (href !== ''){
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