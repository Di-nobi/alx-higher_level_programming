#!/usr/bin/python3
"""Module 3-is_kind_of_class
True if the object is an instance of, or
if the object is an instance of a class that
inherited from otherwise false
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the conditions of
    the method are met else False"""

    return isinstance(obj, a_class)
