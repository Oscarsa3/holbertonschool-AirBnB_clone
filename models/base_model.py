#!/usr/bin/python3
"""This is our class base for this proyect"""
import uuid
import datetime


class BaseModel:
    """This class has attributes and methods"""
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __str__(self):
        """Print"""
        dic = dict(self.__dict__, **{'id': self.id,
               'created_at': self.created_at, 'updated_at':
               self.updated_at})
        return f"[{self.__class__.__name__}] ({self.id}) {dic})"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        return dict(self.__dict__, **{'id': self.id, '__class__':
               self.__class__.__name__, 'created_at':
               self.created_at.isoformat(), 'updated_at':
               self.updated_at.isoformat()})
