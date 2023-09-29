#!/usr/bin/python3
"""
Module 0-hbtn_status
Script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print('Body response:')
        print('\t- type: {}'.format(type(the_page)))
        print('\t- content: {}'.format(the_page))
        print('\t- utf8 content: {}'.format(the_page))
