#!/usr/bin/env python3
"""" City Class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City Class Created """

    state_id = ""
    name = ""

    def __int__(self):
        """Constructor for City class"""
        super().__init__(*args, **kwargs)
