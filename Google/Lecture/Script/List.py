# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 15:10:59 2015

@author: tvu
"""

import commands
import sys
import os


def List(dir):    
    filenames = os.listdir(dir)
    for filename in filenames:
        path = os.path.join(dir, filename)
        print path
        print os.path.abspath(path)

# Gather our code in a main() function
def main():
    
    List(sys.argv[1])
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()