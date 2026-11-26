#!/usr/bin/python3
"""
Module: 5-save_to_json_file
Description: Save an object to a file as its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """Serialize `my_obj` to JSON and write to `filename` using UTF-8.

    Args:
        my_obj: JSON-serializable Python object.
        filename (str): Path to output file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
