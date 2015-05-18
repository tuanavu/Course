# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 13:40:51 2015

@author: tvu
"""

#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

def Cat(filename):
    f = open(filename, 'rU')
    for line in f:
        print line,
    f.close()

# Gather our code in a main() function
def main():
    
    Cat(sys.argv[1])
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()