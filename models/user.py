#!/usr/bin/env python3
"""" User Class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User Class Created """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __int__(self):
        """Constructor for User class"""
        super().__init__(*args, **kwargs)
