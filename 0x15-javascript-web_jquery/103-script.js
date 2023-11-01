/* global $ */

$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    fetchTranslation();
  });

  $('#language_code').on('keypress', function (event) {
    if (event.which === 13) { // Enter key
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  }
});
