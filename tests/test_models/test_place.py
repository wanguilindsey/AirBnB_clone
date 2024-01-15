#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlaceInstantiation
    TestPlaceAttributes
    TestPlaceBaseModel
"""
from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def setUp(self):
        """Instantiate Place test objects."""
        self.place = Place()

    def test_place_instantiation(self):
        """Test that Place class correctly instantiates."""
        self.assertIsInstance(self.place, Place)


class TestPlaceAttributes(unittest.TestCase):
    """Unittests for testing attributes of the Place class."""

    def setUp(self):
        """Instantiate Place test objects."""
        self.place = Place()

    def test_place_attributes_existence_and_type(self):
        """Test that all public class attributes are included
        & in correct types."""
        attributes = {
            'city_id': str,
            'user_id': str,
            'name': str,
            'description': str,
            'number_rooms': int,
            'number_bathrooms': int,
            'max_guest': int,
            'price_by_night': int,
            'latitude': float,
            'longitude': float,
            'amenity_ids': list
        }

        for attribute, data_type in attributes.items():
            with self.subTest(attribute=attribute):
                self.assertTrue(hasattr(self.place, attribute))
                self.assertTrue(isinstance(getattr
                                (self.place, attribute, None), data_type))


class TestPlaceBaseModel(unittest.TestCase):
    """Unittests for testing inheritance from BaseModel."""

    def setUp(self):
        """Instantiate Place test objects."""
        self.place = Place()

    def test_place_isinstance_of_BaseModel(self):
        """Test that Place class inherits from BaseModel."""
        self.assertIsInstance(self.place, BaseModel)


if __name__ == "__main__":
    unittest.main()
