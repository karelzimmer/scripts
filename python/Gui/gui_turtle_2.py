
#Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
# By changing some of the parameters (r, R or d) and the number of iterations
# (steps) we can create more advanced patterns.

import turtle
from math import cos,sin
from time import sleep

def spiro_1(R,r,d, aantal):
    stoppen = False

    def screen_click(x,y):
        nonlocal stoppen
        stoppen = True
    
    turtle.bgcolor("#FFFFFF")
    turtle.tracer(0)
    turtle.onscreenclick(screen_click)

    mySpirograph = turtle.Turtle()
    mySpirograph.hideturtle()
    mySpirograph.speed(0)
    mySpirograph.pensize(2)

    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.speed(0)
    myPen.pensize(3)
    myPen.color("#AA00AA")

    angle = 0

    myPen.penup()
    myPen.goto(R-r+d,0)
    myPen.pendown()

    theta = 0.2
    steps = aantal * int(6*3.14/theta)
    print(steps)

    for t in range(0,steps):
        mySpirograph.clear()
        mySpirograph.penup()
        mySpirograph.setheading(0)
        mySpirograph.goto(0,-R)
        mySpirograph.color("#999999")
        mySpirograph.pendown()
        mySpirograph.circle(R)
        angle+=theta
        
        x = (R - r) * cos(angle)
        y = (R - r) * sin(angle)
        mySpirograph.penup()
        mySpirograph.goto(x,y-r)
        mySpirograph.color("#222222")
        mySpirograph.pendown()
        mySpirograph.circle(r)
        mySpirograph.penup()
        mySpirograph.goto(x,y)
        mySpirograph.dot(5)
        
        x = (R - r) * cos(angle) + d * cos(((R-r)/r)*angle)
        y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)
        mySpirograph.pendown()
        mySpirograph.goto(x,y)
        #mySpirograph.setheading((R-r)*degrees(angle)/r)
        #mySpirograph.forward(d)
        mySpirograph.dot(5)
        myPen.goto(mySpirograph.pos())
        
        turtle.update()
        if stoppen:
            break
        sleep(0.05)


#--- script ---

spiro_1(125,75,125, 1)         #R,r,d, aantal
#spiro_1(125,85,125, 4)

