#!/usr/bin/python3
"""
Module 6-post_email
script that takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter, and finally displays
the body of the response.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    vals = {"email": argv[2]}
    url = argv[1]
    res = requests.post(url, data=vals)
    print(res.text)
