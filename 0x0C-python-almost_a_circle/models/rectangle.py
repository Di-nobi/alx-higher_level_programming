#!/usr/bin/python3

""" Module rectangle.
Create a Rectangle class, inheriting from Base. """
from models.Base import Base
import json
import csv
class Rectangle:
    """ Class that inherits
    from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
         """Initializes a Rectangle instance.
        Args:
            - __width: width
            - __height: height
            - __x: position
            - __y: position
            - id: id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        """Retrieves the width attribute."""
        return self.__width
    @property
    def height(self):
        """Retrieves the height attribute."""
        return self.__height
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise TypeError('width must be >= 0')
        self.__width = value
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
           raise TypeError('height must be an integer')
       if value <= 0:
           raise ValueError('height must be >= 0')
       self.__height = value
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
           raise TypeError('x must be an integer')
       if value <= 0:
           raise ValueError('x must be >= 0')
       self.__x = value
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
           raise TypeError('y must be an integer')
       if value <= 0:
           raise ValueError('y must be >= 0')
       self.__y = value
    def area(self):
        return __width * __height
    def __str__(self):
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
        return s
    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
