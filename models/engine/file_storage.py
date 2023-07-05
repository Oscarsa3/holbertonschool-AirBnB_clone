#!/usr/bin/python3
"""This class serializes instances to a JSON file
and deserializes JSON file to instances"""
import json


class FileStorage:
    """h"""
    def __init__(self):
        """Inicializador"""
        self.__file_path = f"{self.__class__.__name__}.json"
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects = {f"{obj.__class__.__name__}.{obj.id}": obj.__str__()}

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            return f.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.loads(f.read())
        except Exception:
            pass
