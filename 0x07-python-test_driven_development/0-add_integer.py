#!/usr/bin/python3
"""Module for add_integer method"""


def add_integer(a, b=98):
    """
    This is the "add_integer" module.

    Args:
        a: an integer
        b: an integer

    Raises:
        TypeError: if a, b are niether int or float.

    Returns:
        sum of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
