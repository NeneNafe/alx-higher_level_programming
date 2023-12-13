#!/usr/bin/node
/**
 * converts a number form base 10 to another base
 */

exports.converter = function (base) {
  const convert = function (number) {
    if (number === 0) {
      return '';
    } else {
      const remainder = number % base;
      const quotient = Math.floor(number / base);
      return convert(quotient) + remainder;
    }
  };

  return function (number) {
    return convert(number);
  };
};
