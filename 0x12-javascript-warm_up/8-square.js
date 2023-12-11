#!/usr/bin/node

const sizeSquare = parseInt(process.argv[2]);

if (!isNaN(sizeSquare)) {
  for (let i = 0; i < sizeSquare; i++) {
    let row = '';
    for (let j = 0; j < sizeSquare; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
