let jamColor;
let blockParent = $('.jam-block__button-block');
let isStart = false;
const localPath = window.location.pathname.replace('projects/', '')
const acceptText = 'Принять участие';
const unAcceptText = 'Отказаться от участия';

$.when(
    $.ajax({
        url: localPath + 'blockControl/',
        method: 'get',
        dataType: 'json',
        success: function (data) {
            let url = data.url;
            if (url) {
                window.location.href = data.url;
            } else {
                jamColor = data.color;
                AppendControlBlock(data);
            }
        }
    }).done(function () {
        const time = 300;
        const dfd = $.Deferred();
        $('.load-wrapper').fadeOut(time, dfd.resolve);
        dfd.done(function () {
            $('#timer').fadeIn(time);
        });
    }).fail(function () {
        alert('Ошибка загрузки даты, попробуйте перезагрузить страницу')
    })
);

function AppendControlBlock(data) {
    let projectBtn = GetButtonHtml('projectRegister', 'Добавить проект');
    projectBtn.id = 'project_btn';
    blockParent.append(projectBtn);
    DisableProjectBtn();
    let parent = document.querySelector('.jam-block__timer-container');
    if (data.theme) {
        AppendTheme(parent, data)
        isStart = true;
    } else {
        AppendTimer(parent, data)
    }
    if (data.isAuthor) {
        AppendAuthorControl(blockParent);
    } else {
        AppendUserControl(data, blockParent);
    }
}

function AppendTimer(parent, data) {
    let content = GetTimerHTML(data.date);
    content.style.display = 'none';
    parent.append(content);
}

function AppendTheme(parent, data) {
    let content = GetThemeHTML(data.theme);
    content.style.display = 'none';
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
    let btn = $('#participate_button');
    btn.click(function () {
        $.ajax({
            url: localPath + 'participate/',
            method: 'get',
            dataType: 'json',
            success: function (data) {
                let url = data.url;
                if (url)
                    window.location.href = data.url;
                else
                    btn[0].replaceWith(FlipParticipateBtnStyle(btn[0]));
            }
        })
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
    btn.onmouseover = function () {
        btn.style.borderColor = jamColor.main_text_color;
    }
    btn.onmouseout = function () {
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

function DisableProjectBtn() {
    let projectBtn = document.querySelector('#project_btn');
    if (projectBtn) projectBtn.style.display = 'none';
}

function SetActiveBtnStyle(btn) {
    btn.style.borderColor = 'rgba(0,0,0,0)';
    btn.style.color = jamColor.main_text_color;
    btn.style.background = jamColor.background_color;
    return btn;
}

