#!/usr/bin/python3
"""
Module: file_storage.py
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

valid_classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Amenity': Amenity,
    'City': City,
    'State': State,
    'Place': Place,
    'Review': Review
}


class FileStorage():
    """
    class FileStorage that serializes instances to a JSON file,
    and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)."""
        try:
            f = open(self.__file_path, 'w')
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)
        finally:
            if f:
                f.close()

    def reload(self):
        """
        deserializes the JSON file to __objects,
        (only if the JSON file (__file_path).
        """
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None
            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass
            if deserialized is None:
                return
            FileStorage.__objects = {
                k: valid_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
