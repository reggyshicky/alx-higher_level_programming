#!/usr/bin/node
const file = process.argv[2];
const string = process.argv[3];
const fs = require('fs');

fs.writeFile(file, string, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
