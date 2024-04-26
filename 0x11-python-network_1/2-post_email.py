#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.parse as parse
import urllib.request as request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    content = parse.urlencode({"email": email}).encode("ascii")
    data = request.Request(url, data)
    with request.urlopen(data) as result:
        print(result.read().decode("utf-8"))
