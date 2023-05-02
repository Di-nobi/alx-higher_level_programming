#!/usr/bin/python3
""" A python script that takews 2 argument"""

import requests
import sys
if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2], sys.argv[1])

    req = requests.get(url)
    try:
        if req >= 400:
            print("Not found")

        else:
            commit = req.json()

            for i in range (10):
                print("{}: {}".format(commit[i].get("sha"), commit[i].get("author").get("name")))
    except IndexError:
        pass
