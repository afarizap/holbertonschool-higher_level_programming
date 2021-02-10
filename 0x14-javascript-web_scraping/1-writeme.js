#!/usr/bin/node
const fs = require('fs')

try {
  const data = fs.writeFileSync(process.argv[2], process.argv[3])
} catch (err) {
  console.error(err)
}