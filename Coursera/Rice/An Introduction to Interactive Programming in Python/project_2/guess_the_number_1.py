# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:08:25 2015

@author: tvu
"""

"""
URL Solution: http://www.codeskulptor.org/#user40_ixQX5uTEDr_1.py
"""

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

num_range = 100
secret_number = 0
n = 0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global n
    if num_range == 100:
        n = 7
    elif num_range == 1000:
        n = 10
    global secret_number
    secret_number = random.randrange(0,num_range)
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is ",n 


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range 
    num_range = 100    
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range 
    num_range = 1000    
    new_game()    
    
def input_guess(guess):
    # main game logic goes here	    
    num = int(guess)
    print "Guess was", guess
    global n
    n -= 1
    print "Number of remaining guesses is", n
    if num > secret_number:
        print "Lower\n"
    elif num < secret_number:
        print "Higher\n"
    else:
        print "Correct!!!\n"        
        new_game()    
    if n == 0:
        print "Game Over!!!\n"
        new_game()
    

    
# create frame
frame = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
button1 = frame.add_button('range100', range100, 200) 
button2 = frame.add_button('range1000', range1000, 200)                      
frame.add_input("Enter guess number", input_guess, 200)

# Start frame and timers
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
