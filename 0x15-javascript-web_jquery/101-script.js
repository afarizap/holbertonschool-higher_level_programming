$('DIV#add_item').click(() => $('UL.my_list').append('<li>Item</li>'));
$('DIV#remove_item').click(() => $('UL.my_list').children().last().remove());
$('DIV#clear_list').click(() => $('UL.my_list').children().remove());