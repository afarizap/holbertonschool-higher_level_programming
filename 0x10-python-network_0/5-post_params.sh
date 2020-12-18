#!/bin/bash
# takes in a URL, sends a POST request, and displays the body of the response
curl $1 --silent --request POST --data "email=hr@holbertonschool.com&subject=I will always be here for PLD"
