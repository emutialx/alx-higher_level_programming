#!/usr/bin/python3
    """8-rectangle: class rectangle from BaseGeometry
    """


class Rectangle(BaseGeometry):
    """
        Rectangle inerits from BaseGeometry
        Attributes:
            width (int): width of rectangle.
            height (int): height of rectangle.
        Methods:
            __init__ - initialises the Rectangle.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.height = height