#!/usr/bin/python3
"""This is print_square module
"""

def print_square(size):
    """
    A function that prints square character


    Args:
        size: this is a size of square

    Prints:
        Prints square characters

    Raises:
        TypeError: if size is not an integer
        ValueError: if sie < 0
        TypeError: if size is a float and less than 0


    """


    if size < 0 and type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

