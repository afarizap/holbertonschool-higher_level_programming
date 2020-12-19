#!/bin/bash
# sends a request to a URL, and displays only the status code of the response
curl --silent --include --output /dev/null --write-out "%{http_code}" $1
