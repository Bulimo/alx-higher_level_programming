/* global $ */

$(document).ready(function () {
  // Select the DIV#add_item element
  $('DIV#add_item').on('click', function () {
    // Add the item <li>Item</li>
    $('UL.my_list').append('<li>Item</li>');
  });

  // Select the DIV#remove_item element
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });

  // Select the DIV#clear_lis element
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
