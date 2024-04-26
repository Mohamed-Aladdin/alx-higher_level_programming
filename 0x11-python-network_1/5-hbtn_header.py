#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers.get('X-Request-Id'))
