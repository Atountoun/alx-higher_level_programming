#!/usr/bin/python3
"""
Python script that takes in a letter and sends a `POST` request
to `http://0.0.0.0:5000/search_user` with the letter as a param.
"""
import requests
import sys


if __name__ == '__main__':

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    data = {"q": q}
    response = requests.post(url, data=data)

    try:
        to_json = response.json()
        if not to_json:
            print("No result")
        else:
            print(f"[{to_json.get('id')}] {to_json.get('name')}")
    except ValueError:
        print("Not a valid JSON")
