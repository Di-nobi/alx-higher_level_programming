#!/usr/bin/python3
def uppercase(str):
    if str >= ord(97) and str < ord(123):
        str -= 32
        print("{:c}".format(str), end=" ")
