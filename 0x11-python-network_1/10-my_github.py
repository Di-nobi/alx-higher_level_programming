#!/usr/bin/python3

"""A python script that takes your Github credentials and uses
GIthub API to display your id"""

from requests.auth import HTTPBasicAuth
import requests
import sys

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
