#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """
        returns the string representation of the
        BaseModel class
        """
        return ('[{}], ({}), {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            my_dict[k] = v
        return my_dict
