#!/usr/bin/python3
"""
Module: 3-is_kind_of_class
Description: Function that checks if object is an instance of, or a
subclass of, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of, or inherits from, a_class."""
    return isinstance(obj, a_class)
