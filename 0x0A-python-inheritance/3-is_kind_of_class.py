#!/usr/bin/python3
"""
    3-is_kind_of_class: is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class returns True if object is an instance of inherited class from.
        Args:
            obj (object): object.
            a_class (class): class.
        Return: True or False.
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
