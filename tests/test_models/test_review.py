#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReviewInstantiation
    TestReviewAttributes
    TestReviewBaseModel
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review
from models.base_model import BaseModel


class TestReviewInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def setUp(self):
        """Instantiate Review test objects."""
        self.review = Review()

    def test_review_instantiation(self):
        """Test that Review class correctly instantiates."""
        self.assertIsInstance(self.review, Review)


class TestReviewAttributes(unittest.TestCase):
    """Unittests for testing attributes of the Review class."""

    def setUp(self):
        """Instantiate Review test objects."""
        self.review = Review()

    def test_review_attributes_existence_and_type(self):
        """Test that all public class attributes are
        included & in correct types."""
        attributes = {
            'place_id': str,
            'user_id': str,
            'text': str
        }

        for attribute, data_type in attributes.items():
            with self.subTest(attribute=attribute):
                self.assertTrue(hasattr(self.review, attribute))
                attribute_value = getattr(self.review, attribute, None)
                self.assertTrue(isinstance(attribute_value, data_type))


class TestReviewBaseModel(unittest.TestCase):
    """Unittests for testing inheritance from BaseModel."""

    def setUp(self):
        """Instantiate Review test objects."""
        self.review = Review()

    def test_review_isinstance_of_BaseModel(self):
        """Test that Review class inherits from BaseModel."""
        self.assertIsInstance(self.review, BaseModel)


if __name__ == "__main__":
    unittest.main()
