#!/usr/bin/python3
"""
Module: 4-from_json_string
Description: Return Python object represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """Return the Python object represented by JSON string `my_str`.

    Args:
        my_str (str): JSON string.
    """
    return json.loads(my_str)
