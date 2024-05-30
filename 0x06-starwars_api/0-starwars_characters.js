#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode !== 200) {
    console.log(`Error: ${res.statusCode}`);
    return;
  }

  const characters = body.characters;
  characters.forEach(characterUrl => {
    request(characterUrl, { json: true }, (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }

      if (res.statusCode !== 200) {
        console.log(`Error: ${res.statusCode}`);
        return;
      }

      console.log(body.name);
    });
  });
});
