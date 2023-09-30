#!/bin/bash
# Make a request to the server that triggers a response with "You got me!"
curl -s -L -X PUT -d "name=peter" "http://0.0.0.0:5000/catch_me"
