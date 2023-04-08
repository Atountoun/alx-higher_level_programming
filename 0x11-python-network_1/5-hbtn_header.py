#!/usr/bin/python3
"""
Python script that takes a URL, sends a request to that URL and
displays the value of the `X-Request-Id` variable.
"""
import requests
import sys


url = sys.argv[1]
response = requests.get(url)

print(response.headers.get('X-Request-Id'))
