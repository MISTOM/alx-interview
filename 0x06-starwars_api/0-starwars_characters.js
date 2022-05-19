#!/usr/bin/node
const request = require('request')

const movie_id = process.argv[2]
const BASE_SWAPI = 'https://swapi-api.hbtn.io/api/'

console.log(movie_id)
if (movie_id === undefined){
    console.error('Pass in a movie ID (number)\n\t ./0-starwars_characters.js 3')
    process.exit(1)
}

/**
 * Prints all characters' names in the characters enpoints
 * @param {array} characters array of characters enpoints
 */

