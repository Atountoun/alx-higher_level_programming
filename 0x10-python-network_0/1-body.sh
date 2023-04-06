#!/bin/bash
# This script takes in a URL, sends a GET request to it, and
# displays the body of the response.
# Display only body of a 200 status code response

response=$(curl -s -w "%{http_code}" "$1")
status_code=$(echo "${response: -3}")

if [ "$status_code" == "200" ]
then
	body=$(echo "${response::-3}")
	echo "$body"
fi
