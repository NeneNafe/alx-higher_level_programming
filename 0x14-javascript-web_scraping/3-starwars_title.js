#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const APIUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(APIUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
