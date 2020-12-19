#!/bin/bash
# sends a JSON POST request, and displays the body of the response
curl -s --request POST $1 --header "Content-Type: application/json" --data @$2
