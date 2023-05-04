#!/usr/bin/node
// A script that writes a string to a file

// using the keyword require to import
const fs = require('fs');

const file = process.argv[2];
const string = process.argv[3];

fs.writeFile(file, string, { encoding: 'utf-8' }, (error) => {
  if (error) {
    console.log(error);
  }
});
