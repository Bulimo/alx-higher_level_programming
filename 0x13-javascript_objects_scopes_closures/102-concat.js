#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of arguments are provided
if (process.argv.length >= 5) {
  const fileA = process.argv[2];
  const fileB = process.argv[3];
  const fileC = process.argv[4];

  const data1 = fs.readFileSync(fileA, 'utf8');
  const data2 = fs.readFileSync(fileB, 'utf8');

  fs.writeFileSync(fileC, data1 + data2);
}
