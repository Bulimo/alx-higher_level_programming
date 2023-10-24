#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    // iterate over films
    for (const film in films) {
      const actor = films[film].characters;
      for (const c in actor) {
        if (actor[c].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.error('Error:', error || `HTTP Status Code: ${response.statusCode}`);
  }
});
