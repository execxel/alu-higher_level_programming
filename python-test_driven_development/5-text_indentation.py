#!/usr/bin/python3
"""This module provides a function that formats text with blank lines."""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' and ':' character."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length and text[i] == " ":
        i += 1

    while i < length:
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1
