#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if not int(size):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
    @property
    def size(self):
        return self.__size = size

    def size(self, value):
        if not int(value):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
    def area(self):
        return self.__size ** 2
