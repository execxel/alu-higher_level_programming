#!/usr/bin/python3
"""Defines a string-to-JSON conversion function."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object."""
    return json.dumps(my_obj)
