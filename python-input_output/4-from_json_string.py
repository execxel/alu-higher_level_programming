#!/usr/bin/python3
"""Defines a JSON-to-object conversion function."""
import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string."""
    return json.loads(my_str)
