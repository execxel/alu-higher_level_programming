#!/usr/bin/python3
"""
Module: 4-inherits_from
Description: Function that checks if object inherits from the
specified class.
"""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class (direct or indirect).

    Returns False if obj is exactly an instance of `a_class`.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
