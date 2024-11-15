#!/usr/bin/node
const request = require('request');

// Helper function to make HTTP requests and return a Promise
function fetch (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch data from ${url}. Status code: ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Main function to fetch and print all characters of a Star Wars movie
async function fetchMovieCharacters () {
  const movieId = process.argv[2]; // Movie ID passed as a command-line argument

  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  try {
    // Fetch movie details
    const movieData = await fetch(apiUrl);

    // Fetch and log each character's name in order
    for (const characterUrl of movieData.characters) {
      try {
        const characterData = await fetch(characterUrl);
        console.log(characterData.name);
      } catch (characterError) {
        console.error(`Error fetching character data: ${characterError.message}`);
      }
    }
  } catch (error) {
    console.error(`Error fetching movie data: ${error.message}`);
  }
}

// Execute the function
fetchMovieCharacters();
