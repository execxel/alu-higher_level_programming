#!/usr/bin/python3
"""This module defines the Square class inheriting from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square shape with size, x, y, and id."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the width and height of the Square to value."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Updates attributes of the Square via positional or keyword args."""
        attrs = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
