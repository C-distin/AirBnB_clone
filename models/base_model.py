#!/usr/bin/python3
"""
Base Model class
"""


from datetime import datetime
import uuid
import models


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes Base Instance
        """
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "id":
                    self.id = value
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of Base Instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute 'updated_at'
        with the current datetime
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        Returns dictionary representation of Base Instance
        """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.create_at.isoformat()
        new_dict['updated_at'] = self.update_at.isoformat()
        return new_dict
