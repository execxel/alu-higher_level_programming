#!/usr/bin/python3
"""
Module: 9-student
Description: Student class with to_json method returning a dict representation.
"""


class Student:
    """Define a student by first_name, last_name and age.

    Public instance attributes: first_name, last_name, age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student instance."""
        return self.__dict__.copy()
