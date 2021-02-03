#!/usr/bin/node
let x = Number(process.argv[2]);
const y = x;
if (x) {
  while (x > 0) {
    console.log('X'.repeat(y));
    x--;
  }
} else {
  console.log('Missing size');
}
