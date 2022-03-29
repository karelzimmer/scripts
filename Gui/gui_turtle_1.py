#gui turtle

"""

turtle zit in Lib\turtle.py

p = turtle.Pen()
p = turtle.Turtle()     idem
p = turtle.Turtle(shape='classic', undobuffersize=1000, visible=True)
scn = turtle.Screen()
shp = turtle.Shape("polygon", tuple)   [zie register_shape()]
shp = turtle.Shape("compound", None)
    shp.addcomponent(tuple, fillclr, [penclr])
    ...

turtle.mainloop() en turtle.exitonclick() [doet bye() + mainloop()]
MOETEN aan einde script, want blocking.

turtle.tracer(0) ->geen autom update, geen animatie; moet turtle.update() gebr
turtle.tracer(1) ->autom update + animatie
turtle.tracer(>=2) ->autom update zonder animatie; ververst 1 per n keer

bij p.speed(0) of turtle.tracer(<>1) geen animatie, wegens code in RawTurtle._goto():
if self._speed and screen._tracing == 1: ->wel animatie

Pen/Turtle motion:
home()
forward() | fd()
backward() | bk() | back()
left(angle) | lt(); right() | rt()     [relatieve hoek, mag neg]

goto() | setpos() | setposition(x, y)
setx(); sety()
setheading(angle) | seth()   [abs hoek, mag neg; 0 = naar rechts]

dot(px, [clr])   [ook bij p.up()]
stamp()          [= afdruk v turtle; ook bij p.up()]
write(txt, move=False, align="left", font=("Arial",8,"normal")) [ook bij p.up()]
circle([-]r, [[-]angle])

clearstamp()
clearstamps()
undo()
speed(0..10|"normal"|"fast[est]"|"slow[est]")  [1=traag, 10=snel, 0=turbo]

Pen control:
pendown() | pd() | down(); penup() | pu() | up()
isdown()
showturtle() | st(); hideturtle() | ht()
isvisible()
pensize(px) | width(px)

color(pen, fill) of (beide): "blue", "#rrggbb", (r,g,b)
pencolor()
fillcolor()
filling() ->bool, True na begin_fill()
begin_fill()
end_fill()

Pen state:
xcor(); ycor()
position() | pos() ->turtle.Vec2D (= x,y)
heading() ->abs angle; 0 = hor naar rechts bij mode="standard"
towards(x,y) of (turtle2) ->abs angle
distance(x,y) of (turtle2) ->dist
pen() ->status dict

More drawing control:
clone() ->kopie v turtle
reset()
clear()
begin_poly()      [normaal eerst reset() doen]
end_poly()
get_poly() ->tuple, kan tuple ook zelf definieren
getturtle() | getpen()
getscreen()   [geeft scn.xyz() ipv turtle.xyz()]
setundobuffer()    [dflt 1000]
undobufferentries()

Turtle appearance:
shape("name")   ["classic","arrow","turtle","circle","square","triangle"]
resizemode("noresize"|"auto"|"user")   ["user" ->zie vlg]
shapesize() | turtlesize(stretch_wid, stretch_len, outline)
shearfactor()
settiltangle()     [abs angle, vgl setheading(..)]
tiltangle()        [get abs angle, vgl heading()]
tilt(angle)        [relatieve draaiing angle]
shapetransform()
get_shapepoly()

Turtle events:
[vlg add=True ->voeg fn toe aan event-actions, ipv vervang fn]
onclick(fn, btn=1, add=None)      [fn(x,y), btn: 1=li,2=mid,3=re]
onrelease(fn, btn=1, add=None)
ondrag(fn, btn=1, add=None)

Screen [scn.xyz(), kan ook via global turtle.xyz()]:
title()
bgcolor()
bgpic("gif")
clearscreen()
resetscreen()
screensize([w,h],[bgclr])
window_height()
window_width()
setup(width,height, startx,starty) ->window size; dflt 0.5,0.75, None,None

mainloop() | done()    [blocking; onderdrukt in IDLE >>> aan einde tekening]
bye()   [sluit screen]
exitonclick()    [blocking; doet bye() bij muisklik + mainloop()]
listen() [nodig voor key-listen events; geeft screen de focus]

Text:
textinput(title, prompt)
numinput(title, prompt, default=None, minval=None, maxval=None)

Animation control:
delay([msecs])      [=tussen screen updates]
tracer([n], [delay])  [alleen 1 keer per n verversen; 0=nooit]
update()

Settings and special methods:
mode("standard"|"logo"|"world")
setworldcoordinates(llx,lly, urx,ury)   [eigen coord stelsel: lion, rebo]
colormode(1.0|255)    [dflt=1.0; kleurschaal: 0.0-1.0 of 0-255]
getcanvas()
getshapes()
register_shape(..) | addshape("name", shape=None)
  ["myturtle.gif" | "mytriangle", ((5,-3), (0,5), (-5,-3)) | "myshape", shp]
 ]
turtles() ->list v actieve turtle-objn (std 1)

Screen events (non-blocking):
onkey() | onkeyrelease(fn, "key")       [fn(), None = wis ev handler]
onkeypress(fn, ["key"])                 [idem]
onscreenclick(fn, btn=1, add=None (of: True|False))    [fn(x,y)]
ontimer(fn, t=msecs)      [fn(), gebr voor infinite loop]

"""

