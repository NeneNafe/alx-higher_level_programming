#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != '':
        char1 = sentence[0]
    else:
        char1 = None
    return (len(sentence), char1)
