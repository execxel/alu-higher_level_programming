#!/usr/bin/python3
"""
Module: 11-student
Description: Student class with to_json and reload_from_json methods.
"""


class Student:
    """Student with public attributes: first_name, last_name, age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dict representation of the instance."""
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace attributes of the instance using `json` dict.

        Args:
            json (dict): Dictionary with attribute names and values.
        """
        if not isinstance(json, dict):
            return
        for k, v in json.items():
            setattr(self, k, v)
