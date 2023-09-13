#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_table = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    if not roman_string or type(roman_string) != str:
        return 0
    total = 0

    for i in reversed(roman_string):
        numeral = roman_table[i]
        total += numeral if total < numeral * 5 else -numeral
    return total
