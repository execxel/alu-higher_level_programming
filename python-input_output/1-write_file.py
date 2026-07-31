#!/usr/bin/python3
"""
Module: 1-write_file
Description: Write a string to a UTF-8 text file and return the number of
characters written.
"""


def write_file(filename="", text=""):
    """Write `text` to `filename` (UTF-8) and return number of chars written.

    If the file does not exist it is created. Existing content is overwritten.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
