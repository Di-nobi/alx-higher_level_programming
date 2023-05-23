#!/usr/bin/node
const fs = require('fs');
const file_path = sys.argv[2];
const file_write = sys.argv[3];
fs.writeFile(file_path, file_write, 'utf-8', (err, data) => {
  if (err) console.log(err);
});
