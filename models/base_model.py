#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs.pop('__class__', None)
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            cr_str = kwargs['created_at']
            up_str = kwargs['updated_at']
            kwargs['created_at'] = datetime.strptime(cr_str, date_format)
            kwargs['updated_at'] = datetime.strptime(up_str, date_format)
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return (data)
