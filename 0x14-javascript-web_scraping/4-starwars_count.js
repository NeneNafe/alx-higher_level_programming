#!/usr/bin/node

const request = require('request');
const APIUrl = process.argv[2];
const CharID = 18;
let count = 0;

request.get(APIUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(CharID)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
