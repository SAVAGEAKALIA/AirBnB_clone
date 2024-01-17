#!/usr/bin/env python3
"""" Place Class that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place Class Created """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __int__(self):
        """Constructor for City class"""
        super().__init__(*args, **kwargs)
