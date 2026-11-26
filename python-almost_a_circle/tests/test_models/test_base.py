#!/usr/bin/python3
"""Defines unit tests for models/base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def setUp(self):
        """Resets __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleans up generated JSON files after tests."""
        for fname in ["Rectangle.json", "Square.json", "Base.json"]:
            if os.path.exists(fname):
                os.remove(fname)

    def test_auto_id(self):
        """Test automatic sequential ID assignment."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """Test explicit integer ID assignment."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_mixed_ids(self):
        """Test alternating auto and explicit IDs."""
        b1 = Base()
        b2 = Base(98)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 98)
        self.assertEqual(b3.id, 2)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """Test to_json_string with a valid list of dictionaries."""
        res = Base.to_json_string([{"id": 12}])
        self.assertEqual(res, '[{"id": 12}]')
        self.assertIsInstance(res, str)

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        res = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(res, [{"id": 89}])
        self.assertIsInstance(res, list)

    def test_save_to_file_none(self):
        """Test save_to_file with None writes empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test save_to_file with empty list writes empty list."""
        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_and_load_rectangle(self):
        """Test saving and loading Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))
        self.assertIsNot(loaded[0], r1)

    def test_save_and_load_square(self):
        """Test saving and loading Square instances."""
        s1 = Square(5, 1, 2, 10)
        Square.save_to_file([s1])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(str(loaded[0]), str(s1))

    def test_load_from_missing_file(self):
        """Test load_from_file returns empty list when file does not exist."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_create_rectangle(self):
        """Test Rectangle.create with dictionary kwargs."""
        r = Rectangle.create(id=89, width=3, height=5, x=1, y=2)
        self.assertEqual(str(r), "[Rectangle] (89) 1/2 - 3/5")

    def test_create_square(self):
        """Test Square.create with dictionary kwargs."""
        s = Square.create(id=42, size=7, x=2, y=3)
        self.assertEqual(str(s), "[Square] (42) 2/3 - 7")


if __name__ == "__main__":
    unittest.main()
