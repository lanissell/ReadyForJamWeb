$(document).ready(function(){
    let is_reverse = true;
    $('#quantity_sort_btn').on('click', function() {
        is_reverse.reverse();
        $.ajax({
            type: 'POST',
            url: $(this).data('url'),
            datatype: 'json',
            data: {'is_quantity_reverse': is_reverse}
        }).done(function (data) {
            $('.product-wrapper').html(data.sort_by_choice);
        });
    });

});