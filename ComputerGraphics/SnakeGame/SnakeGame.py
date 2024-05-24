import turtle
import time
import random

images=[r"D:\SnakeGame\SnakeGame\22.gif"]
for img in images:
    turtle.register_shape(img)
delay=0.105

score=0
high_score=0

wn=turtle.Screen()
wn.title("Snake Game by Ahlam")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

food=turtle.Turtle()
food.speed(0)
food.shape(r"D:\SnakeGame\SnakeGame\22.gif")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score=0   Highest Score=0",align="center",font=("Courier",24,"normal"))



#functions
def move():
    if head.direction=="up":
        head.sety(head.ycor()+20)
    elif head.direction=="down":
        head.sety(head.ycor()-20)
    elif head.direction=="left":
        head.setx(head.xcor()-20)
    elif head.direction=="right":
        head.setx(head.xcor()+20)


def move_up():
    if head.direction!="down":
        head.direction="up"


def move_down():
    if head.direction != "up":
        head.direction="down"


def move_right():
    if head.direction != "left":
        head.direction="right"


def move_left():
    if head.direction != "right":
        head.direction="left"


def lose():
    pen.clear()
    pen.write(f"Score={score}   Highest Score={high_score}",align="center",font=("Courier",24,"normal"))


wn.listen()
wn.onkeypress(move_up,'w')
wn.onkeypress(move_down,'s')
wn.onkeypress(move_right,'d')
wn.onkeypress(move_left,'a')




while True:
    wn.update()
    #if he get into the board
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #delete the rest of the body(start the game again from zero)
        for s in segments:
            s.goto(100000,10000)
        segments=[]
        score = 0
        lose()

    if head.distance(food)<20:
        food.goto(random.randint(-290,290),random.randint(-290,290))

        segment=turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("grey")
        segment.penup()
        segments.append(segment)

        #update the score
        score+=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write(f"Score={score}   Highest Score={high_score}",align="center",font=("Courier",24,"normal"))


    # for the body movement
    for i in range(len(segments)-1,0,-1):
        #each one will move to the prevous place (كل وحدة بتتحرك مكان اللي قلبها )
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    #if the head get into the body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for s in segments:
                s.goto(100000, 10000)
            segments = []
            score = 0
            lose()

    time.sleep(delay)



wn.mainloop()
