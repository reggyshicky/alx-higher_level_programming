#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """fuction that finds the peak of a list"""
    list_len = len(list_of_integers)

    left = 0  # leftmost index
    right = list_len - 1  # rightmost index

    if list_len == 0:
        return None

    while (left < right):

        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
