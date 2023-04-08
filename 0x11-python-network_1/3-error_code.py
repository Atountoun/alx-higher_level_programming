#!/usr/bin/python3
"""
Python script that takes a URL and sends a request to that URL.
Displays the body of the response(utf-8). Manages errors.
"""
import urllib.request
import urllib.error
import sys


if __name__ == '__main__':

    url = sys.argv[1]

    with urllib.request.urlopen(url) as req:
        try:
            print(req.read().decode('utf-8'))
        except urllib.error.HTTPError as err:
            print(f"Error code: {err.code}")
