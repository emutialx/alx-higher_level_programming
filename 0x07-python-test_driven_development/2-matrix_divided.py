#!/usr/bin/python3
"""This is matrix division module"""

def matrix_divided(matrix, div):
    """Function that divides matrix to a given number

    Args:
        div: The divisor

    Returns:
        The result is a list of matrix divided by div
    Raises:
        TypeError: If matrix lists of list is not float or integer
        TypeError: If Each row of matrix is not equal
        TypeError: If div is not float or integer
        ZeroDivisionError: if div is zero
    """
    
    for k in matrix:
        for j in k:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return (list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix)))
