#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c ** 2
    else:
        raise Exception("a cannot be greater than or ewual to b")
