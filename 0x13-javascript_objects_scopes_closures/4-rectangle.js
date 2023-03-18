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

  rotate () {
    const exchange = this.width;
    this.width = this.height;
    this.height = exchange;
  }

  double () {
    this.width = this.width * 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
