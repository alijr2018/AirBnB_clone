#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                from models.base_model import BaseModel
                for key, value in data.items():
                    cls_name, obj_id = key.split(".")
                    cls = BaseModel if cls_name == "BaseModel" else None
                    if cls:
                        obj = cls(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
