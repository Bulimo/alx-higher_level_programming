#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s "$1" -o /dev/null -w "%{http_code}\n" | ([ "$(cat)" == "200" ] && curl -s "$1")
