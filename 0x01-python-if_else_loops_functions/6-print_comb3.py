#!/usr/bin/python3
# 6-print_comb3.py

"""A program that prints all possible combinations of two digits"""
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        if tens_digit == 8 and ones_digit == 9:
            print("{}{}".format(tens_digit, ones_digit))
        else:
            print("{}{}".format(tens_digit, ones_digit), end=", ")
