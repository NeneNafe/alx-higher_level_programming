#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const APIUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(APIUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
