#!/bin/bash
# Script that sends a JSON POST request. The data is contained in a file.
curl -s -X POST "$1" --json @"$2"
