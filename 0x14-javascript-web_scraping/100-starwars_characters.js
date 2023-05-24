#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const num = process.argv[2];

request.get(url + num, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body).characters;

  for (const i of data) {
     request.get(i, function (err, response, body2) {
       if (err) console.log(err);
       const nxt_data = JSON.parse(body2);
	     console.log(nxt_data.name);
     });
  }
});
