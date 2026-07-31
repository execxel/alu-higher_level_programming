#!/usr/bin/python3
"""Square class that inherits from Rectangle."""


class BaseGeometry:
    """A geometry base class."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name: The name of the variable (string).
            value: The value to validate (should be int).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height.

        Args:
            width: The width of the rectangle (must be positive integer).
            height: The height of the rectangle (must be positive integer).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
