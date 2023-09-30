#!/usr/bin/python3
"""
Module 6-peak
defines function find_peak()
"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers using binary search."""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    start = 0
    end = len(list_of_integers) - 1
    ls = list_of_integers

    while start <= end:
        mid = (start + end) // 2

        # Check if the middle element is a peak
        if (mid == 0 or ls[mid] >= ls[mid - 1]) and \
                (mid == len(ls) - 1 or ls[mid] >= ls[mid + 1]):
            return ls[mid]

        # If the mid element is not a peak, search in left or right subarray
        if mid > 0 and ls[mid] < ls[mid - 1]:
            end = mid - 1
        else:
            start = mid + 1

    # No peak found
    return None
