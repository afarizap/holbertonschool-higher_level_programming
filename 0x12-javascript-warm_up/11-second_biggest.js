#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const n = process.argv.slice(2).sort(function (a, b) { return b - a; });
  console.log(n[1]);
}
