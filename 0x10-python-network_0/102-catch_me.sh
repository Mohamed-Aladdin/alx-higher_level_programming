#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
