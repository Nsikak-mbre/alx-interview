#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// URL of the Star Wars API for the specified movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchMovieCharacters () {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie details:', error.message);
      return;
    }

    const data = JSON.parse(body);
    const characterUrls = data.characters;

    // Iterate through the character URLs and fetch their names
    characterUrls.forEach((url) => {
      request(url, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character:', charError.message);
          return;
        }

        if (charResponse.statusCode !== 200) {
          console.error(`Failed to fetch character. Status code: ${charResponse.statusCode}`);
          return;
        }

        const character = JSON.parse(charBody);
        console.log(character.name);
      });
    });
  });
}

fetchMovieCharacters();
