#!/usr/bin/python3
# 6-raise_exception_msg.py


def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as ne:
        print(ne)
