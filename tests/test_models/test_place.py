#!/usr/bin/python3
"""test for place.py"""

import os
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self) -> None:
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):

        y = Place()
        p3 = Place("hello", "wait", "in")
        k = f"{type(y).__name__}.{y.id}"
        self.assertIsInstance(y.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(p3.name, "")

        self.assertIsInstance(y.name, str)
        self.assertIsInstance(y.user_id, str)
        self.assertIsInstance(y.city_id, str)
        self.assertIsInstance(y.description, str)
        self.assertIsInstance(y.number_bathrooms, int)
        self.assertIsInstance(y.number_rooms, int)
        self.assertIsInstance(y.price_by_night, int)
        self.assertIsInstance(y.max_guest, int)
        self.assertIsInstance(y.longitude, float)
        self.assertIsInstance(y.latitude, float)
        self.assertIsInstance(y.amenity_ids, list)

    def test_init(self):

        y = Place()
        x = Place(**y.to_dict())
        self.assertIsInstance(y.id, str)
        self.assertIsInstance(y.created_at, datetime)
        self.assertIsInstance(y.updated_at, datetime)
        self.assertEqual(y.updated_at, x.updated_at)

    def test_str(self):
        y = Place()
        string = f"[{type(y).__name__}] ({y.id}) {y.__dict__}"
        self.assertEqual(y.__str__(), string)

    def test_save(self):
        y = Place()
        old_update = y.updated_at
        y.save()
        self.assertNotEqual(y.updated_at, old_update)

    def test_todict(self):
        y = Place()
        x = Place(**y.to_dict())
        z = x.to_dict()
        self.assertIsInstance(z, dict)
        self.assertEqual(z['__class__'], type(x).__name__)
        self.assertIn('created_at', z.keys())
        self.assertIn('updated_at', z.keys())
        self.assertNotEqual(y, x)


if __name__ == "__main__":
    unittest.main()
