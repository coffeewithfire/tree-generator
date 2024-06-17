import turtle
from random import choice, randint


# turtle setup
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0)
turtle.penup()
turtle.setposition(0, -450)
turtle.setheading(randint(85, 95))
turtle.pendown()

thick = 17
turtle.pensize(thick)


#l system rules
axiom = '222220'

itr = 13
angle = 15
length = 15

ts = {"1": "21",
      "0": "1[+20]-20"}

for _ in range(itr):
    axiom = axiom.translate(str.maketrans(ts))




RED = ["#E09F3E", "#9E2A2B", "#540B0E"]
GREEN = ["#009933", "#669900", "#20BB00"]
PINK = ["#FFB7C5", "#FFD1DA", "#733746"]
curColor = choice([RED, GREEN, PINK])


stk = []

for c in axiom:
    if c == "0":
        if randint(0,2):
            turtle.pensize(8)
            turtle.pencolor(curColor[randint(0,2)])
            turtle.forward(length - 3)
            turtle.pensize(thick)
            turtle.pencolor("#000000")
        else:
            turtle.forward(length)
    elif c == "1":
        if randint(0, 9) > 6:
            turtle.forward(length * 1.5)
    elif c == "2":
        if randint(0, 9) > 2:
            turtle.forward(length * .7)
    elif c == "+":
        turtle.right(angle + randint(-10, 10))
    elif c == "-":
        turtle.left(angle + randint(-10, 10))
    elif c == "[":
        thick *= .75
        turtle.pensize(thick)
        x = turtle.xcor()
        y = turtle.ycor()
        ang = turtle.heading()
        stk.append((x, y, ang, thick))
    elif c == "]":
        x, y, ang, thick = stk.pop()
        turtle.penup()
        turtle.setposition(x, y)
        turtle.setheading(ang)
        turtle.pensize(thick)
        turtle.pendown()

turtle.update()
turtle.done()