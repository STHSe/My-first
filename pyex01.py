# -*- coding: cp949 -*-
import turtle
import math
import sys

global scoreCount
scoreCount = 0

player = turtle.Turtle()
box = turtle.Turtle()
score = turtle.Turtle()
screen = player.getscreen()

def printScore():
    global scoreCount
    score.clear()
    score.hideturtle()
    score.penup()
    score.goto(0, 330)
    scoreString = "Score: %s" % scoreCount
    score.write(scoreString, False, align="center", font=("Arial", 18, "bold"))

def draw():
    mypen = turtle.Turtle()
    mypen.penup()
    mypen.goto(-300, 300)
    mypen.pendown()
    mypen.pensize(5)
    mypen.speed(100)

    for i in range(4):
        mypen.forward(600)
        mypen.right(90)
    mypen.hideturtle()

def reset():
    sys.stdout.flush()
    player.penup()
    player.goto(-290, -290)
    player.setheading(0)
    player.pendown()
    player.clear()
    printScore()

def turnLeft():
    player.left(5)
    sys.stdout.flush()

def turnRight():
    player.right(5)
    sys.stdout.flush()

def fire():
    global scoreCount
    x = -290
    y = -290
    velocity = 50

    angle = player.heading()
    vx = velocity * math.cos(angle * 3.14 / 180.0)
    vy = velocity * math.sin(angle * 3.14 / 180.0)
    while player.ycor() >= -290:
        vx = vx
        vy = vy - 4
        x = x + vx
        y = y + vy
        player.goto(x, y)
        d = math.sqrt( math.pow((player.xcor()) - (box.xcor()), 2) + math.pow((player.ycor()) - (box.ycor()), 2))
        if (d < 15):
            scoreCount += 1
            break
        if player.xcor() > 300 or player.xcor() < -300:
            reset()
            break
        if player.ycor() > 300 or player.ycor() < -300:
            reset()
            break
    reset()
    draw()
        
#======================================

player.shape("turtle")
box.shape("square")

box.penup()
box.goto(280, -280)
box.color("red")

player.penup()
player.pensize(5)
player.goto(-290, -290)
player.setheading(0)
player.pendown()
    
draw()
printScore()

while True:
    sys.stdout.flush()
    screen.onkeypress(turnLeft, "Left")
    screen.onkeypress(turnRight, "Right")
    screen.onkeypress(fire, "space")
    screen.listen()

    turtle.mainloop()         