#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let hi = 0; hi < this.height; hi++) {
      let rec = '';
      for (let wi = 0; wi < this.width; wi++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }
}

module.exports = Rectangle;
