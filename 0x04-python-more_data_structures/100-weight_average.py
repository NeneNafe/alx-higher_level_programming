#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:
        return 0

    overall_score = 0
    overall_weight = 0

    for score, weight in my_list:
        overall_score += score * weight
        overall_weight += weight

    if overall_weight == 0:
        return 0

    weighted_average = overall_score / overall_weight
    return weighted_average
