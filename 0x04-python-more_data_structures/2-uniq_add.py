#!/usr/bin/python3

def uniq_add(my_list=[]):

    new_set = set()
    result = 0

    for number in my_list:
        if number not in new_set:
            result += number
            new_set.add(number)

    return result
