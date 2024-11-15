#!/usr/bin/node
const axios = require('axios');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// URL of the Star Wars API for the specified movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

async function fetchMovieCharacters () {
  try {
    // Fetch movie details
    const response = await axios.get(apiUrl);
    const data = response.data;

    // Fetch and log the names of the characters
    const characterPromises = data.characters.map(async (url) => {
      try {
        const charResponse = await axios.get(url);
        return charResponse.data.name;
      } catch (charError) {
        console.error('Error fetching character:', charError.message);
      }
    });

    const characterNames = await Promise.all(characterPromises);
    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error('Error fetching movie details:', error.message);
  }
}

fetchMovieCharacters();
