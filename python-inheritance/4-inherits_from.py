#!/usr/bin/python3
"""Function that checks if object inherits from specified class."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class (direct or indirect), else False."""
    return isinstance(obj, a_class) and type(obj) is not a_class
