#!/usr/bin/python3
"""Python script that:
- takes in a URL,
- sends a request to the URL
- displays the body"""
import sys
from urllib import request, error
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as res:
            response = res.read().decode("ascii"))
            print(response)
    except error.HTTPError as e:
        print('Error code:' e.code)
