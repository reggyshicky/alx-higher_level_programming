#!/usr/bin/node

const { argv } = require('process');
const intval = parseInt(argv[2]);
if (isNaN(intval) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < intval; i++) {
    let row = '';
    for (let j = 0; j < intval; j++) {
      row += 'X';
    }
    console.log(row); // prints the row containig 'X' characters
  }
}