import turtle
from math import *
from tkinter import messagebox, colorchooser
import time

p = turtle.Pen()        #of: turtle.Turtle()

stop = False
def screen_click(x,y):      #event-fn onscreenclick-event
    global stop
    stop = True

def setdot(pen, pos, clr="black"):
    oldpos = pen.pos()
    oldcolor = pen.pencolor()
    olddown = pen.isdown()
    oldvis = pen.isvisible()
    pen.up()
    pen.ht()
    pen.goto(pos)
    pen.pencolor(clr)
    pen.dot()
    pen.pencolor(oldcolor)
    pen.goto(oldpos)
    if olddown:
        pen.down()
    if oldvis:
        pen.st()

def jump(pen, x,y):
    olddown = pen.isdown()
    pen.up()
    pen.goto(x,y)
    if olddown:
        pen.down()

def line(pen, x1,y1, x2,y2):
    pen.up()
    pen.setpos(x1,y1)
    pen.down()
    pen.goto(x2,y2)
    
    
def test_status():
    #turtle.setup(400,300)          #windowgrootte

    print("Screen:")
    print("screensize =", turtle.screensize())        #(400,300), canvas
    print("window w,h =", turtle.window_width(), turtle.window_height())
    #->512,450, want doet: 0.5, 0.75 -> 1/2 + 3/4 scherm
    print("mode =", turtle.mode())                #standard
    print("colormode =", turtle.colormode())      #1.0
    print("bgcolor =", turtle.bgcolor())          #white
    #turtle.bgcolor(230,230,230)                #dflt error, wegens colormode(1.0)
    #turtle.bgcolor(0.8,0.8,1.0)                #goed
    print("delay =", turtle.delay())              #10
    print("tracer =", turtle.tracer())            #1

    print("\nTurtle:")
    print("speed =", p.speed())                 #3
    print("shape =", p.shape())                 #classic
    #p.shapesize(5)      #wijz wid,len: (5,5,1) + wijz resizemode in "user"
    print("shapesize =", p.shapesize())         #(1.0, 1.0, 1)
    print("resizemode =", p.resizemode())       #noresize
    print("shearfactor =", p.shearfactor())     #0.0
    print("tiltangle =", p.tiltangle())         #0.0
    print("pos =", p.pos())                     #(0.00,0.00) [Vec2D]
    print("heading =", p.heading())             #0.0
    print("width =", p.width())                 #1
    print("color =", p.color())                 #('black', 'black')
    print("isvisible =", p.isvisible())         #True
    print("isdown =", p.isdown())               #True

    print("\npen dict:\n", p.pen())

