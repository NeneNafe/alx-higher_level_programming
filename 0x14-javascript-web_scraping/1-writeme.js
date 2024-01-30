#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];

fs.readFile(filename, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  }
});
