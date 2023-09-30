#!/bin/bash
# Send a JSON POST request to the URL and display the response body
curl -s -X POST -H "Content-Type: application/json" --data "@$2" "$1"
