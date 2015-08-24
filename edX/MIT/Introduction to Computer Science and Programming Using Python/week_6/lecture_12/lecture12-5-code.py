# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:44:19 2015

@author: tvu
"""

def genFib():
    """
    generate Fibonaci numbers on the fly
    """
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
    # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
        
        
def allStudents(self):
    if not self.isSorted:
        self.students.sort()
        self.isSorted= True
    for s in self.students:
        yield s
