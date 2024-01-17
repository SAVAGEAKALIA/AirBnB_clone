#!/usr/bin/env python3
"""" State Class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State Class Created """

    name = ""

    def __int__(self):
        """Constructor for State class"""
        super().__init__(*args, **kwargs)
