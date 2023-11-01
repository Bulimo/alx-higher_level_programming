/* global $ */

$(document).ready(function () {
  // Use jQuery to select the <header> element and updates the text to New Header!!!
  $('DIV#update_header').on('click', function () {
    // Update the text of the <header> element to "New Header!!!"
    $('header').text('New Header!!!');
  });
});
