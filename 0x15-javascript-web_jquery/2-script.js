/* global $ */

$(document).ready(function () {
  // Use jQuery to select the <header> element and update its text color to red when clicked
  $('#red_header').on('click', function () {
    $(this).css('color', '#FF0000');
  });
});
