#!/usr/bin/node
let find = 0;
exports.logMe = function (item) {
  console.log(`${find++}: ${item}`);
};
