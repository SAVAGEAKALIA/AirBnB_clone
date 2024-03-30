#!/usr/bin/env python3
""" Base Class model setup """
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Class Base Model created"""

    def __init__(self, *args, **kwargs):
        """
        Init instance for SuperClass Obj for instance creation for obj
        :param args: Unique id for each instance
        :param kwargs: Time it was created
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(str(value)))
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

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
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        """
        str implementation for Class
        :return: [<class name>] (<self.id>) <self.__dict__>
        """
        cls = self.__class__.__name__
        cls_id = self.id
        cls_dic = self.__dict__
        return "[{}] ({}) {}".format(cls, cls_id, cls_dic)
