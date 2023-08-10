#!/usr/bin/python3
'''class inherent of BaseModel'''
from models.base_model import BaseModel




class Amenity(BaseModel):
    '''class amenity'''


    name = ""


    def _init_(self, *args, **kwargs):
        """initializes Amenity"""
        super()._init_(*args, **kwargs)
