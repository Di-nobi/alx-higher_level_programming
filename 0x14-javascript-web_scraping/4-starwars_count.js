#!/usr/bin/node
const req = require('req');
req.get(process.argv[3], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).movies;
    let num = 0;
     const film;

