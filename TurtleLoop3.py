#------------------------------------------------------------------------------
#  TurtleLoop3.py
#------------------------------------------------------------------------------

import turtle

n = int(input('Enter the number of sides: '))
wn = turtle.Screen()      
wn.bgcolor("lightgreen")
wn.title(str(n)+"-gon")

bob = turtle.Turtle()  
bob.color("blue", "red")  # pen color, fill color
bob.pensize(2)

bob.begin_fill()
for i in range(n):
   bob.forward(840/n)
   bob.left(360/n)
bob.end_fill()

wn.mainloop()