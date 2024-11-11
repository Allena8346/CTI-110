# Alexander Allen
# 28Oct24
# P4LAB1
# Use Loops to make a turtle object

import turtle             # Allows us to use turtles
win = turtle.Screen()      # Creates a playground for turtles
t = turtle.Turtle()    # Create a turtle, assign to t
# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("purple")     # set pencolor (takes string)
t.shape("arrow")


#While Loop to drae 4 sides of square
line = 0
while line < 4:
    t.right(90)
    t.forward(50)
    line += 1
'''
for s in ("1"):
    t.forward(50)          
    t.left(90)             
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
'''
# triangle, sides are 360 / 3 = 120 degrees
for tri in range(3):
    t.left(120) 
    t.forward(50)          

# end commands
win.mainloop()             # Wait for user to close window
