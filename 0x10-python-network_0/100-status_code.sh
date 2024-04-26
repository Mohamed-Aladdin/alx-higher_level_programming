#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -L -o /dev/null -s -w "%{http_code}" "$1"
