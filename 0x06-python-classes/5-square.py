#!/usr/bin/python3
# 5-square by Dinobi 
"""A module that defines a square """
class Square:
    """A class that represents a square"""
    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
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
