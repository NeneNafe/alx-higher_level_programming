#!/usr/bin/python3
for char_rev in range(122, 96, -1):
    if char_rev % 2 != 0:
        char_rev = char_rev - 32
    print("{}".format(chr(char_rev)), end="")