def test_input():
    #a = int(input("Hoeveel naar voren: "))
    a = turtle.numinput("Vraag", "Hoeveel naar voren:", 20,10,150)     #float
    # vor None bij knop Cancel
    print(type(a))
    if a:                   #moet, anders error bij p.forward(None)
        p.forward(a)

def test_cirkel():
    #turtle.tracer(2, 10)
    print(turtle.delay())

    #print(p.resizemode())      #noresize
    #p.shape("triangle")
    #p.width(15)
    
    #p.up()
    #p.dot()                 #tekent ook bij up()
    #p.stamp()               #idem
    #p.write("AHAAAA")       #idem
    #p.down()
    #setdot(p, (0,50), "red")

    #p.left(90)
    #p.right()

    p.circle(50, 135)          #naar links, vooruit
    #p.circle(-50, 135)         #naar rechts, vooruit
    #p.circle(50, -135)         #naar links, achteruit (pen wijst terug)
    #p.circle(-50, -135)        #naar rechts, achteruit

    #turtle.tracer(0)           #doet niet autom refresh
    #turtle.update()            #handmatig refresh


def vierkant_01():
    p.pensize(2)            #idem p.width(2)
    for _ in range(4):
        p.forward(50)
        p.left(90)

    print("undobuff", p.undobufferentries())
    print(p.pos())
    p.color("red")
    p.goto(50,50)
    p.up()
    p.right(90)
    p.fd(50)
    p.down()
    print(p.pos(), p.heading())
    p.right(135)
    p.fd(50 * sin(radians(45)))       #tot diagonaal
    #p.fd(50 / sin(radians(45)))      #reon ->libo

    #p.undo()

    #p.mainloop()            #error, hoort bij screen

def ster_01():
    # vijfhoek:
    #turtle.exitonclick()           #blocking
    p.speed(1)
    for _ in range(5):
        p.forward(80)
        #p.right(144)            #180-36
        p.right(72)

    p.up()
    p.backward(120)
    p.right(90)
    p.fd(10)
    p.down()
    p.color("slate blue")
    p.write("Vijfhoek!", font=('',16,''))
    p.hideturtle()

def ster_02():
    # veelhoeken:
    p.up()
    p.goto(-160,20)
    p.down()
    p.dot()
    for _ in range(8):
        p.forward(90)
        p.left(225)                 #turtle draait rond
        #p.right(135)               #turtle maakt haakse hoek

    p.up()
    p.setheading(15)
    p.goto(80,0)
    p.color((0,0.2,0.9),(0.95,0.75,0))       #penclr,fillclr
    p.down()
    p.dot()
    p.pensize(2)
    p.begin_fill()
    #print(p.filling())          #True
    # 18 lijnen -> 9 punten -> per punt een hk van 360 / 9 = 40 graden
    # eist: hkre - hkli = 40; bv 45 knik re - 5 scherpe punt li
    hkre = 130              #bv 180 - 135 = 45 binnenhoek knik re
    hkli = 170              #bv 180 - 175 = 5 binnenhoek punt li
    for i in range(18):
        p.forward(80)
        if i % 2:
            p.right(hkre)
        else:
            p.left(hkli)
    p.end_fill()
    #print(p.filling())         #False
    p.hideturtle()

def cirkels_01():
    turtle.onscreenclick(screen_click)
    #p.speed(2)          #dflt 3
    for i in range(1,24):
        p.circle(5*i)
        p.circle(-5*i)
        p.left(i)
        if stop:
            break

def patroon_01():
    turtle.bgcolor("lightblue")
    turtle.title("Doolhof vierkant")
    size = 150
    p.up()
    p.goto(-size/2, -size/2)
    p.down()
    p.ht()                  #of: p.hideturtle()
    p.speed(4)

    while size >= 10:
        p.fd(size)          #forward
        p.lt(90)            #left
        size -= 5

