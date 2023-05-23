#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request.get(process.argv[2], function (err, response, body) {
   if (err) {
     console.log(err);
   }
   fs.writeFileSync(process.argv[3], body, 'utf-8', (err) => {
     if (err) {
       console.log(err);
     }
   });
});
