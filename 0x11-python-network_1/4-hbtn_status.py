#!/usr/bin/python3
""" Python script that fetches 
https://alx-intranet.hbtn.io/status
"""
import requests
if __name__ == "__main__":

    display = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(display.text.__class__))
    print("\t- content: {}".format(display.text))
