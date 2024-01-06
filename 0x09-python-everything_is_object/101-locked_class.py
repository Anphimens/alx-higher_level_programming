#!/usr/bin/python3
# 101-locked_class.py
"""Defines a locked class """


class LockedClass:
    """
   A class with no class or object attribute,
   prevents the user from dynamically creating
   new instance attributes, except if the new
   instance is called 'first_name'
    """
    __slots__ = ["first_name"]
