#!/usr/bin/python3
""" A python script that takes in a URL and an email,
sends a POST reuest to the passed URL and email as paramitere
"""
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data_1 = urllib.parse.urlencode(values)
    data_1 = data_1.encode('ascii')
    req = urllib.request.Request(url, data_1)
    with urllib.request.urlopen(req) as feedback:
        out_page = feedback.read().decode('utf-8')
        print(out_page)
