#!/usr/bin/node
const request = require('request');

// Function to make the request and return a promise
function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error || `HTTP Status Code: ${response.statusCode}`);
      }
    });
  });
}

// Main function to fetch and print character names
async function PrintCharacters (id) {
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  try {
    const filmResponse = await makeRequest(url);
    const filmData = JSON.parse(filmResponse);
    for (const characterUrl of filmData.characters) {
      try {
        const charResponse = await makeRequest(characterUrl);
        const characterData = JSON.parse(charResponse);
        console.log(characterData.name);
      } catch (charError) {
        console.error('Error fetching character:', charError);
      }
    }
  } catch (error) {
    console.error('Error:', error);
  }
}
const id = process.argv[2];
PrintCharacters(id);
