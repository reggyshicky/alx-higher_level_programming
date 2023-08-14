#!/usr/bin/node

const { argv } = require('process');
const intval = parseInt(argv[2]);
function factorial (n) {
  if (isNaN(n)) {
    return 1; // factorial of NaN is 1
  } else if (n === 0 || n === 1) {
    return 1; // Base case: factorial of 0 and 1 is 1
  } else {
    return n * factorial(n - 1); // recursive case
  }
}
console.log(factorial(intval));
