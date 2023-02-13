#!/usr/bin/python3
"""Module base.
Defines a Base class for other classes in the project.
"""
import json
import os
import csv
class Base:
    """Class with:
    Private class attribute: __nb_objects
    """
    __nb_objects = 0
    def __init__(self, id=None):
         """Initialization of a Base instance.
        Args:
            - id: id of the instance
        """
        if id is not None and not isinstance(id, int):
            raise TypeError("Must be an integer")
        return self.id = id
    else:
       Base. __nb_objects += 1
       self.id = Base.__nb_objects
