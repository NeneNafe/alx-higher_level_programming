#!/usr/bin/node
/**
 * imports an array and computes a new array
 */

const { list } = require('./100-data');

const newList = list.map((value, ind) => value * ind);
console.log(list);
console.log(newList);
