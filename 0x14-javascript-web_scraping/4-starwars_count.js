#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0; // keeps track of the no of chars
    for (const eachfilm in films) {
      const eachfilmchars = films[eachfilm].characters;
      for (const eachchar in eachfilmchars) {
        if (eachfilmchars[eachchar].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Status code: ' + response.statusCode);
  }
});
