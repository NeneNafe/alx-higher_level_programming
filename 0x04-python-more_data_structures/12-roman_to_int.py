#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    prev, sum = 0, 0

    for i in roman_string:
        sum += roman_dict[i] if roman_dict[i] <= prev else roman_dict[i] - prev * 2
        prev = roman_dict[i]
    return sum
