# -*- coding: utf-8 -*-
"""
Created on Wed Mar 04 09:38:07 2015

@author: tvu
"""
#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

def Hello(name):
    if name == 'Alice' or name == 'Nick':
        name = name + '???'
    else:
        DoesNotExist(name)
    name = name + "!!!!!"
    print 'Hello', name

# Gather our code in a main() function
def main():
    
    Hello(sys.argv[1])
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()