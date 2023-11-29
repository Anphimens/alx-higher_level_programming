#!/usr/bin/python3
# 5-print_comb2.py

"""A program that prints numbers from 0 to 99"""
for i in range(0, 100):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
