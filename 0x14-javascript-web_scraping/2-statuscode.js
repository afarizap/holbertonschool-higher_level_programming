#!/usr/bin/node
const request = require('request');

request
  .get(process.argv[2])
  .on('res', res => console.log('code: ' + response.statusCode));
