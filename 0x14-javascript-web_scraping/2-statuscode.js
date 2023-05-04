#!/usr/bin/node
// display the status of a GET request

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, data)
  {
    if (err) {
      console.log(err);
    }
    else {
      console.log(`code: ${response.statusCode}`);
    }
  });
