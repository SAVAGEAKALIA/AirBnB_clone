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

        with open(FileStorage.__file_path, "a") as f:
            json.dump(obj_dict, f)
            # f.write(json.dumps(obj_dict))
            f.write('\n')

    def reload(self):
        """
        Deserializes __objects json. file to dict
        """
        try:
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, "r") as f:
                    for line in f:
                        obj_dict = json.loads(line)
                        my_class = obj_dict.get("__class__", None)
                        if my_class:
                            try:
                                new_obj = eval(my_class)(**obj_dict)
                                key = f"{my_class}.{new_obj.id}"
                                FileStorage.__objects[key] = new_obj
                                return FileStorage.__objects
                            except NameError:
                                # Handle the case when the class is not defined
                                pass
            else:
                pass  # Ignore if the file doesn't exist
        except FileNotFoundError:
            pass
