#!/usr/bin/python3
# 2-matrix_divided.py
# Antoinette P Mensah <philipinamensah19@gmail.com>
"""Division of all elements of a matrix:

    Prototype:
        def matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """A function that returns a new matrix from
    dividing all elements of the matrix.

    Args:
            matrix(list): [list[of list]] of integers or floats
            div (int/float): the divisor

    Raises:
        1. TypeError: if matrix is not a (list of lists) of integers/floats
        2. TypeError: if each row of the matrix does not have the same size
        3. TypeError: div is not a number
        4. ZeroDivisionError: if div is equal to zero

    Note: All elements of the matrix should be divided by div,
    rounded to 2.decimal places

    Returns a new matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
