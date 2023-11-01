/* global $ */

$(document).ready(function () {
  // Make an AJAX request to fetch the list of movies
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Extract movie titles from the response data
    const movies = data.results;

    // Select the UL#list_movies element
    const $listMovies = $('UL#list_movies');

    // Loop through the movies and add each title to the list
    $.each(movies, function (index, movie) {
      $listMovies.append('<li>' + movie.title + '</li>');
    });
  });
});
