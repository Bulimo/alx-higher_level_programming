#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const actors = JSON.parse(body).characters;
    // iterate over films
    for (const actor of actors) {
      request(actor, function (err, resp, character) {
        if (!err && resp.statusCode === 200) {
          const name = JSON.parse(character).name;
          console.log(name);
        }
      });
    }
  } else {
    console.error('Error:', error || `HTTP Status Code: ${response.statusCode}`);
  }
});
