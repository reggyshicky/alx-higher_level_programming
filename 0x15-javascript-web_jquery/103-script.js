$(function () {
  $('btn_translate').bind('click', function () {
    const language = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + language,
      function (data) {
        $('#hello').text(data.hello);
      });
  });
  $('#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      const lang = $('#language_code').val();
      $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang,
        function (data) {
          $('#hello').text(data.hell0);
        });
    }
  });
});
