# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 17:08:10 2015

@author: tvu
"""

import sys

def Cat(filename):
 try:
    f = open(filename)
    text = f.read()
    print '---', filename
    print text
 except IOError:    
     print 'IO Error', filename

# Gather our code in a main() function
def main():
    
    args = sys.argv[1:]
    for arg in args:
        Cat(arg)
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()