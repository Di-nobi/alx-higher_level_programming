#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:54] + str[54:66] + str[106:112] + str[:-123]
print(str)