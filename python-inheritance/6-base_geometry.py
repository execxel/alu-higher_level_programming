#!/usr/bin/python3
"""BaseGeometry class with area method."""


class BaseGeometry:
    """A geometry base class."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
