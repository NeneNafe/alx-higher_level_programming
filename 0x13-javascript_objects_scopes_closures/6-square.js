#!/usr/bin/node
/**
 * define a square that inherits from a rectangle
 */

const LastSquare = require('./5-square');

class Square extends LastSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
