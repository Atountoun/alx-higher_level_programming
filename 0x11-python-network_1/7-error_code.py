#!/usr/bin/python3
"""
Python script that takes a URL and sends a request to that URL.
Displays the body of the response(utf-8). Manages errors.
"""
import requests
import sys


url = sys.argv[1]

response = requests.get(url)

if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
