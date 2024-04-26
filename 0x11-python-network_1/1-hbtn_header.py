#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request as request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as result:
        info = result.info()
        print(info.get("X-Request-Id"))
