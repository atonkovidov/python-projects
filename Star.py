#Andre Tonkovidov
#atonkovi@ucsc.edu
#pa2
#Draws a green-filled, blue star with an odd, user-provided number of points
#represented by red dots.

import turtle

s = int(input('Enter an odd integer greater than or equal to 3: '))
fw = turtle.Screen()
fw.title(str(s) +'-pointed star')

frank = turtle.Turtle()
frank.color('blue', 'green2')
frank.pensize(2)
frank.hideturtle()

frank.speed(0)
frank.penup()
frank.setx(-150)
frank.pendown()

frank.begin_fill()
for i in range(s):
   frank.forward(300)
   frank.right(180-(180/s))
   frank.dot(10, 'red')
frank.end_fill()

fw.mainloop()