#!/usr/bin/node
// print title of a Star Wars movies

const request = require('request');
const actor = 'https://swapi-api.alx-tools.com/api/people/18/';
const url = process.argv[2];

// => can also be used instead of the function keyword just like in task 0 & 1
request(url, function (err, response, data) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(data).results;
    const match = films.filter((film) => file.characters.includes(actor));
    console.log(`${match.length}`);
  }
});
