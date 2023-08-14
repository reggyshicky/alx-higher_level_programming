#!/usr/bin/node

const { argv } = require('process');
let a = parseInt(argv[2]);
let b = parseInt(argv[3]);
function add(a, b) {
  console.log(a + b);
}
add(a, b);
