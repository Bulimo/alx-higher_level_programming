#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

// Get the contents of the url
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    // Write the file in UTF-8 encoding
    fs.writeFile(filename, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.error('Error:', error || `HTTP Status Code: ${response.statusCode}`);
  }
});
