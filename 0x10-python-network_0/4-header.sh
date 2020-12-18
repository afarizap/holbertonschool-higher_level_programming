#!/bin/bash
# takes a URL, sends GET request, and displays the body of the response
curl $1 --silent --request GET --header 'X-HolbertonSchool-User-Id: 98'
