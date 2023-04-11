#!/usr/bin/node
//	A script that prints a message
const find = process.argv.length;
console.log(find === 2 ? 'No argument' : find === 3 ? 'Argument found' : 'Arguments found');
