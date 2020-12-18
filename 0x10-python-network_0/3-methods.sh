#!/bin/bash
# that takes in a URL and displays all HTTP methods the server will accept.
curl $1 --silent --include --request OPTIONS | grep "Allow:" | cut -c8-
