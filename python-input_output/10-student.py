#!/usr/bin/python3
"""Defines a class Student with attribute filtering."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student."""
        if type(attrs) is list:
            all_strings = True
            for item in attrs:
                if type(item) is not str:
                    all_strings = False
                    break

            if all_strings:
                result = {}
                for attr in attrs:
                    if hasattr(self, attr):
                        result[attr] = getattr(self, attr)
                return result

        return self.__dict__
