#!/usr/bin/node

const { argv } = require('process');
const intvalue = parseInt(argv[2]);

if (isNaN(intvalue) === false) {
  console.log('My number: ' + intvalue);
} else {
  console.log('Not a number');
}
