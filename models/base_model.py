#!/usr/bin/env python3
""" Base Class model setup """
from uuid import uuid4
from datetime import datetime
from engine import storage


class BaseModel:
    """Class Base Model created"""

    def __init__(self, *args, **kwargs):
        """
        Init instance for SuperClass Obj for instance creation for obj
        :param args: Unique id for each instance
        :param kwargs: Time it was created
        """
        self.id = str(uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()
        storage.new()

        if kwargs is not None:
            for key, value in self.__dict__.items():
                if not key.startswith("__class__"):
                    if key.startswith("created_at"):
                        # Convert strings to datetime objects
                        setattr(self, key, datetime.fromisoformat(str(value)))
                    elif key.startswith("updated_at"):
                        # Convert strings to datetime objects
                        setattr(self, key, datetime.fromisoformat(str(value)))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current date
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        :return:
        a dictionary containing all keys/values of __dict__ of the instance
        """
        # Use a new dictionary to store item
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__

        # Ensure a specific order of keys
        ordered_keys = ['my_number', 'name', '__class__', 'updated_at', 'id', 'created_at']

        # Create a new dictionary with the desired key order
        # ordered_dict = {key: instance_dict[key] for key in ordered_keys if key in instance_dict}
        ordered_dict = {}
        for key in ordered_keys:
            if key in instance_dict:
                ordered_dict[key] = instance_dict[key]

        # Convert 'created_at' and 'updated_at' to ISO format
        ordered_dict['created_at'] = self.created_at.isoformat()
        ordered_dict['updated_at'] = self.updated_at.isoformat()

        return ordered_dict
        # instance_dict['created_at'] = self.created_at.isoformat()
        # instance_dict['updated_at'] = self.updated_at.isoformat()
        # return  instance_dict

    def __str__(self):
        """
        str implementation for Class
        :return: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
