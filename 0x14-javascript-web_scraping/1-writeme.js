#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];

// Write the file in UTF-8 encoding
fs.writeFile(filename, content, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
