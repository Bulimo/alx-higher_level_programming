#!/usr/bin/python3
"""
Module 8-json_api
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    data = {"q": ""}
    if len(argv) >= 2:
        data['q'] = argv[1]

    res = requests.get('http://0.0.0.0:5000/search_user', data=data)

    # Check if the response contains valid JSON and is not empty
    try:
        json = res.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
