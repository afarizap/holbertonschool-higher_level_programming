function Holis () {
  const lang = $('INPUT#language_code').val();
  $.get('https://www.fourtonfish.com/hellosalut/' + '?lang=' + lang,
        (data) => $('DIV#hello').text(data.hello));
}
$('INPUT#btn_translate').click(Holis);
$('INPUT#language_code').keypress(function (event) {
  var keycode = (event.keyCode ? event.keyCode : event.which);
  if(keycode === 13){
        Holis;  
    }
}); 
