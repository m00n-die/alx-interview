#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const endPoint = 'https://swapi-api.hbtn.io/api/films/' + movieID;
let characters = [];
const names = [];

const getCharacters = async () => {
  await new Promise(resolve => request(endPoint, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Error: ', error, '| StatusCode: ', response.statusCode);
    } else {
      const result = JSON.parse(body);
      characters = result.characters;
      resolve();
    }
  }));
};

const getNames = async () => {
  if (characters.length > 0) {
    for (const character of characters) {
      await new Promise(resolve => request(character, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          console.error('Error: ', error, '| StatusCode: ', response.statusCode);
        } else {
          const result = JSON.parse(body);
          names.push(result.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: No Characters Found');
  }
};

const getTheirNames = async () => {
  await getCharacters();
  await getNames();

  for (const name of names) {
    if (name === names[names.length - 1]) {
      process.stdout.write(name);
    } else {
      process.stdout.write(name + '\n');
    }
  }
};

getTheirNames();
