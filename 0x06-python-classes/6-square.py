#!/usr/bin/python3
"""Modulue"""
class Square:
    """defines a square"""
    def __init__(self, size=0, position(0, 0)):
         """Create a Square
        Args:
            size: length of a side of Square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position
    def __str__(self):
        self.my_print()
@property
    def size(self):
        """"The propery of size as the len of a side of Square
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        return self.__size
@property.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise TypeError('size must be >= 0')
        self.__size = value
@property
    def position(self):
        return self.__position 
@property.setter
    def position(self, value):
        if not len(isinstance(value, tuple)) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
    def area(self):
        return self.__size * self.__size
    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
