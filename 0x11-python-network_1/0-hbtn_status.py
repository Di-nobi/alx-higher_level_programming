#!/usr/bin/python3
""" A python script thatfetches alx url"""
import urllib.request

if __name__ == "__main__":

    r = urllib.request.Request('https://alx-intranet.hbtn.io/status')

    with urllib.request.urlopen(r) as response:
        page_out = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(page_out)))
        print("\t- content: {}".format(page_out))
        print("\t- utf8 content: {}".format(page_out.decode('utf-8')))
