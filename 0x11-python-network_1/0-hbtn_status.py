#!/usr/bin/python3
"""
Python script that fetches `https://alx-intranet.hbtn.io/status`
"""
import urllib.request


if __name__ == '__main__':

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as status:
        data = status.read()
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
        decoded = data.decode('utf-8')
        print(f"\t- utf-8 content: {decoded}")
