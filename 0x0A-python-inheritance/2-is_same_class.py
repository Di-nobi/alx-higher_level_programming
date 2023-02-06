#!/usr/bin/python3
"""Module 2-is_same_class
True if the object is an instance of the class"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance
    of the class a_class"""

    return True if type(obj) is a_class else False
