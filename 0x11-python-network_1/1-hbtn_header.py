#!/usr/bin/python3
""" A python script that takes iin a URL, sends a request to the
URL and displays the value of the X-Request-Id variable """
import sys
import urllib.request
if __name__ == "__main__":

    url = sys.argv[1]
    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as f:
        print(dict(f.headers).get("X-Request_Id"))
