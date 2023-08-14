#!/usr/bin/node

const { argv } = require('process');
const x = argv[2];
if (isNaN(x) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
