#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    const pattern = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(pattern);
    }
  }
}

module.exports = Rectangle;
