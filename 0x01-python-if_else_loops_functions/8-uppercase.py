#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord(97) and ord(i) < ord(123):
            char = ord(i) - 32
            print("{:c}".format(char), end=" ")