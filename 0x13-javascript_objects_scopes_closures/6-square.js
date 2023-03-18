#!/usr/bin/node
const Square1 = require('./5-square.js');
class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let hi = 0; hi < this.height; hi++) {
      let rectangle = '';
      for (let wi = 0; wi < this.width; wi++) {
        rectangle += c;
      }
      console.log(rectangle);
    }
  }
}

module.exports = Square;
