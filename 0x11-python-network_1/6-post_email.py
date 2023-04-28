#!/usr/bin/python3
"""
A python script that sends a POST to an email address
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    respond = requests.POST(url, data={'email': sys.argv[2]})
    print(respond.text)
