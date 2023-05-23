#!/usr/bin/node

const req = require('req');
const url = 'https://swapi-api.hbtn.io/api/films/';
const epi = process.argv[2];

req.get(url + epi, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
