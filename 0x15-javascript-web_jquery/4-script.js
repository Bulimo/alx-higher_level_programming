/* global $ */

$(document).ready(function () {
  // Use jQuery to select the <header> element and toggle between classes red and green
  $('DIV#toggle_header').on('click', function () {
    const headerClass = $('header');
    // toggle between the classes
    if (headerClass.hasClass('red')) {
      headerClass.removeClass('red').addClass('green');
    } else {
      headerClass.removeClass('green').addClass('red');
    }
  });
});
