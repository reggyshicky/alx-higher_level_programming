#!/usr/bin/node

function add (a, b) {
  return a + b;
}
// module .exports line is crucial for exporting the add function
module.exports = {
  add
};
