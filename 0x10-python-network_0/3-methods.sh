#!/bin/bash
# This script takes in a URL and displays all HTTP methods allowed
curl -sI "$1" | grep -i '^Allow:' | awk -v FS=': ' '{print $2}'
