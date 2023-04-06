#!/bin/bash
# This script displays the body of 200 status code response body
response=$(curl -w '%{http_code}' -s --output /dev/null "$1") && [[ $response -eq 200 ]] && curl -s "$1"
