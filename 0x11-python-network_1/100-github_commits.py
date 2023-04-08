#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
- First argument with be the `repository name`
- Second argument will be the `owner name`
"""
import requests
import sys


if __name__ == "__main__":

    repo = sys.argv[1]
    owner = sys.argv[2]

    response = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits")
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    else:
        print(None)
