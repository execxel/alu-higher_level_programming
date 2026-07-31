#!/usr/bin/python3
"""
Module: 3-to_json_string
Description: Return JSON string representation of a Python object.
"""

import json


def to_json_string(my_obj):
    """Return the JSON representation (string) of `my_obj`.

    Args:
        my_obj: Object serializable by the JSON module.
    """
    return json.dumps(my_obj)
