/* global $ */

$(document).ready(function () {
  // Make an AJAX request to fetch character data
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Extract the character name from the response data
    const person = data.name;

    // Display the character name in DIV#character
    $('DIV#character').text(person);
  });
});
