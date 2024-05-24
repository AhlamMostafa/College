import turtle
import random
wn=turtle.Screen()
wn.setup(700,700)
wn.bgcolor("lightblue")

pen=turtle.Turtle()
pen.speed(0)
pen.color("black",'green')



def mm(steps,direction):
    x1=-350
    tall = [100, 150, 200, 250, 285, 220, 230, 245,130,210,270]
    for i in range(5):
        if direction=="up":
            pen.begin_fill()
            steps=random.choice(tall)
            pen.penup()
            pen.goto(x1, 350)
            pen.pd()
            pen.fd(100)
            pen.right(90)
            pen.fd(steps)
            pen.right(90)
            pen.fd(100)
            pen.right(90)
            pen.fd(steps)
            pen.right(90)
            pen.end_fill()
            x1+=150
        else:
            pen.begin_fill()
            steps=random.choice(tall)
            pen.penup()
            pen.goto(x1, -350)
            pen.pd()
            pen.fd(100)
            pen.left(90)
            pen.fd(steps)
            pen.left(90)
            pen.fd(100)
            pen.left(90)
            pen.fd(steps)
            pen.left(90)
            pen.end_fill()
            x1+=150

tall=[50,100,150,200,250,285,220,230,245,75,98,130]

mm(random.choice(tall),'up')
mm(random.choice(tall), 'down')

turtle.done()
