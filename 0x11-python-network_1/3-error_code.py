#!/usr/bin/python3
"""
Module 3-error_code
script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
Also manages urllib.error.HTTPError exceptions
"""
if __name__ == "__main__":
    import urllib.error
    import urllib.request
    from sys import argv

    try:
        url = argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
