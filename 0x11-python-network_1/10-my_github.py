#!/usr/bin/python3
"""
Module 0-my_github
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'

    # Set up Basic Authentication using your username and PAT
    auth = (username, password)

    res = requests.get(url, auth=auth)
    data = res.json()
    print(data.get('id'))
