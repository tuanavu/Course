# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:56:21 2015

@author: tvu
"""

def DFSBinary(root, fcn):
    stack= [root]
    while len(stack) > 0:
        if fcn(stack[0]):
            return True
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
    return False