#!/usr/bin/python3
"""Defines a function"""


def text_indentation(text):
    """This is a function that prints a text with 2 new lines after
    each of these characters: . ? and :, text must be a string"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    prints = 0
    while prints < len(text) and text[prints] == " ":
        prints = prints + 1

    while prints < len(text):
        print(text[prints], end="")
        if text[prints] == "\n" or text[prints] in ".?:":
            if text[prints] in ".?:":
                print("\n")
            prints = prints + 1
            while prints < len(text) and text[prints] == " ":
                prints = prints + 1
            continue
        prints = prints + 1
