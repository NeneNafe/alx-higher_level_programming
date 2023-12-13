#!/usr/bin/node
/**
 * returns args already printes and new arg value
 */

let counter = 0;

exports.logMe = function count (item) {
  console.log(`${counter}: ${item}`);
  counter++;
};
