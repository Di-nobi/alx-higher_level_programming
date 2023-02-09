#!/usr/bin/python3
""" Modulue """
def inherits_from(obj, a_class):
    """Determines if obj is an instance of a class that
    inherited from a_class.
    Args:
        - obj: object to look at
        - a_class: class to evaluate
    Returns: True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
