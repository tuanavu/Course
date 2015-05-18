# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 16:14:04 2015

@author: tvu
"""

import commands
import sys
import os


def Status(dir):
    cmd = 'ls ' + dir
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        print sys.stderr.write('there was an error:'+ output)
        sys.exit(1)
    print output  

# Gather our code in a main() function
def main():
    
    Status(sys.argv[1])
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()