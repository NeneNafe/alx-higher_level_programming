#!/usr/bin/python3
"""Defines a function"""


def class_to_json(obj):
    """
    a function that returns the dictionary description with simple
    data structure for JSON serialization of an object
    """

    if isinstance(obj, int) or isinstance(obj, bool) or isinstance(obj, str):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        result = {}
        for key, value in obj.__dict__.items():
            result[key] = class_to_json(value)
        return result
    else:
        return None
