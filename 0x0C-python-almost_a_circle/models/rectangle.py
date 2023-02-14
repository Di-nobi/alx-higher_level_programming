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
    def update(self, *args, **kwargs):
        """Updates attributes of an instance.
        Args:
            - id attribute
            - width attribute
            - height attribute
            - x attribute
            - y attribute
        """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
