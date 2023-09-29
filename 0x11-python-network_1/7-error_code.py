#!/usr/bin/python3
"""
Module 7-error_code
script that takes in a URL, sends a request to the URL
and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: HTTP status code
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    res = requests.get(url)

    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
