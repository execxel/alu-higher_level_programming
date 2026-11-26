#!/usr/bin/python3
"""Add all command-line arguments to a Python list and save to a file."""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, "add_item.json")
