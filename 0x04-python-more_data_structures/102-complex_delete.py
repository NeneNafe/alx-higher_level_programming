#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_list = []
    if value in a_dictionary.values():
        for key, val in a_dictionary.items():
            if value == val:
                key_list.append(key)

        for key1 in key_list:
            if key1 in a_dictionary:
                del a_dictionary[key1]
    return a_dictionary
