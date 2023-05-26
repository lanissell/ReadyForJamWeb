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
                InsertTh(tr, '+');
                table.insertAdjacentElement('beforeend', tr)
            })
        })
    }
})


function InsertTh(tableRow, thInnerHtml) {
    let th = document.createElement('th');
    th.innerHTML = thInnerHtml;
    tableRow.insertAdjacentElement('beforeend', th)
}