#!/usr/bin/env python3
"""" Amenity Class that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity Class Created """

    name = ""

    def __int__(self):
        """Constructor for Amenity class"""
        super().__init__(*args, **kwargs)
