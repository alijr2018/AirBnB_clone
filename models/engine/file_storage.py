#!/usr/bin/python3
"""
Module: file_storage.py
"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

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
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (FileStorage.__objects)

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        try:
            f = open(self.__file_path, 'w')
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)
        finally:
            if f:
                f.close()

    def reload(self):
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
