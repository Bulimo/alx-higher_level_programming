/* global $ */

$(document).ready(function () {
  // Make an AJAX request to fetch the translation
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Extract the translation of "hello" from the response data
    const translation = data.hello;

    // Display the translation in DIV#hello
    $('DIV#hello').text(translation);
  });
});
