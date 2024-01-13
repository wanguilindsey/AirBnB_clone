#!/usr/bin/python3
"""Defines tests for the BaseModel module <base_model.py>."""
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModelClass(unittest.TestCase):
    """Defines a class with BaseModel test cases."""
    def setUp(self):
        """Set up BaseModel object(s) to use in tests."""
        self.base = BaseModel()

    def test_class_instantiation(self):
        """Test class instantiation."""
        base1 = BaseModel()
        self.assertEqual(type(base1), type(self.base))

    def test_attributes_assignment_on_instantiation(self):
        """Test class instantiation assigns id, created, and
        updated_at attributes."""
        attrs = ['created_at', 'updated_at', 'id']
        for attr in attrs:
            self.assertTrue(attr in self.base.__dict__)

    def test_object_id_unique(self):
        """Test class objects have unique ids."""
        base1 = BaseModel()
        self.assertFalse(base1.id == self.base.id)

    def test_object_id_is_str(self):
        """Test that object id is converted to string."""
        self.assertTrue(type(self.base.id) is str)

    def test_creation_and_update_time_different_at_creation(self):
        """Test that object creation and update time are not the same at
        creation."""
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_save(self):
        """Test that the save instance method updates updated_at."""
        base1 = BaseModel()
        old_time = base1.updated_at
        base1.save()
        self.assertNotEqual(old_time, base1.updated_at)

    def test_str_method(self):
        """Test class' str method."""
        self.assertTrue(len(str(self.base)) > 100)

    def test_to_dict(self):
        """Test that the to_dict instance method returns a dictionary."""
        self.assertTrue(type(self.base.to_dict()) is dict)

    def test_to_dict_datetime_is_str(self):
        """Test that the to_dict instance method converts datetime
        objects to strings."""
        cls_dict = self.base.to_dict()
        self.assertTrue('datetime' not in cls_dict.values() and
                        type(cls_dict['created_at']) is str)

    def test_to_dict_class_key(self):
        """Test that the to_dict instance method adds the __class__
        key to its return dict."""
        cls_dict = self.base.to_dict()
        self.assertTrue('__class__' in cls_dict.keys())

    def test_to_dict_class_key_value(self):
        """Test that the to_dict __class__ key's value is the class_name."""
        cls_dict = self.base.to_dict()
        self.assertEqual(cls_dict['__class__'], 'BaseModel')


class TestBaseModelRecreation(unittest.TestCase):
    """Defines tests for the BaseModel recreation."""
    def setUp(self):
        """Initialize a class to use in tests."""
        self.base = BaseModel()
        self.base.name = 'Test_Model'
        self.base.number = 7
        obj_dict = self.base.to_dict()
        self.new_base = BaseModel(**obj_dict)

    def test_object_recreation_kwargs_check(self):
        """Test that kwargs are checked for before initializing new objects."""
        attrs = {'name': 'Test'}
        base1 = BaseModel(**attrs)
        self.assertTrue('name' in (base1.__dict__).keys())

    def test_object_recreation_datetime_conversion(self):
        """Test that datetime strings are converted back to
        datetime objects."""
        self.assertTrue(isinstance(self.new_base.created_at, datetime))

    def test_object_recreation_no_kwargs(self):
        """Test that if **kwargs isn't defined, normal
        initialization occurs."""
        self.assertTrue(self.base)

    def test_object_recreation_args_not_used(self):
        """Test that if **kwargs isn't defined, normal initialization occurs,
        args aren't used."""
        args = ['Test_Model', 'hello']
        base1 = BaseModel(*args)
        for arg in args:
            self.assertEqual(getattr(self, arg, None), None)

    def test_object_recreation_args__class__handled(self):
        """Test that if **kwargs is defined, the __class__ key/value
        is not added as an attribute."""
        self.assertTrue(getattr(self.new_base, '__class__', None))
