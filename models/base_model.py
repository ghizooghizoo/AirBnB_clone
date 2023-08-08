#!/usr/bin/python3
"""BaseModel Class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self):
        """constructor to make instance"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ return string representation of the object"""
        return ('[' + type(self).__name__ + '] (' + str(self.id) +
                ') ' + str(self.__dict__))

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance"""
        tempDict = self.__dict__.copy()
        tempDict["__class__"] = self.__class__.__name__
        tempDict["created_at"] = self.created_at.isoformat()
        tempDict["updated_at"] = self.updated_at.isoformat()
        return tempDict
