#!/bin/bash
: '
This script takes in a URL, sends a POST request to the passed
URL, and displays the body of the response.
'
response=$(
	curl -s -X POST "$1" -d '{"email": "test@gmail.com", "subject": "I will always be there for PLD"}'
)

status=$(echo "${response: -3}")
body=$(echo "${response::-3}")

echo "$body"
