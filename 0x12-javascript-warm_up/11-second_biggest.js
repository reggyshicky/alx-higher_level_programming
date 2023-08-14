#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first 2 arguments
function findSecondBiggest (numbers) {
  if (numbers.length <= 1) {
    return 0;
  }
  numbers = numbers.map(Number); // convert string args tonumbers
  numbers.sort((a, b) => b - a); // sort the nos in desc order
  return numbers[1]; // return the 2nd biggest element
}
console.log(findSecondBiggest(args));
