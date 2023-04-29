#!/usr/bin/python3
""" Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000"""

import requests
import sys
if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    res = requests.post('http://0.0.0.0:5000', data={'q': letter})
    try:
        respond = res.json()
        if respond == {}:
            print("No result")
        else:
            print("[{}] {}".format(respond.get("id"), respond.get("name")))
    except ValueError:
        print("Not a valid JSON")
