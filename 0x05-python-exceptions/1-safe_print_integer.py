#!/usr/bin/python3
# 1-safe_print_integer.py


def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except ValueError:
        pass
        return False
