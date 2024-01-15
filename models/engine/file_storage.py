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
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        :return:
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        :return:
        """
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes __objects json.file to dict
        :return:
        """

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                dic = json.load(f)
                for key, value in dic.items():
                    my_class = value.get("__class__", None)
                    if my_class:
                        try:
                            new_obj = eval(my_class)(**value)
                            self.__objects.update({key: new_obj})
                        except NameError:
                            # Handle the case when the class is not defined
                            pass
        else:
            pass  # Ignore if the file doesn't exist
