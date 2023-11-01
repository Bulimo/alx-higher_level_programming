/* global $ */

$(document).ready(function () {
  // Use jQuery to select the <header> element and add item in the list
  $('DIV#add_item').on('click', function () {
    // Add the item <li>Item</li>
    $('UL.my_list').append('<li>Item</li>');
  });
});
