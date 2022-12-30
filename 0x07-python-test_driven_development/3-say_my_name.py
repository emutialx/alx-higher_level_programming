#!/usr/bin/python3
"""This is a say_my_name module
"""

def say_my_name(first_name, last_name=""):
    """ Gunction that prints a name

    Args:
        first_name: this is a firstname
        last_name: this is last name
    
    Prints:
        First name and last name

    Raises:
        TypeError: if first_name and last_name is not strings

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
