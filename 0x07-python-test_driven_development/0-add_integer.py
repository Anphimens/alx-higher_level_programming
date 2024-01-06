#!/usr/bin/python3
# 0-add_integer.py
# Antoinette P Mensah <philipinamensah19@gmail.com>
"""A function that adds two integers:
    The argument are typecasted into int before computing.
    Returns an "int"
    Raises a typeError if arguments != int or float
    """


def add_integer(a, b=98):
    """Raises:
    TypeError: if arguments, that is (a, b) != integers or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
