#!/usr/bin/node
// display the status of a GET request

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, function (err, response, data) {
  if (err) {
    console.log(err);
  } else {
    const actors = JSON.parse(data).characters;
    // forEach is used to loop through, it is a built-in fxn
    actors.forEach((actor) => {
    // each actor now rep. url endpoint
      request(actor, (err, res, data) => {
        if (err) {
          console.log(err);
          return;
        }
        console.log(JSON.parse(data).name);
      });
    });
  }
});
