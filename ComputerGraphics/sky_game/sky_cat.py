import turtle
import random
import pygame

pygame.init()
cat_sound=pygame.mixer.Sound(r"Cat.wav")
dog_sound=pygame.mixer.Sound(r"Dog.wav")
images=["cat_right_small.gif",
        "cat_left_small.gif",
        r"milk.gif",
        r"dog.gif",
        r"background.gif"]

for img in images:
    turtle.register_shape(img)

score=0
# lives=3

wn=turtle.Screen()
wn.setup(width=700,height=500)
wn.title("Cat Sky Game")
wn.bgcolor("green")
wn.bgpic(r"background.gif")
wn.tracer(0)

class Cat(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("cat_left_small.gif")
        self.color("white")
        self.penup()
        self.goto(0, -200)
        self.direction = "left"

class Milk(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape(r"milk.gif")
        self.color("white")
        self.penup()
        x = random.randint(-300, 300)
        self.goto(x, 200)
        self.ss = random.choice([0.5, 0.6, 0.7,0.8,0.3,0.4,0.2])

class Dog(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape(r"dog.gif")
        self.color("red")
        self.penup()
        x = random.randint(-300, 300)
        self.goto(x, 200)
        self.ss = random.choice([0.5, 0.6, 0.7,0.8,0.3,0.4,0.2])

pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color('black')
pen.penup()
pen.goto(0,210)
pen.write(f"Score {score}",align="center",font=("Courier",16,"normal"))

def print_new_results(score):
    pen.clear()
    pen.write(f"Score {score}", align="center", font=("Courier", 16, "normal"))


cat=Cat()
milks=[]
dogs=[]
for _ in range(8):
    milks.append(Milk())
for _ in range(8):
    dogs.append(Dog())


def left():
    cat.shape("cat_left_small.gif")
    cat.direction='left'
def right():
    cat.shape("cat_right_small.gif")
    cat.direction='right'

wn.listen()
wn.onkeypress(left,"a")
wn.onkeypress(right,'d')

while True:
    if cat.direction=="left":
        if cat.xcor()<-320:
            cat.setx(cat.xcor())
        else:
            cat.setx(cat.xcor()-0.5)
    if cat.direction=="right":
        if cat.xcor()>320:
            cat.setx(cat.xcor())
        else:
            cat.setx(cat.xcor() + 0.5)

    for milk in milks:
        milk.sety(milk.ycor()-milk.ss)
        if milk.ycor()<-250:
            x=random.randint(-300,300)
            # y=random.randint(0,300)
            milk.goto(x,230)

        if milk.distance(cat)<30:
            cat_sound.play()
            x = random.randint(-300, 300)
            # y = random.randint(0, 250)
            milk.goto(x, 230)
            score+=10
            print_new_results(score)

    for dog in dogs:
        dog.sety(dog.ycor()-dog.ss)
        if dog.ycor()<-250:
            x=random.randint(-300,300)
            # y=random.randint(0,300)
            dog.goto(x,230)

        if dog.distance(cat)<30:
            dog_sound.play()
            x = random.randint(-300, 300)
            # y = random.randint(0, 250)
            dog.goto(x, 230)
            # lives-=1
            score-=10
            print_new_results(score)
    wn.update()

wn.mainloop()