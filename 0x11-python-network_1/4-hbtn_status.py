#!/usr/bin/python3
"""
Python script that fetches `https://alx-intranet.hbtn.io/status`
"""
import requests


if __name__ == '__main__':

    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    data = response.text
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
