#!/usr/bin/python3
"""
Module: 8-class_to_json
Description: Return a dictionary representation of a class instance suitable
for JSON serialization.
"""


def class_to_json(obj):
    """Return the `__dict__` of `obj` as a dictionary.

    This function does not import modules and assumes attributes are
    JSON-serializable (lists, dicts, strings, ints, booleans).
    """
    return obj.__dict__.copy()
