#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances.
"""
import json
from datetime import datetime


class FileStorage:
    """The file storage engine class, that is;
    A class that serialize and deserialize instances to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Sets new obj in __objects dictionary."""
        return (self.__objects)

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                loaded_objs = json.load(file)
                for key, value in loaded_objs.items():
                    class_name = value['__class__']
                    del value['__class__']
                    x = '%Y-%m-%dT%H:%M:%S.%f'
                    y = value['updated_at']
                    z = value['created_at']
                    value['created_at'] = datetime.strptime(z, x)
                    value['updated_at'] = datetime.strptime(y, x)
                    new_obj = globals()[class_name](**value)
                    self.__objects[key] = new_obj
        except FileNotFoundError:
            pass
