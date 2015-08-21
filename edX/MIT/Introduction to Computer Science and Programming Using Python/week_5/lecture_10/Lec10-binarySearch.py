# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 08:55:52 2015

@author: tvu
"""

def search(L, e):
    """    
    1.   Pick an index, i, that divides list in half 
    2.   Ask if L[i] == e
    3.   If not, ask if L[i] larger or smaller than e
    4.   Depending on answer, search leK or right half of L for e

    A new version of a divide-­‐and-­‐conquer algorithm 
    •     Break into smaller version of problem (smaller list), 
    plus some simple operaBons 
    •     Answer to smaller version is answer to original 
    problem 
    """
    def bSearch(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = low + int((high - low)/2)
        if L[mid] == e:
            return True
        if L[mid] > e:
            return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)
    
    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)