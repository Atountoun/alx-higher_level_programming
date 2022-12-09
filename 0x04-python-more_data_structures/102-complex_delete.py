#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    values = list(a_dictionary.values())
    items = list(a_dictionary.items())
    if value in values:
        for key, val in items:
            if val == value:
                del a_dictionary[key]

    return (a_dictionary)
