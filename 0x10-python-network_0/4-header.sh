#!/bin/bash
: '
This script takes in a URL as an argument, sends a GET request
to it and displays the body of the response.
'
response=$(curl -s -I "$1" -H "X-School-User-Id: 98")

status=$(echo "${response: -3}")
body=$(echo "${response::-3}")

echo "$body"
