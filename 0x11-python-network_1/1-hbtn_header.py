#!/usr/bin/python3
"""
Python script that takes a URL, sends a request to that URL and
displays the value of the `X-Request-Id` variable.
"""
import urllib.request
import sys


if __name__ == '__main__':

    url = sys.argv[1]
    with urllib.request.urlopen(url) as req:
        print(req.headers.get('X-Request-Id'))
