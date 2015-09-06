# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:09:58 2015

@author: tvu
"""

def merge(left, right, compare):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
    

import operator
def mergeSort(L, compare = operator.lt):
    """
    Complexity: O(n log n)
    Use a divide-­‐and-­‐conquer approach:
    1. If list is of length 0 or 1, already sorted
    2. If list has more than one element, split into two lists, and sort each
    3. Merge results
        1. To merge, just look at first element of each, move smaller to end of the result
        2. When one list is empty, just copy rest of other list
    """
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)