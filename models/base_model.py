#!/usr/bin/python3
"""
Write a class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    x = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key, datetime.strptime(value, x))
                elif key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        class_name = self.__class__.__name__
        instance_id = self.id
        instance_dict = self.__dict__
        return ("[{}] ({}) {}".format(class_name, instance_id, instance_dict))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
