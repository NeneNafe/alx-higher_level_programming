#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D':500,
            'M': 1000
    }

    prev, sum = 0, 0

    for i in roman_string:
        sum += roman_dict[i] if roman_dict[i] <= prev else roman_dict[i] - prev * 2
        prev = roman_dict[i]
    return sum
