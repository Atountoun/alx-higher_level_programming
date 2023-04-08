#!/bin/bash
# Script that sends a request to the server and diplays the server response
curl -s -o /dev/null --header "Referer: http://0.0.0.0:50000/catch_me" "http:0:0:0:0:5000/catch_me" -d "user_id=12" -L
