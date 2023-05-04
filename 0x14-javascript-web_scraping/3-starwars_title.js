#!/usr/bin/node
// display the status of a GET request

const request = require('request');
const url = "https://swapi-api.alx-tools.com/api/films/:id" + id;

request(url, function (err, response, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(data).title);
  }
});
