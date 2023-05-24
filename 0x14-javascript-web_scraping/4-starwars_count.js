#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).movies;
    let num = 0;
     for (const movie of movies) {
       for (const move of movie.characters) {
	 if (move.endswith('/18/')) {
	   num++;
	 }
       }
     }
	  console.log(num);
  });

