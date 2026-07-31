#!/usr/bin/python3
"""
Module: 0-read_file
Description: Provide a function that reads a UTF-8 text file and prints it.
"""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to stdout.

    Args:
        filename (str): Path to the file to read.

    Prints the file content (no extra newlines added).
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
