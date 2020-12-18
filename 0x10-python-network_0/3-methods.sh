#!/bin/bash
# that takes in a URL and displays all HTTP methods the server will accept.
curl localhost:5000/route_4 -siX HEAD | grep "Allow:" | cut -c8-
