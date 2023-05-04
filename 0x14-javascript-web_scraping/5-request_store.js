#!/usr/bin/node
// A script that writes a string to a file

// using the keyword require to import
const fs = require('fs'); // to write
const request = require('request'); // to query

const url = process.argv[2];
const filePath = process.argv[3];

request(url, 'utf-8', (err, res, body) => {
  if (err) {
    console.log(err);
    return; // using 'return' instead of 'else'
  }

  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
