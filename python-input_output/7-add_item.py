#!/usr/bin/python3
"""
Script: 7-add_item
Description: Add all command-line arguments to a Python list and save them in
`add_item.json` using the JSON helpers from this package.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = 'add_item.json'
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []

    args = sys.argv[1:]
    for a in args:
        items.append(a)

    save_to_json_file(items, filename)
