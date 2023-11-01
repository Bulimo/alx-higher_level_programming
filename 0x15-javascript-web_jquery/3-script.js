/* global $ */

$(document).ready(function () {
  // Use jQuery to select the <header> element and adds class red when clicked
  $('#red_header').on('click', function () {
    $(this).addClass('red');
  });
});
