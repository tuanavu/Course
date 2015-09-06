# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:07:43 2015

@author: tvu
"""

def selSort(L):
    """
    •  Loop invariant 
    –  Given preﬁx of list L[0:i] and suﬃx L[i+1:len(L)-­‐1], then preﬁx is sorted and no element in 
    preﬁx is larger than smallest element in suﬃx 
    1.   Base case: preﬁx empty, suﬃx whole list – invariant true 
    2.   Induc$on step: move minimum element from suﬃx to end of preﬁx. Since invariant true before 
    move, preﬁx sorted a\er append 
    3.   When exit, preﬁx is en$re list, suﬃx empty, so sorted
    """
    for i in range(len(L) - 1):
        minIndx = i
        minVal= L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal= L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp