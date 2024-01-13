#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects obj with key <obj_class_name>.id."""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path."""
        obj_dict = {key: obj.to_dict() for key, obj in
                    FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file __file_path to __objects,
        if the JSON file exists."""
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_cls = FileStorage.__objects.get(class_name)
                    if obj_cls:
                        self.new(obj_cls(**value))
        except FileNotFoundError:
            return
