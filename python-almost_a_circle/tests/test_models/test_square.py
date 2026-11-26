#!/usr/bin/python3
"""Defines unit tests for models/square.py."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for the Square class."""

    def setUp(self):
        """Resets __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_basic_instantiation(self):
        """Test Square creation and inherited attributes."""
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_size_setter_and_validation(self):
        """Test size getter/setter and Rectangle validation inheritance."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -3

    def test_invalid_constructor_args(self):
        """Test Square constructor validation for size, x, and y."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "1")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 1, "2")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 1, -2)

    def test_area(self):
        """Test Square area calculation."""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_str(self):
        """Test Square __str__ formatting."""
        s = Square(3, 1, 3, 7)
        self.assertEqual(str(s), "[Square] (7) 1/3 - 3")

    def test_display(self):
        """Test Square display output."""
        s = Square(2, 1, 1)
        expected = "\n ##\n ##\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_update_args(self):
        """Test Square update with positional *args."""
        s = Square(5, 0, 0, 1)
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")

    def test_update_kwargs(self):
        """Test Square update with keyword **kwargs."""
        s = Square(5, 0, 0, 1)
        s.update(size=7, id=89, y=1, x=2)
        self.assertEqual(str(s), "[Square] (89) 2/1 - 7")

    def test_to_dictionary(self):
        """Test Square to_dictionary returns expected dict keys and values."""
        s = Square(10, 2, 1, 4)
        expected = {"id": 4, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
