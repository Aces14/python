#https://www.geeksforgeeks.org/turtle-programming-python/
import turtle  #Inside_Out
wn = turtle.Screen()
wn.bgcolor("#00ff00")
cr = turtle.Turtle()
cr.color("blue")

def sqrfunc(size):
    cr.width(size/5)
    for i in range(4):
        cr.fd(size)
        cr.left(90)
        size = size + 10

sqrfunc(10)
sqrfunc(20)
sqrfunc(30)
sqrfunc(40)
sqrfunc(50)
sqrfunc(60)
sqrfunc(70)
sqrfunc(80)
holdit = input();
