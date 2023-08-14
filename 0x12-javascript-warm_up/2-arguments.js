#!/usr/bin/node

const { argv } = require('process');
// require function is used to import the built-in process module in node.js
// argv property is destructures from the imported process mod and assigned to a const variable named argv
// The curly braces in argv are part of destructuring assigment syntax in js
if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
