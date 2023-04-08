#!/usr/bin/python3
"""
Python scripts that takes a URL and an email, sends a `POST` request
to that URL with the email as a parameter.
Displays the body of the response (decode in `utf-8`)
"""
import requests
import sys


if __name__ == '__main__':

    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    response = requests.post(url, json=data)

    print(response.text)
