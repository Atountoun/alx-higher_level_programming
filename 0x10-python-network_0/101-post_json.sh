#!/bin/bash
# Script that sends a JSON POST request. The data is contained in a file.
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
