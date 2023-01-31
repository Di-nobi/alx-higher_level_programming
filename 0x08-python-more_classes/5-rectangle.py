#!/usr/bin/python3
"""5-rectangle Module
Defines a rectangle with
an input height and width
"""


class Rectangle:
    """Rectangle class defined by width and height"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle class instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            """Returns a typeerror if NaN"""
            raise TypeError("width must be an integer")
        elif value < 0:
            """Returns a valueerror if value is less than 0"""
            raise ValueError("width must be >= 0")
        else:
            """Sets the width value"""
            self.__width = value

    @property
    def height(self):
        """Returns the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            """returns a typeerror if value is NaN"""
            raise TypeError("height must be an integer")
        elif value < 0:
            """returns a valueerror if value is less than 0"""
            raise ValueError("height must be >= 0")
        else:
            """sets the height value"""
            self.__height = value


    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            """returns 0 if either width or height is 0"""
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """returns 0 if either value is 0"""
        if self.__height == 0 or self.__width == 0:
            return ''
        """Returns a string representation of a rectangle"""
        return '\n'.join('#' * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Returns a string representation of a Rectangle instance
        that is able to recreate a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle instance"""
        print("Bye rectangle...")
