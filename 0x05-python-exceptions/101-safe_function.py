#!/usr/bin/python3
# 101-safe_function.py
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        error_msg = "Exception: {}".format(e)
        print(error_msg, file=sys.stderr)
        return None
    return result
