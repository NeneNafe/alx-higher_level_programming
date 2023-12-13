#!/usr/bin/node
const Intlist = require('./100-data.js').list;
console.log(Intlist);
const newList = Intlist.map((val, indx) => val * indx);
console.log(newList);
