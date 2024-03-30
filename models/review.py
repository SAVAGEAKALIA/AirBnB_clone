#!/usr/bin/env python3
"""" Review Class that inherits from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review Class Created """

    place_id = ""
    user_id = ""
    text = ""

    def __int__(self):
        """ Constructor for Review class"""
        super().__init__(*args, **kwargs)
