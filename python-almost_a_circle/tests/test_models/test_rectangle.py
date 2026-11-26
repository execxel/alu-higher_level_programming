#!/usr/bin/python3
"""Defines unit tests for models/rectangle.py."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def setUp(self):
        """Resets __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_basic_instantiation(self):
        """Test Rectangle creation with required and optional arguments."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

    def test_invalid_types(self):
        """Test TypeError raised for non-integer attributes."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {}, 0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, [1])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.5, 2)

    def test_invalid_values(self):
        """Test ValueError raised for out-of-range attributes."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Test area computation."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        """Test __str__ formatting."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        """Test display output with x and y offsets."""
        r = Rectangle(2, 3, 2, 1)
        expected = "\n  ##\n  ##\n  ##\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_update_args(self):
        """Test update method with positional *args."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update method with keyword **kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(y=1, width=2, x=3, id=89, height=4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/4")

    def test_update_args_skips_kwargs(self):
        """Test that *args takes priority and skips **kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(50, width=99)
        self.assertEqual(r.id, 50)
        self.assertEqual(r.width, 10)

    def test_to_dictionary(self):
        """Test to_dictionary returns expected dict keys and values."""
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
