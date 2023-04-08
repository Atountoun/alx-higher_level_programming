#!/usr/bin/python3
"""
Python scripts that takes a URL and an email, sends a `POST` request
to that URL with the email as a parameter.
Displays the body of the response (decode in `utf-8`)
"""
import urllib.request
import urllib.parse
import sys


url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({"email": email})

req = urllib.request.Request(url, data=data, method="POST")

with urllib.request.urlopen(url) as post:
    res = post.read()
    print(res.decode('utf-8'))
