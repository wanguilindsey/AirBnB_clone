#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenityInstantiation
    TestAmenitySave
    TestAmenityToDict
"""
import os
import models
import unittest
from datetime import datetime, timedelta
from time import sleep
from models.amenity import Amenity


class TestAmenityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        amenity_instance = Amenity()
        self.assertIsInstance(amenity_instance, Amenity)

    def test_new_instance_stored_in_objects(self):
        amenity_instance = Amenity()
        self.assertIn(amenity_instance, models.storage.all().values())

    def test_attributes(self):
        amenity_instance = Amenity()
        self.assertTrue(hasattr(amenity_instance, 'id'))
        self.assertIsInstance(amenity_instance.id, str)
        self.assertTrue(hasattr(amenity_instance, 'created_at'))
        self.assertIsInstance(amenity_instance.created_at, datetime)
        self.assertTrue(hasattr(amenity_instance, 'updated_at'))
        self.assertIsInstance(amenity_instance.updated_at, datetime)

    def test_unique_ids(self):
        amenity_instance1 = Amenity()
        amenity_instance2 = Amenity()
        self.assertNotEqual(amenity_instance1.id, amenity_instance2.id)

    def test_different_timestamps(self):
        amenity_instance1 = Amenity()
        sleep(0.05)
        amenity_instance2 = Amenity()
        self.assertLess(amenity_instance1.created_at,
                        amenity_instance2.created_at)
        self.assertLess(amenity_instance1.updated_at,
                        amenity_instance2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        amenity_instance = Amenity()
        amenity_instance.id = "123456"
        amenity_instance.created_at = dt
        amenity_instance.updated_at = dt
        amenity_str = amenity_instance.__str__()

        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'created_at': {!r}".format(dt.isoformat()), amenity_str)
        self.assertIn("'updated_at': {!r}".format(dt.isoformat()), amenity_str)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amenity_instance = Amenity(
                id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity_instance.id, "345")
        self.assertEqual(amenity_instance.created_at, dt)
        self.assertEqual(amenity_instance.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenitySave(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_save_updates_timestamp(self):
        amenity_instance = Amenity()
        sleep(0.05)
        first_updated_at = amenity_instance.updated_at
        amenity_instance.save()
        self.assertLess(first_updated_at, amenity_instance.updated_at)

    def test_save_updates_file(self):
        amenity_instance = Amenity()
        amenity_instance.save()
        amenity_id = "Amenity." + amenity_instance.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())

    def test_save_with_arg(self):
        amenity_instance = Amenity()
        with self.assertRaises(TypeError):
            amenity_instance.save(None)


class TestAmenityToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        amenity_instance = Amenity()
        self.assertIsInstance(amenity_instance.to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        amenity_instance = Amenity()
        amenity_dict = amenity_instance.to_dict()
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("__class__", amenity_dict)

    def test_to_dict_contains_added_attributes(self):
        amenity_instance = Amenity()
        amenity_instance.middle_name = "Holberton"
        amenity_instance.my_number = 98
        self.assertEqual("Holberton", amenity_instance.middle_name)
        self.assertIn("my_number", amenity_instance.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amenity_instance = Amenity()
        amenity_dict = amenity_instance.to_dict()
        self.assertEqual(str, type(amenity_dict["id"]))
        self.assertEqual(str, type(amenity_dict["created_at"]))
        self.assertEqual(str, type(amenity_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        amenity_instance = Amenity()
        amenity_instance.id = "123456"
        amenity_instance.created_at = dt
        amenity_instance.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(amenity_instance.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        amenity_instance = Amenity()
        self.assertNotEqual(amenity_instance.to_dict(),
                            amenity_instance.__dict__)

    def test_to_dict_with_arg(self):
        amenity_instance = Amenity()
        with self.assertRaises(TypeError):
            amenity_instance.to_dict(None)


if __name__ == "__main__":
    unittest.main()