def patroon_02():
    #turtle.delay(50)
    #turtle.tracer(2)       #geen animatie
    #print(turtle.delay())

    turtle.bgcolor("black")
    turtle.title("Spiraal in kleur")
    turtle.onscreenclick(screen_click)
    colors = ["red","purple","blue","green","orange","yellow"]
    p.hideturtle()
    p.speed(6)
    for i in range(0,220):
        p.pencolor(colors[i % 6])
        p.pensize(i/80 + 1)
        p.forward(i)
        p.left(59)          #bij 60 geen verschuiving
        if stop:
            break

def patroon_03():
    #turtle.tracer(2)       #>1 ->geen animatie; 2 = om en om verversen
    turtle.title("Nautilus")
    turtle.onscreenclick(screen_click)
    p.hideturtle()
    p.speed(0)          #wel update, geen animatie
    p.pencolor("MediumAquamarine")
    h = 20
    for i in range(181):
        for _ in range(4):          #teken rechthoek
            p.forward(h)
            p.right(90)
        p.right(6)
        h = h * 1.01
        if stop:
            break

def fractal_tree_01():
    turtle.title("Fractal tree")
    hk = 30
    krimp = 0.75

    p.color("green")
    p.speed(7)
    p.pensize(3)
    p.left(90)
    p.up()
    p.bk(100)
    p.down()

    def vertak(lengte):         #recursieve fn
        if lengte < 10:
            return
        p.width(round((lengte+1)/16))
        p.fd(lengte)
        p.lt(hk)
        vertak(krimp * lengte)
        p.rt(2 * hk)
        vertak(krimp * lengte)
        p.lt(hk)
        p.pu()
        p.bk(lengte)
        p.pd()

    vertak(80)

def setup_xy_as(xschaal):
    p.up()
    p.bk(2*xschaal)
    p.down()
    for _ in range(4):
        p.forward(xschaal)
        p.dot()
    p.up()
    p.home()
    p.left(90)
    p.bk(150)
    p.down()
    p.fd(300)
    p.up()
    p.home()
    p.setheading(0)
    p.down()

def functie_01():
    # y = 0.6 * x - 20
    setup_xy_as(100)
    p.pencolor("red")
    x = -100
    y = 0.6 * x - 20
    jump(p, x,y)
    for x in range(-100,100, 10):
        y = 0.6 * x - 20
        p.goto(x,y)
    p.ht()

def functie_02():
    # y = (x+3)*(x-4)
    # y = x**2 + 3*x + 5
    # y = 0.2*x**3 - x**2 + 3*x + 2
    turtle.setworldcoordinates(-10,-20, 10,40)
    line(p, -9,0, 9,0)
    line(p, 0,-18, 0,38)
    p.pencolor("red")
    x = -6
    #y = (x+3)*(x-4)
    #y = x**2 + 3*x + 5
    y = 0.2*x**3 - x**2 + 3*x + 2
    jump(p, x,y)
    for x in range(-6,7):
        #y = (x+3)*(x-4)
        #y = x**2 + 3*x + 5
        y = 0.2*x**3 - x**2 + 3*x + 2
        p.goto(x,y)
    p.ht()

def functie_03():
    # y = sin(radians(x))
    # y = cos(radians(x))
    turtle.setworldcoordinates(-90,-2, 450,2)
    line(p, -80,0, 420,0)
    line(p, 0,-2, 0,2)
    p.pencolor("red")
    x = 0
    #y = sin(radians(x))
    y = cos(radians(x))
    jump(p, x,y)
    for x in range(0,361,5):
        #y = sin(radians(x))
        y = cos(radians(x))
        p.goto(x,y)
    p.ht()

def functie_04():
    # y = sin(x)/x          sync-formule
    turtle.setworldcoordinates(-40,-2, 40,2)
    line(p, -40,0, 40,0)
    line(p, 0,-2, 0,2)
    p.pencolor("red")

    x = 0.1                     #rechts
    y = sin(x)/x
    jump(p, x,y)
    for _ in range(180):
        y = sin(x)/x
        p.goto(x,y)
        x += 0.2
    x = -0.1                    #links
    y = sin(x)/x
    jump(p, x,y)
    for _ in range(180):
        y = sin(x)/x
        p.goto(x,y)
        x -= 0.2
    line(p,-0.1,1, 0.1,1)       #punt (0,1)
    p.ht()

