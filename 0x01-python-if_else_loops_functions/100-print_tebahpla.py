#!/usr/bin/python3
for i in range (97, 123, -1):
    if i % 2 == 0:
        i = i - 32
        print("{:c}".format(i), end="")
    else:
        print("{}".format(i), end="")
