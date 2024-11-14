#!/usr/bin/node
// Prints all characters of a Star Wars movie using the ALX Star Wars API

if (process.argv.length !== 3) {
  process.exit();
}
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
const request = require('request');

// Recursive function to get and print character names from a list of URLs
function printNextCharacter (urls) {
  // Remove first URL from list and parse it
  const characterURL = urls.shift();
  if (characterURL) {
    request(characterURL, function (error, response, body) {
      if (!error) {
        // Parse and print the character name from the response body
        console.log(JSON.parse(body).name);
        // Move to next character in the list
        printNextCharacter(urls);
      }
    });
  }
}

// Fetches a list of character's URLs then uses a callback to print each one's name
function printStarWarsCharacters (url) {
  // Get list of URLs for characters in selected film
  request(url, function (error, response, body) {
    if (!error) {
      // Call recursive function to fetch and print character names from URLs list
      printNextCharacter(JSON.parse(body).characters);
    }
  });
}

printStarWarsCharacters(url);
