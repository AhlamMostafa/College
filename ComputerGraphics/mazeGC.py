# maze task
import turtle
import random
wn=turtle.Screen()
wn.setup(700,700)
wn.bgcolor("lightgreen")

pen=turtle.Turtle()
pen.color("black")
pen.penup()
pen.width(10)
pen.goto(-300,300)
pen.down()
pen.speed(10)
pen.fd(300)
pen.up()
pen.fd(100)
pen.down()
pen.fd(200)
pen.right(90)
pen.fd(600)
pen.right(90)
pen.fd(500)
pen.up()
pen.fd(100)
pen.down()
pen.right(90)
pen.fd(600)

pen.up()
pen.goto(-300,200)
pen.pd()
pen.right(90)
pen.fd(200)
pen.right(90)
pen.fd(200)

pen.up()
pen.goto(-0,300)
pen.pd()
pen.fd(200)
pen.left(90)
pen.fd(100)

pen.up()
pen.goto(100,300)
pen.pd()
pen.right(90)
pen.fd(100)

pen.up()
pen.goto(200,200)
pen.pd()
pen.fd(200)
pen.left(90)
pen.fd(100)

pen.up()
pen.goto(-200,-200)
pen.pd()
pen.fd(400)
pen.left(90)
pen.fd(100)

pen.up()
pen.goto(-200,0)
pen.pd()
pen.left(180)
pen.fd(200)

pen.up()
pen.goto(-100,-200)
pen.pd()
pen.fd(100)

pen.up()
pen.goto(0,100)
pen.pd()
pen.fd(200)


pen.up()
pen.goto(100,100)
pen.pd()
pen.fd(200)

pen.hideturtle()

images=["D:\Maze_Game\cat_right_small.gif"]
for image in images:
    turtle.register_shape(image)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("D:\Maze_Game\cat_right_small.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
    def go_down(self):
        move_to_x=self.xcor()
        move_to_y=self.ycor()-24
        self.goto(move_to_x, move_to_y)
    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()+24
        self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()
        self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        self.goto(move_to_x, move_to_y)

player=Player()
player.goto(50,300)
turtle.listen()
turtle.onkeypress(player.go_left,"a")
turtle.onkeypress(player.go_right,"d")
turtle.onkeypress(player.go_up,"w")
turtle.onkeypress(player.go_down,"s")
wn.tracer(0)

while True:
    wn.update()
turtle.done()