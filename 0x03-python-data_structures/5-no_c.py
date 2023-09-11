#!/usr/bin/python3

def no_c(my_string):
    result = ""

    for a in my_string:
        if a != 'c' and a != 'C':
            result += a
    return result
