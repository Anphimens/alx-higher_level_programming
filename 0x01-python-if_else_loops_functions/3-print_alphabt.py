#!/usr/bin/python3
# 3-print_alphabet.py

"""Prints the ASCII alphabet in lowercase, not followed by a new line"""
for letter in range(97, 123):
    if chr(letter) in ['q', 'e']:
        continue
    print("{}".format(chr(letter)), end="")
