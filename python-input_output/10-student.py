#!/usr/bin/python3
"""
Module: 10-student
Description: Student class with to_json method supporting optional attribute
filtering.
"""


class Student:
    """Student with public attributes: first_name, last_name, age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict representation; filter keys if `attrs` is a list.

        If `attrs` is not a list of strings, return all attributes.
        """
        obj_dict = self.__dict__.copy()
        if isinstance(attrs, list):
            filtered = {}
            for k in attrs:
                if k in obj_dict and isinstance(k, str):
                    filtered[k] = obj_dict[k]
            return filtered
        return obj_dict
