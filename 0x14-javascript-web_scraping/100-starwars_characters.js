#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
num = process.argv[2];

request(url + num, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
      for (let i = 0; i < JSON.parse(body).characters.length; i++) {
	request(JSON.parse(body).characters[i], function (body2, response2) {
          console.log(JSON.parse(body2).name);
	});
      }
  }
});
