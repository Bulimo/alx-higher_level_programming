#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    sum = 0
    for i in set(my_list):
        sum += i
    return sum
