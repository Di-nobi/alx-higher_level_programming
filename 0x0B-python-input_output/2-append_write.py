#!/usr/bin/python3
""" Module that contains a function that appends from a file """
def append_write(filename="", text=""):
    """ Function that reads from a file
    Args:
        filename: filename
    Raises
        Exception: when the file can be opened
    """
    with open(filename, 'a', encoding="utf-8") as f:
        append_file = f.write(text)
        return append_file
