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
     if (task[i].done && done[tasks[i].userId] === undefined) {
       done[tasks[i].userId] = 1;
     } else if (tasks[i].done) {
       done[tasks[i].userId] += 1;
     }
  }
   console.log(done);
});

