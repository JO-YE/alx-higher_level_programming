#!/usr/bin/node
let mul = Number(process.argv[2]);
if (isNaN(mul)) {
  console.log('Missing number of occurrences');
} else {
//  for (let i = 0; i < mul; i++)
  while (mul > 0) {
    console.log('C is fun');
    mul--;
  }
}
