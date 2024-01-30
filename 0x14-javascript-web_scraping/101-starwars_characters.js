#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const APIUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;
let characters = [];

request(APIUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  characters = data.characters;
  getChars(0);
});

const getChars = (index) => {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const charData = JSON.parse(body);
    console.log(charData.name);
    getChars(index + 1);
  });
};
