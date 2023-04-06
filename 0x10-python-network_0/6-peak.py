#!/usr/bin/python3
"""
This module contains a technical interview question.
Find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """This funciton is used ot find the peak in @list_of_integers.
    args:
        list_of_integers ([int]): list of integers
    Returns:
        a peak in the list or None
    """
    if isinstance(list_of_integers, list):
        length = len(list_of_integers)
        if length == 0:
            return None
        if length <= 2:
            return max(list_of_integers)
        mid = length // 2
        if list_of_integers[mid] > list_of_integers[mid-1] and \
                list_of_integers[mid] > list_of_integers[mid+1]:
            return list_of_integers[mid]
        elif list_of_integers[mid - 1] > list_of_integers[mid]:
            return find_peak(list_of_integers[:mid])
        else:
            return find_peak(list_of_integers[mid:])
    return None
