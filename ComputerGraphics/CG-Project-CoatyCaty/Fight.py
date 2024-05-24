from turtle import *
from time import *
import random
import math

score = 0

wind = Screen()
wind.setup(1000, 600)

cloud = Turtle()
cloud.speed(0)
cloud.penup()
cloud.goto(-340, 200)
cloud.shape("circle")
cloud.color("light blue")
cloud.shapesize(5)

for i in range(4):
    cloud.stamp()
    cloud.fd(60)
cloud.fd(340)
for i in range(3):
    cloud.stamp()
    cloud.fd(60)

register_shape(r"Cat_Bigger.gif")
register_shape(r"Garbage.gif")

pen = Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0, 150)
pen.speed(0)
pen.pencolor("Black")
pen.pensize(30)
pen.write("Score: 0  ", align="center", font=[50])

p = Turtle()
p.penup()
p.hideturtle()
p.goto(0, 0)
p.speed(0)
p.pencolor("Red")
p.pensize(30)

bin = Turtle()
bin.penup()
bin.hideturtle()
bin.goto(520, -110)
bin.showturtle()
bin.seth(180)
bin.shape(r"Garbage.gif")
bin.dx = -5

ground = Turtle()
ground.hideturtle()
ground.penup()
ground.speed(0)
ground.setposition(500, -200)
ground.seth(180)
ground.pendown()
ground.pensize(4)
ground.fd(1400)

cat = Turtle()
cat.hideturtle()
cat.penup()
cat.shape(r"Cat_Bigger.gif")
cat.setposition(-310, -180)
cat.showturtle()
cat.speed(0)
cat.state = "Yes"
cat.dy = 0

boo = False

def up():
    if cat.state == "Yes":
        cat.dy = 13
        cat.state = "NO"

wind.listen()
wind.onkeypress(up, "space")
x = 0
while True:
    cat.dy -= 0.5

    cat.sety(cat.dy + cat.ycor())

    if cat.ycor() <= -180:
        cat.sety(-180)
        cat.dy = 0
        cat.state = "Yes"

    if boo == False:
        if bin.xcor() < -490:
            bin.hideturtle()
            bin.setx(520)
            bin.showturtle()
            x = 0
        else:
            bin.fd(5)
            x += 1

    if (cat.xcor() >= bin.xcor() - 55 and cat.xcor() <= bin.xcor() + 60) and cat.ycor() <= -70:
        bin.stamp()
        cat.stamp()
        bin.hideturtle()
        boo = True
        pen.clear()
        pen.write(f"Score:{score}", align="center", font=[50])
        p.write("GAME OVER", align="center", font=["bold", 70])
    else:
        score += 1
        pen.clear()
        pen.write(f"Score:{score} ", align="center", font=[50])

    wind.update()
wind.mainloop()