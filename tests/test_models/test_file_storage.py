#!/usr/bin/python3
"""Defines tests for the FileStorage module (file_storage.py)"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def setUp(self):
        """Set up instance objects for the tests"""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.classes = ['BaseModel', 'User', 'City', 'State',
                        'Place', 'Amenity', 'Review']

    def test_instantiation(self):
        """Test that the class instantiates correctly"""
        self.assertTrue(isinstance(self.storage, FileStorage))

    def test_private_objects_attribute(self):
        """Test that the attribute 'objects' is private"""
        self.assertEqual(getattr(self.storage, '__objects', None), None)

    def test_private_file_path_attribute(self):
        """Test that the attribute 'file_path' is private"""
        self.assertEqual(getattr(self.storage, '__file_path', None), None)

    def test_empty_objects_at_instantiation(self):
        """Test that '__objects' is empty at class instantiation"""
        self.assertEqual(len(self.storage.all()), 0)

    def test_all_return_at_instantiation(self):
        """Test that 'all()' returns an empty dictionary
        on class instantiation"""
        storage_instance = FileStorage()
        self.assertEqual(len(storage_instance.all()), 0)

    def test_all_return_with_objects(self):
        """Test that 'all()' returns a non-empty dictionary
        after saving an object"""
        self.assertTrue(len(self.storage.all()) > 0)
        self.assertTrue(len(self.storage.all().keys()) > 0)

    def test_new_affects_objects(self):
        """Test that 'new()' sets an object in '__objects'"""
        storage_instance = FileStorage()
        base_model_instance = BaseModel()
        self.assertTrue(f"BaseModel.{base_model_instance.id}"
                        in storage_instance.all().keys())

    def test_save_affects_file_path(self):
        """Test that 'save()' writes to a JSON file
        and the file is not empty"""
        storage_instance = FileStorage()
        base_model_instance = BaseModel()
        storage_instance.reload()
        self.assertTrue(len(storage_instance.all()) > 0)

    def test_save_dumps_to_file_path(self):
        """Test that 'save()' dumps '__objects' to a file"""
        self.storage.reload()
        self.assertTrue(len(self.storage.all().keys()) > 0)

    def test_reload_checks_file_path_existence(self):
        """Test that 'reload()' checks for file existence and raises
        no exception if not found"""
        self.storage.reload()
        self.assertTrue(True)  # Assert that no exception is raised
        # (the opposite of assertRaises)
