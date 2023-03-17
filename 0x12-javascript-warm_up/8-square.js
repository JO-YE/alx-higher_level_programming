#!/usr/bin/node
let size = Number(process.argv[2]);
let height = size;
if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (height > 0) {
  let square = 'X'.repeat(size);
  console.log(square);
  height--;
    }
}
