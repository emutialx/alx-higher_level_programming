#!/usr/bin/python3
"""
    6-base_geometry: class BaseGeometry
"""


class BaseGeometry:
    """
        baseGeometry
        Attributes: None.
        Methods:
            area() - raises an exception
            integer_validator() - validates value.
    """
    def area(self):
        """
        Area raise an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            integer_validator checks the value of value.
            Args: 
                name (str): name
                value (int): value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