def achtergrond(pen, w, h, clr):
    jump(pen, -w/2-1, -h/2-1)
    pen.fillcolor(clr)
    pen.width(1)
    pen.begin_fill()
    pen.fd(w+2)
    pen.lt(90)
    pen.fd(h+2)
    pen.lt(90)
    pen.fd(w+2)
    pen.lt(90)
    pen.fd(h+2)
    pen.end_fill()
    pen.lt(90)

def lijst(pen, w, h, clr):
    jump(pen, -w/2-5, -h/2-5)
    pen.pencolor(clr)
    pen.width(10)
    pen.fd(w+10)
    pen.lt(90)
    pen.fd(h+10)
    pen.lt(90)
    pen.fd(w+10)
    pen.lt(90)
    pen.fd(h+10)
    pen.lt(90)

def mondriaan_01():
    turtle.setup(560,524)
    w,h = 430,430
    turtle.title("Compositie met rood en blauw")

    p.up()
    achtergrond(p, w, h, (.90, .90, .94))
    p.fillcolor("red")
    jump(p, -w/2,-20)
    p.begin_fill()
    p.fd(w*0.45)
    p.lt(90)
    p.fd(h/2+20)
    p.lt(90)
    p.fd(w*0.45)
    p.lt(90)
    p.fd(h/2+20)
    p.end_fill()
    p.lt(90)
    
    p.fillcolor(0, 0, .8)           #donkerblauw
    jump(p, w/2+1,-20)
    p.begin_fill()
    p.rt(90)
    p.fd(h*0.26)
    p.rt(90)
    p.fd(w*0.15)
    p.rt(90)
    p.fd(h*0.26)
    p.rt(90)
    p.fd(w*0.15)
    p.end_fill()

    p.color("black")
    p.width(7)
    line(p, w*0.35,-20, w*0.35,-h/2)            #ver kort
    line(p, -w*0.05,h/2, -w*0.05,-h/2)          #ver lang
    p.width(8)
    line(p, -w*0.05,-h/2+25, w*0.35,-h/2+25)    #hor kort
    line(p, -w/2,-20, w/2,-20)                  #hor lang
    p.width(10)
    line(p, w*0.36,-h*0.26-20, w/2,-h*0.26-20)

    lijst(p, w, h, (.92, .90, .82))

    p.pencolor("gray60")
    jump(p, -w/2+8, -h/2+7)
    p.write("P M  '32", align='left', font=('',5))
    p.ht()

def mondriaan_02():
    turtle.setup(560,524)
    w,h = 430,430
    turtle.title("Compositie met geel en blauw")

    p.up()
    achtergrond(p, w, h, (.90, .90, .94))
    p.fillcolor(.98, .92, 0.16)          #geel
    jump(p, -w/2,-19)
    p.begin_fill()
    p.fd(w*0.43)
    p.lt(90)
    p.fd(h/2+19)
    p.lt(90)
    p.fd(w*0.43)
    p.lt(90)
    p.fd(h/2+19)
    p.end_fill()
    p.lt(90)
    
    p.fillcolor(0, 0, .8)           #donkerblauw
    jump(p, w/2+1,-20)
    p.begin_fill()
    p.rt(90)
    p.fd(h*0.26)
    p.rt(90)
    p.fd(w*0.18)
    p.rt(90)
    p.fd(h*0.26)
    p.rt(90)
    p.fd(w*0.18)
    p.end_fill()

    p.color("black")
    p.width(8)
    line(p, -w/2,-19, w/2,-19)                  #hor lang
    line(p, -w*0.06,-h/2+23, w*0.32,-h/2+23)    #hor kort
    p.width(7)
    line(p, -w*0.07,h/2, -w*0.07,-h/2)          #ver lang
    line(p, w*0.324,-20, w*0.324,-h/2)          #ver kort
    p.width(14)
    line(p, w*0.33,-h*0.26-18, w/2,-h*0.26-18)

    lijst(p, w, h, (.92, .90, .82))

    p.pencolor("gray60")
    jump(p, w/2-2, -h/2+4)
    p.write("P    M   32", align='right', font=('',5))
    p.ht()

