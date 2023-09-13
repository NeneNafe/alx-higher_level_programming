#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary.keys())

    for keys in sort_keys:
        value_of_key = a_dictionary[keys]
        print(f"{keys}: {value_of_key}")
