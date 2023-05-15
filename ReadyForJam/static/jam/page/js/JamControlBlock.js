let jamColor;

const acceptText = 'Принять участие';
const unAcceptText = 'Отказаться от участия';

SetJamControlBlock();

function SetJamControlBlock() {
    let data = null;
    let blockParent = document.querySelector('.jam-block__button-block');
    let xhr = new XMLHttpRequest();
    xhr.open('GET', window.location.pathname + 'blockControl/', true);

    xhr.addEventListener('readystatechange', function () {

        if ((xhr.readyState === 4) && (xhr.status === 200)) {
            data = JSON.parse(xhr.response);
            let url = data.url;
            if (url) {
                window.location.href = data.url;
            } else {
                jamColor = data.color;
                let projectBtn = GetButtonHtml('projectRegister', 'Добавить проект');
                projectBtn.id = 'project_btn';
                blockParent.append(projectBtn);
                AppendTimer(data);
                if (data.isAuthor) {
                    AppendAuthorControl(blockParent);
                } else {
                    AppendUserControl(data, blockParent);
                }
                document.querySelector('.load-wrapper').remove()
            }
        }
    })

    xhr.setRequestHeader("X-CSRFToken", GetCookie('csrftoken'));
    xhr.send();
}

function AppendTimer(data) {
    let content;
    if (data.date) {
        content = GetTimerHTML(data.date);
    } else {
        content = GetThemeHTML(data.theme);
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
        btn = FlipBtnStyle(btn);
    blockParent.append(btn);
    ActivateParticipateButton();
}

function ActivateParticipateButton() {
    let btn = document.querySelector("#participate_button");

    btn.addEventListener("click", function () {
        let xhr = new XMLHttpRequest();
        xhr.open('GET', window.location.pathname + 'participate/', true);
        xhr.addEventListener('readystatechange', function () {
            if ((xhr.readyState === 4) && (xhr.status === 200)) {
                let data = JSON.parse(xhr.response);
                let url = data.url;
                if (url)
                    window.location.href = data.url;
                else
                    btn.replaceWith(FlipBtnStyle(btn));
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
            window.location.href = window.location.pathname + href;
        })
    }
    btn.insertAdjacentHTML('beforeend', `<div class="button-block__link">${title}</div>`);
    SetActiveBtnStyle(btn);
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
    timer.insertAdjacentHTML('beforeend', html)
    return timer
}

function FlipBtnStyle(btn) {
    if (btn.style.background === 'none') {
        btn.children[0].innerHTML = acceptText;
        return SetActiveBtnStyle(btn);
    } else {
        btn.children[0].innerHTML = unAcceptText;
        return SetUnActiveBtnStyle(btn);
    }

}

function SetActiveBtnStyle(btn) {
    btn.style.borderColor = 'rgba(0,0,0,0)';
    btn.style.color = jamColor.main_text_color;
    btn.style.background = jamColor.form_color;

    let projectBtn = document.querySelector('#project_btn');
    if (projectBtn) projectBtn.style.display = 'none';
    return btn;
}

function SetUnActiveBtnStyle(btn) {
    btn.style.borderColor = btn.style.backgroundColor;
    btn.style.color = btn.style.backgroundColor;
    btn.style.background = 'none';

    let projectBtn = document.querySelector('#project_btn');
    if (projectBtn) projectBtn.style.display = '';
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