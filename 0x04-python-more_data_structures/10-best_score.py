#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.keys()) == 0:
        return (None)
    res = (list(a_dictionary.keys())[0], list(a_dictionary.values())[0])
    for i, j in a_dictionary.items():
        if j > res[1]:
            res = (i, j)

    return (res[0])
