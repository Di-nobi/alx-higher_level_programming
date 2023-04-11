#!/usr/bin/node

const num = Number(process.argv[2]);
if (num === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
