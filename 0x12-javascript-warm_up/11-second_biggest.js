#!/usr/bin/node
const args = process.argv;
const len = process.argv.length;
let largest;
let secondLargest = 0;
if (len > 3) {
  largest = args[2];
  for (let i = 2; i < args.length; i++) {
    if (args[i] > largest) {
      secondLargest = largest;
      largest = args[i];
    } else {
      if (args[i] > secondLargest && args[i] !== largest) {
        secondLargest = args[i];
      }
    }
  }
}
console.log(secondLargest);
