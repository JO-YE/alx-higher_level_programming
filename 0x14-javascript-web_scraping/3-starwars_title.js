#!/usr/bin/node
// display the status of a GET request

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, function (err, response, data) {
  if (err) {
    console.log(err);
  } else {
    const title = JSON.parse(data);
    console.log(`${title.title}`);
  }
});
