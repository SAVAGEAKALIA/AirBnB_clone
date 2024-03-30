#!/usr/bin/env python3
""" New file for File Storage """
import json
import os


class FileStorage:
    """
    Class for created for file storage
    Deserialization/Serialization of python Dictionary
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        :return:
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {}

        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes __objects json. file to dict
        """
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, "r", encoding="UTF-8") as f:
                    # json.loads converts to python object
                    obj_dict = json.load(f)

                for key, dictionary in obj_dict.items():  # Corrected `items()`
                    # Check for class name within any value

                    class_name = dictionary['__class__']
                    obj_id = dictionary["id"]
                    key = "{}.{}".format(class_name, obj_id)
                    new_obj = self.classes()[class_name](**dictionary)

                    self.__objects[key] = new_obj

            else:
                # Handle objects without a valid class name
                # print("Warning: No File Path Detected")
                pass
        except FileNotFoundError:
            pass

    def classes(self):
        """ This code is written to handle the importation of classes"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        return {"BaseModel": BaseModel,
                "User": User,
                "Amenity": Amenity,
                "City": City,
                "Place": Place,
                "Review": Review,
                "State": State
                }
