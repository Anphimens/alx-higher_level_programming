#!/usr/bin/python3
# 5-text_indentation.py
# Antoinette P Mensah
"""Defines a text-indentation function with
    Prototype:
        def text_indentation(text):
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each
        ``.``, ``?``, and ``:``.

        Checks if the current charater is a newline
        or one of ".", "?", ":"

        -   if yes, two new lines are printed (indentation)
        -    the character 's' skips spaces after the newline
            punctuation and moves to the next character

        Args:
            text(str): string of text to print
        Raises:
            TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
                continue
        c += 1
