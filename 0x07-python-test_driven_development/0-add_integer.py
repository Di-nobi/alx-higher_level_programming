#!/usr/bin/python3
"""Module add_integer
adds two integers
"""


def add_integer(a, b=98):
    """Raises a typeerror if values aren't
    ints or floats
    """
    if not isinstance(a, int) and not isinstance(b, float):
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
