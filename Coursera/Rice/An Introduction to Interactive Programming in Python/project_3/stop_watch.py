# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:36:10 2015

@author: tvu
"""
"""
URL : http://www.codeskulptor.org/#user40_StCqGjUhyt_0.py
Test format: http://www.codeskulptor.org/#user40_7WdqxzCjLI_0.py
"""

# template for "Stopwatch: The Game"
import simplegui
# define global variables
counter = 0
A = 0
B = 0
C = 0
D = 0
x = 0
y = 0
score = '0/0'
message = '0:00:0'

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A,B,C,D
    
    A = t // 600
    B = int((t // 10 % 60) // 10)
    C = int((t // 10 % 60) % 10)
    D = int(t % 10)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
     if timer.is_running() == False:
        timer.start()

def stop_button_handler():
      if timer.is_running() == True:
        timer.stop()
        global y
        y = y + 1
        if D == 0:
            global x
            x = x + 1
        global score
        score = str(x)+"/"+str(y)


def reset_button_handler():
    timer.stop()
    
    global message
    message = '0:00:0'
    global counter
    counter = 0
    global score
    score = '0/0'

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter += 1
    format(counter)
    
    global message
    message = str(A) + ":"+str(B) + str(C) +'.'+ str(D)
    

# define draw handler
def draw(canvas):
    canvas.draw_text(message, [100,100], 36, "white")
    canvas.draw_text(score,[250,20],28,'white')

    
# create frame
frame = simplegui.create_frame("Timer", 300, 200)
frame.set_draw_handler(draw)
# register event handlers
timer = simplegui.create_timer(100, timer_handler)
button1 = frame.add_button('Start', start_button_handler,200) 
button2 = frame.add_button('Stop', stop_button_handler,200) 
button3 = frame.add_button('Reset', reset_button_handler,200)

# start frame
frame.start()
timer.start()
timer.stop()

# Please remember to review the grading rubric
