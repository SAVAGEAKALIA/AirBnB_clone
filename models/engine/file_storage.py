#!/usr/bin/env python3
""" New file for File Storage """
from json import load, dump


class FileStorage:
    """
    Class for created for file storage
    Deserialization/Serialization of python Dictionary
    """

    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        """ string - path to the JSON file (ex: file.json) getter"""
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        """string - path to the JSON file (ex: file.json)"""

        # with open("file.json", mode="r+", encoding="utf-6") as f:
        # f = dumps(value)

        self.__file_path = value

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

        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            dump(self.__objects, f)

    def reload(self):
        """
        Deserializes __objects json.file to dict
        :return:
        """

        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                self.__objects = load(f)
        except FileNotFoundError:
            pass  # Ignore if the file doesn't exist