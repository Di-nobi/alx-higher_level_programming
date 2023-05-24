#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const tasks = JSON.parse(body);
  const done = {};
  for (const i in tasks) {
     task = tasks[i];
     if (task.done === true && done[task.userId] === undefined) {
       done[task.userId] = 1;
     } else {
       done[task.userId]++;
     }
  }
   console.log(done);
});