def mondriaan_03():
    turtle.setup(560,524)
    w,h = 430,430
    turtle.title("Compositie met dubbele lijn en geel en grijs")

    p.up()
    achtergrond(p, w, h, (.90, .90, .94))
    p.fillcolor(.98, .92, 0.16)          #geel
    jump(p, -w/2,-36)
    p.begin_fill()
    p.fd(w*0.5)
    p.lt(90)
    p.fd(h/2+36)
    p.lt(90)
    p.fd(w*0.5)
    p.lt(90)
    p.fd(h/2+36)
    p.end_fill()
    p.lt(90)
    
    p.fillcolor(.86, .86, .84)           #grijs
    jump(p, w/2+1,-46)
    p.begin_fill()
    p.rt(90)
    p.fd(h*0.17)
    p.rt(90)
    p.fd(w*0.1)
    p.rt(90)
    p.fd(h*0.17)
    p.rt(90)
    p.fd(w*0.1)
    p.end_fill()

    p.color("black")
    p.width(7)
    line(p, 0,h/2, 0,-h/2)                  #ver lang
    line(p, w*0.4,-48, w*0.4,-h/2)          #ver kort
    p.width(8)
    line(p, 0,-h/2+16, w*0.4,-h/2+16)       #hor kort
    p.width(12)
    line(p, w*0.41,-h*0.26-11, w/2,-h*0.26-11)

    p.width(3)
    line(p, -w/2,-36, w/2,-36)              #hor lang 1
    line(p, -w/2,-45, w/2,-45)              #hor lang 2

    lijst(p, w, h, (.92, .90, .82))

    p.pencolor("gray60")
    jump(p, -w/2+8, -h/2+7)
    p.write("P M  '32", align='left', font=('',5))
    p.ht()
    
def panda():
    def oor(a, b, teken):
        p.up()
        p.setpos(a,b)
        p.seth(teken * 90)
        #p.dot()
        p.down()
        p.begin_fill()
        p.circle(30, teken * 260)
        p.end_fill()

    def oog(a, b, teken):
        p.up()
        p.color("black")
        p.setpos(a, b)
        p.seth(0)
        p.down()
        p.begin_fill()
        p.circle(30)
        p.end_fill()
        p.up()
        p.setpos(a + teken * 8, b + 16)
        p.down()
        p.color("white")
        p.begin_fill()
        p.circle(15)
        p.end_fill()
        p.color("black")
        print(p.heading())
        p.up()
        p.left(90)
        p.forward(2)
        p.right(90)
        p.down()
        p.begin_fill()
        p.circle(5)
        p.end_fill()

    x, y = 0, -60
    strenger = 8
    p.width(2)                      #gezicht
    p.up()
    p.setposition(x, y + strenger)
    p.down()
    p.circle(100)
    oor(x + 50, y + 185, -1)        #re oor
    oor(x - 50, y + 185, 1)         #li oor

    oog(x - 40, y + 90, 1)          #li oog
    oog(x + 40, y + 90, -1)         #re oog

    p.up()                      #neus
    p.setpos(x, y + 50)
    p.down()
    p.begin_fill()
    p.circle(10)
    p.end_fill()

    p.right(90)                 #mond
    p.circle(20, 180)
    p.up()
    p.setpos(x, y + 50)
    p.down()
    p.circle(20, -180)
    p.ht()

