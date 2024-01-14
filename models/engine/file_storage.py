#!/usr/bin/env python3
""" New file for File Storage """
import json
import os


class FileStorage():
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

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Deserializes __objects json.file to dict
        :return:
        """


        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                self.__objects = json.load(f)
        else:
            pass  # Ignore if the file doesn't exist