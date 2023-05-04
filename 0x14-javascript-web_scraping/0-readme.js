#!/usr/bin/node
// A script that reads and prints the content of a file

// using the keyword require
const fs = require('fs'); // how to import in javascript

const filePath = process.argv[2];

fs.readFile(filePath, { encoding: 'utf-8' }, (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
