#!/usr/bin/python3
"""
Python script that takes Github creadentials (username and password)
and uses Github API to display the account id.
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]

    basic = HTTPBasicAuth(username, password)

    response = requests.get(f'https://api.github.com/users/{username}', auth=basic)

    print(response.json().get('id'))
