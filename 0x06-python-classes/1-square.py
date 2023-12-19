#!/usr/bin/python3
""" A class Square that defines a square by:
(based on 0-square.py)
"""


class Square:
    """ A class with name Square """
    def __init__(self, size):
        """ Initialization of the size """
        self.__size = size
        """ size is made private, because a size
        of a square is crucial for a square, many things depend of it
        """
