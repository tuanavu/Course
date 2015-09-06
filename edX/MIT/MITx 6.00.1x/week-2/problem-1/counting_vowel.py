# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 19:22:31 2015

@author: tvu
"""

"""
COUNTING VOWELS  (10 points possible)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.

Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
    Number of vowels: 5
    
For problems such as these, do not include raw_input statements or define the variable s in any way. 
Our automated testing will provide a value of s for you - so the code 
you submit in the following box should assume s is already defined. 
If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.
"""

s = 'azcbobobegghakl'
total = 0
for c in s:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        total += 1
print "Number of vowels: " + str(total)
    