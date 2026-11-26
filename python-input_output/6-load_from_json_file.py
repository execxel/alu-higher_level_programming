#!/usr/bin/python3
"""
Module: 6-load_from_json_file
Description: Load a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """Load and return the Python object from JSON file `filename`.

    Args:
        filename (str): Path to input JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
