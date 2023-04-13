#!/usr/bin/node
const filepath = require('filepath');
const first = filepath.readFileSync(process.argv[2], 'utf8');
const second = filepath.readFileSync(process.argv[3], 'utf8');
filepath.writeFileSync(process.argv[4], first + second);
