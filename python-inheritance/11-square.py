#!/usr/bin/python3
"""Square class that inherits from Rectangle."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with size.

        Args:
            size: The size of the square (must be positive integer).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def __repr__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
