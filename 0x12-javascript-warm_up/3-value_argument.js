#!/usr/bin/node
if (process.argv.lenght < 3) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
