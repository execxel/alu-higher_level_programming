#!/usr/bin/python3
"""
Module: 2-append_write
Description: Append a string to a UTF-8 text file and return number of added
characters.
"""


def append_write(filename="", text=""):
    """Append `text` to `filename` (UTF-8) and return number of chars added.

    If the file doesn't exist it is created.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
