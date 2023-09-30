#!/bin/bash
# Send a JSON POST request to the URL and display the response body
curl -s -X POST --json "@$2" "$1"
