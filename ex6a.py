# ex5.py cwc
# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['orange', 'black', 'orange', 'black', 'orange', 'black']
t = turtle.Pen()
turtle.bgcolor('grey')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
