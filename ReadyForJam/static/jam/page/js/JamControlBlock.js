let jamColor;
let isStart = false;
const localPath = window.location.pathname.replace('projects/', '')
const acceptText = 'Принять участие';
const unAcceptText = 'Отказаться от участия';

SetJamControlBlock();

function SetJamControlBlock() {
    let data = null;
    let blockParent = document.querySelector('.jam-block__button-block');
    let xhr = new XMLHttpRequest();
    xhr.open('GET', localPath + 'blockControl/', true);

    xhr.addEventListener('readystatechange', function () {

        if ((xhr.readyState === 4) && (xhr.status === 200)) {
            data = JSON.parse(xhr.response);
            let url = data.url;
            if (url) {
                window.location.href = data.url;
            } else {
                if (data.theme) isStart=true;
                jamColor = data.color;
                let projectBtn = GetButtonHtml('projectRegister', 'Добавить проект');
                projectBtn.id = 'project_btn';
                blockParent.append(projectBtn);
                DisableProjectBtn();
                AppendTimer(data);
                if (data.isAuthor) {
                    AppendAuthorControl(blockParent);
                } else {
                    AppendUserControl(data, blockParent);
                }
                document.querySelector('.load-wrapper').remove();
            }
        }
    })

    xhr.setRequestHeader("X-CSRFToken", GetCookie('csrftoken'));
    xhr.send();
}

function AppendTimer(data) {
    let content;
    if (isStart) {
        content = GetThemeHTML(data.theme);
    } else {
        content = GetTimerHTML(data.date);
    }
    let parent = document.querySelector('.jam-block__timer-container');
    parent.append(content);
}

function AppendAuthorControl(blockParent) {
    let btn = GetButtonHtml('update', 'Обновить');
    btn.id = 'update_button';
    blockParent.append(btn);

    btn = GetButtonHtml('', 'Удалить');
    btn.id = 'delete_button';
    blockParent.append(btn);
}

function AppendUserControl(data, blockParent) {
    let btn = GetButtonHtml('participate', acceptText);
    btn.id = 'participate_button';
    if (data.isParticipant)
        btn = FlipParticipateBtnStyle(btn);
    blockParent.append(btn);
    ActivateParticipateButton();
}

function ActivateParticipateButton() {
    let btn = document.querySelector("#participate_button");

    btn.addEventListener("click", function () {
        let xhr = new XMLHttpRequest();
        xhr.open('GET', localPath + 'participate/', true);
        xhr.addEventListener('readystatechange', function () {
            if ((xhr.readyState === 4) && (xhr.status === 200)) {
                let data = JSON.parse(xhr.response);
                let url = data.url;
                if (url)
                    window.location.href = data.url;
                else
                    btn.replaceWith(FlipParticipateBtnStyle(btn));
            }
        })
        xhr.setRequestHeader("X-CSRFToken", GetCookie('csrftoken'));
        xhr.send();
    })
}

function GetButtonHtml(href, title) {
    let btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'jam-block__button';
    if (href !== 'participate' && href !== '') {
        btn.addEventListener('click', function () {
            window.location.href = localPath + href;
        })
    }
    btn.insertAdjacentHTML('beforeend', `<div class="button-block__link">${title}</div>`);
    SetActiveBtnStyle(btn);
    btn.onmouseover = function (){
        btn.style.borderColor = jamColor.main_text_color;
    }
    btn.onmouseout = function (){
        btn = SetActiveBtnStyle(btn)
    }
    return btn;
}

function GetThemeHTML(theme) {
    let themeDiv = document.createElement('div');
    themeDiv.append(theme);
    themeDiv.id = 'timer'
    return themeDiv;
}

function GetTimerHTML(startDate) {
    let timer = document.createElement('div');
    timer.id = 'timer';
    let date = document.createElement('textarea');
    date.id = 'startDate';
    date.style.display = 'none';
    date.append(startDate);
    timer.append(date);
    let html = '<div id="days">00</div>\n' +
        '              <div class="jam-block__time-separator">д:</div>\n' +
        '              <div id="hours">00</div>\n' +
        '              <div class="jam-block__time-separator">ч:</div>\n' +
        '              <div id="minutes">00</div>\n' +
        '              <div class="jam-block__time-separator">м:</div>\n' +
        '              <div id="seconds">00</div>' +
        '              <div class="jam-block__time-separator">с</div>\n'
    timer.style.color = jamColor.main_text_color;
    timer.insertAdjacentHTML('beforeend', html)
    return timer
}

function FlipParticipateBtnStyle(btn) {
    if (btn.children[0].innerHTML === unAcceptText) {
        btn.children[0].innerHTML = acceptText;

        DisableProjectBtn();

        return SetActiveBtnStyle(btn);
    } else {
        btn.children[0].innerHTML = unAcceptText;

        let projectBtn = document.querySelector('#project_btn');
        if (projectBtn && isStart) projectBtn.style.display = '';

        return btn;
    }

}

function DisableProjectBtn(){
    let projectBtn = document.querySelector('#project_btn');
    if (projectBtn) projectBtn.style.display = 'none';
}

function SetActiveBtnStyle(btn) {
    btn.style.borderColor = 'rgba(0,0,0,0)';
    btn.style.color = jamColor.main_text_color;
    btn.style.background = jamColor.background_color;
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