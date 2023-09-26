#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const apiurl = 'https://swapi-api.alx-tools.com/api/films/';

request(apiurl + episode, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responsejsobj = JSON.parse(body);
    console.log(responsejsobj.title);
  } else {
    console.log('code: ' + response.StatusCode);
  }
});
