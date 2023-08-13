#!/usr/bin/python3
"""
Module:test_base_model.py
"""
import json
import os
import time
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    """TestBase:"""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization_positive(self):
        x = BaseModel()
        b2_uuid = str(uuid.uuid4())
        y = BaseModel(id=b2_uuid, name="The weeknd", album="Trilogy")
        self.assertIsInstance(x.id, str)
        self.assertIsInstance(y.id, str)
        self.assertEqual(b2_uuid, y.id)
        self.assertEqual(y.album, "Trilogy")
        self.assertEqual(y.name, "The weeknd")
        self.assertIsInstance(x.created_at, datetime)
        self.assertIsInstance(x.created_at, datetime)
        self.assertEqual(str(type(x)), "<class 'models.base_model.BaseModel'>")

    def test_dict(self):
        x = BaseModel()
        b2_uuid = str(uuid.uuid4())
        y = BaseModel(id=b2_uuid, name="The weeknd", album="Trilogy")
        x_dict = x.to_dict()
        self.assertIsInstance(x_dict, dict)
        self.assertIn('id', x_dict.keys())
        self.assertIn('created_at', x_dict.keys())
        self.assertIn('updated_at', x_dict.keys())
        self.assertEqual(x_dict['__class__'], type(x).__name__)
        with self.assertRaises(KeyError) as e:
            y.to_dict()

    def test_save(self):
        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_save_storage(self):
        b = BaseModel()
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        file_path = FileStorage._FileStorage__file_path
        self.assertTrue(os.path.isfile(file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_save_no_args(self):
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        message = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), message)

    def test_save_excess_args(self):
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        message = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), message)

    def test_str(self):
        x = BaseModel()
        string = f"[{type(x).__name__}] ({x.id}) {x.__dict__}"
        self.assertEqual(x.__str__(), string)


if __name__ == "__main__":
    unittest.main()
