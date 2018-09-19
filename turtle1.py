# turtle1.py
import turtle 
colors = ['navy blue', 'black', 'grey', 'red', 'white', 'yellow']
t = turtle.Pen()
turtle.bgcolor('grey')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/57)
    t.forward(x)
    t.left(75)
