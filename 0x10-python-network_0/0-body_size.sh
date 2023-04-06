#!/bin/bash
# This script displays the body size of the request
curl -sI "$1" | awk -v FS=': ' 'tolower($1) ~ /content-length/{print $2}'
