#!/usr/bin/python3
import unittest
from unittest.mock import patch
from datetime import datetime
from models import storage
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}"
          .format(key, type(my_model_json[key]), my_model_json[key]))


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        # Set up any necessary configurations or objects before each test
        storage.__objects = {}

    def test_init(self):
        # Test the __init__ method
        model_instance = BaseModel()
        self.assertTrue(hasattr(model_instance, 'id'))
        self.assertTrue(hasattr(model_instance, 'created_at'))
        self.assertTrue(hasattr(model_instance, 'updated_at'))
        self.assertIsInstance(model_instance.created_at, datetime)
        self.assertIsInstance(model_instance.updated_at, datetime)

    def test_save(self):
        # Test the save method
        model_instance = BaseModel()
        initial_updated_at = model_instance.updated_at
        with patch('models.storage.save') as mock_save:
            model_instance.save()
            mock_save.assert_called_once()
            self.assertNotEqual(model_instance.updated_at, initial_updated_at)

    def test_to_dict(self):
        # Test the to_dict method
        model_instance = BaseModel()
        model_dict = model_instance.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_str(self):
        # Test the __str__ method
        model_instance = BaseModel()
        str_representation = str(model_instance)
        self.assertIsInstance(str_representation, str)
        self.assertIn(model_instance.__class__.__name__, str_representation)
        self.assertIn(model_instance.id, str_representation)


if __name__ == '__main__':
    unittest.main()
