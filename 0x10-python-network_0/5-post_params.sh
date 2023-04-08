#!/bin/bash
# This script takes in a URL, sends a POST request to the passed URL arg
curl -s -X POST "$1" --data-urlencode "email=test%40gmail.com"  --data-urlencode "subject=I will always be there for PLD"
