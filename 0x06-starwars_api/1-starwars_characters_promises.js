#!/usr/bin/node
// Prints all characters of a Star Wars movie using the ALX Star Wars API

if (process.argv.length !== 3) {
  process.exit();
}
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
const request = require('request');

// Upgrade request module from callbacks to promises
const util = require('node:util');
const req = util.promisify(request);

// Asynchronous function to get and print character names for a movie
async function printStarWarsCharacters (url) {
  try {
    // Get list of URLs for characters in current film
    const characters = JSON.parse((await req(url)).body).characters;
    if (!characters) {
      process.exit();
    }

    // Loop through list of URLs, fetch character name from each and print it
    while (characters.length) {
      const name = JSON.parse((await req(characters.shift())).body).name;
      console.log(name);
    }
  } catch (error) {
    // Ignore internet connection error, but output all other errors
    if (error.code !== 'ENOTFOUND' && error.name !== 'SyntaxError') {
      console.error(error);
    }
  }
}

printStarWarsCharacters(url);
