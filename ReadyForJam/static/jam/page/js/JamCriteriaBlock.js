const bgColor = $('body').css('backgroundColor');
const formColor = $('.jam-block__list').css('backgroundColor');
const textColor = $('.text-block__name').css('color');

$.ajax({
    url: window.location.pathname.replace('projects/', '')
        + 'criteria/',
    method: 'get',
    dataType: 'json',
    success: function (data) {
        let cards = $('.jam-list__name');
        cards.each(function (index, card) {
            let criteriaArray = data[card.firstElementChild.innerHTML]
            let table = card.parentElement.querySelector('.jam-list__table').firstElementChild
            let borderColor = table.firstElementChild.style.borderColor;
            Object.entries(criteriaArray).forEach(([key, value]) => {
                let tr = document.createElement('tr');
                tr.style.borderColor = borderColor;
                InsertTh(tr, key);
                InsertTh(tr, value['rank']);
                InsertTh(tr, value['count']);
                InsertTh(tr, GetVoteBtn(value['isVote']));
                table.insertAdjacentElement('beforeend', tr)
            });
        });
    }
}).done(function () {
    $('.vote_button').on('click', function (event) {
        let target = event.target
        let criteriaName = GetParent(target, 2)
            .firstElementChild.innerHTML;
        let projectName = GetParent(target, 5).firstElementChild.firstElementChild.innerHTML
        $.ajax({
            url: window.location.pathname + 'vote/',
            method: 'post',
            headers: {'X-CSRFToken': $('meta[name="csrf-token"]').attr('content')},
            dataType: 'json',
            data: {'criteriaName': criteriaName, 'projectName': projectName},
            success: function (data) {
                let command = data['command'];
                switch (command) {
                    case 'cant':
                        Swal.fire({
                            icon: 'error',
                            title: 'Упс...',
                            text: 'Вы проглосовали по этому критерию за другой проект :(',
                            background: '#414141',
                            color: 'white',
                            confirmButtonColor: '#CA3E47',
                            iconColor: '#CA3E47'
                        })
                        break;
                    case 'reduce':
                        target.innerHTML = '+';
                        target.parentElement.previousElementSibling.innerHTML--;
                        break;
                    case 'voted':
                        target.innerHTML = '-';
                        target.parentElement.previousElementSibling.innerHTML++;
                        break;
                }
            }
        });
    });
});

function InsertTh(tableRow, thInnerHtml) {
    let th = document.createElement('th');
    th.append(thInnerHtml);
    tableRow.insertAdjacentElement('beforeend', th)
}

function GetVoteBtn(isVote) {
    let btn = document.createElement('button');
    let text = '+';
    if (isVote) text = '-'
    btn.innerHTML = text;
    btn.className = 'vote_button';
    $(btn).css({'backgroundColor': formColor, 'color': textColor});

    $(btn).mouseenter(function () {
        $(this).css({
            'backgroundColor': bgColor
        });
    }).mouseleave(function () {
        $(this).css({
            'backgroundColor': formColor
        }, 1);
    });
    return btn;
}

function GetParent(element, count) {
    let parent = element;
    for (let i = 0; i < count; i++) {
        parent = parent.parentElement;
    }
    return parent;
}