def vrij_tekenen():
    hk = 90
    afst = 5
    iswisser = False

    def doPosClick(x,y):
        #print(x,y)
        isdown = p.isdown()
        p.up()
        p.setpos(x,y)
        if isdown:
            p.down()
        
    def doUpDown():
        #print("doUpDown")
        if p.isdown():
            p.up()
        else:
            p.down()
    def doWisser():
        if p.shape() == "classic":
            p.shape("turtle")
            p.pencolor("white")
        else:
            p.shape("classic")
            p.pencolor("black")
    def doDikte():
        d = turtle.numinput("Vrij tekenen", "Dikte [1-10]:", default=p.width(), minval=1, maxval=10)
        if d:
            p.width(d)
        turtle.listen()             #screen opnieuw focus geven
    def dikker():
        d = p.width()
        if d < 10:
            d += 1
            p.width(d)
    def dunner():
        d = p.width()
        if d > 1:
            d -= 1
            p.width(d)
    def doHoek():
        nonlocal hk
        d = turtle.numinput("Vrij tekenen", "Hoek [10-90]:", default=hk, minval=10, maxval=90)
        if d:
            hk = int(d)
        turtle.listen()
    def groter():
        nonlocal hk
        hk += 10
        if hk > 90: hk = 90
    def kleiner():
        nonlocal hk
        hk -= 10
        if hk < 10: hk = 10
    def doAfstand():
        nonlocal afst
        d = turtle.numinput("Vrij tekenen", "Afstand [1-50]:", default=afst, minval=1, maxval=50)
        if d:
            afst = int(d)
        turtle.listen()
    def versnel():
        nonlocal afst
        if afst < 50: afst += 1
    def vertraag():
        nonlocal afst
        if afst > 1: afst -= 1

    def doEscape():
        nonlocal hk, afst
        hk = 90
        afst = 5
        p.width(1)
        p.setheading(0)
    def doReset():
        if messagebox.askyesno("Vrij tekenen", "Tekening wissen?"):
            turtle.resetscreen()
    def doQuit():
        if messagebox.askyesno("Vrij tekenen", "Afsluiten?"):
            turtle.bye()
    def doKleur():
        clr = colorchooser.askcolor()
        if clr[1]:
            p.pencolor(clr[1])          #2e item is color str

    turtle.onscreenclick(doPosClick)
    # vlg doet: self.cv.bind("<KeyPress-Left>", fun)
    # ->Control-key werkt niet, want moet voor Keypress
    turtle.onkeypress(lambda : p.left(hk), "Left")
    turtle.onkeypress(lambda : p.right(hk), "Right")
    turtle.onkeypress(lambda : p.forward(afst), "Up")
    turtle.onkeypress(lambda : p.backward(afst), "Down")
    turtle.onkeypress(doUpDown, "Return")       #moet hfdlet
    turtle.onkeypress(doWisser, "space")        #moet kl let
    # de vlg keys zijn hfdlet gevoelig, dus "D" werkt alleen bij Shift+d
    turtle.onkeypress(doDikte, "d")
    turtle.onkeypress(doAfstand, "a")
    turtle.onkeypress(doHoek, "h")
    turtle.onkeypress(doKleur, "k")

    turtle.onkeypress(versnel, "=")             #afstand bij p.forward()
    turtle.onkeypress(vertraag, "minus")        #moet kl let
    turtle.onkeypress(groter, "0")              #hoek
    turtle.onkeypress(kleiner, "9")
    turtle.onkeypress(dikker, "8")              #lijndikte
    turtle.onkeypress(dunner, "7")

    turtle.onkeypress(lambda : p.dot(), "p")
    turtle.onkeypress(lambda : p.undo(), "u")
    turtle.onkeypress(doEscape, "Escape")
    turtle.onkeypress(doReset, "r")
    turtle.onkeypress(doQuit, "q")

    turtle.listen()


#--- script ---

#test_status()
#test_input()
#test_cirkel()

#vierkant_01()
#ster_01()
#ster_02()
#cirkels_01()
#patroon_01()
#patroon_02()
#patroon_03()

#fractal_tree_01()

#functie_01()
#functie_02()
#functie_03()
#functie_04()

#mondriaan_01()
#mondriaan_02()
mondriaan_03()

#panda()
#vrij_tekenen()

#turtle.exitonclick()   #blocking ->moet aan einde script
#turtle.mainloop()      #niet in IDLE, blocking ->geen >>> na einde tekening
#turtle.bye()           #window sluiten

