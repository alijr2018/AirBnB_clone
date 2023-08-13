#!/usr/bin/python3
"""Defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime



class BaseModel:
    """  that defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance."""
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
            from models import storage
            storage.new(self) 

    def __str__(self):
        """Returns a readable string representation
        of BaseModel instance"""
        class_name = self.__class__.__name__
        instance_id = self.id
        instance_dict = self.__dict__
        return ("[{}] ({}) {}".format(class_name, instance_id, instance_dict))

    def save(self):
        """updates the public instance attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance."""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return (new_dict)
