#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

from urllib import request, parse, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)
