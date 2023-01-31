#!/usr/bin/python3
import sys

class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
    @property
    def size(self):
        return(self.__size)
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
    def area(self):
        return (self.__size ** 2)
    def my_print(self):
        for i in range(self.__size):
            print('#' * self.__size)
