#!/bin/bash
: '
This script takes in a URL, sends a request to the URL and
displays the size of the body of the response.
'
curl -sI "$1" | awk -v FS=': ' 'tolower($1) ~ /content-length/{print $2}'
