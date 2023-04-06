#!/bin/bash
# This script sends a DELETE request to the URL passed as the first
# argument and displays the body of the response.

response=$(curl -s -w "%{http_code}" -X DELETE "$1")

status=$(echo "${response: -3}")
response_body=$(echo "{$response::-3}")

echo "$response_body"
