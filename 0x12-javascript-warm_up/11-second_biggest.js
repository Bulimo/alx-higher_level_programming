#!/usr/bin/node
// const args = process.argv;
// const len = process.argv.length;
// let largest;
// let secondLargest = 0;
// if (len > 3) {
//   largest = args[2];
//   for (let i = 2; i < args.length; i++) {
//     if (args[i] > largest) {
//       secondLargest = largest;
//       largest = args[i];
//     } else {
//       if (args[i] > secondLargest && args[i] !== largest) {
//         secondLargest = args[i];
//       }
//     }
//   }
// }
// console.log(secondLargest);

// Get the arguments excluding the first one (which is the script name)
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0); // No arguments or 1 argument passed, print 0
} else {
  // Convert the arguments to integers and sort them in descending order
  const integers = args.map(Number).sort((a, b) => b - a);

  // Find the second biggest integer (at index 1 after sorting)
  console.log(integers[1]);
}
