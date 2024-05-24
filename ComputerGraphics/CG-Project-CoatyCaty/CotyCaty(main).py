from turtle import *
from time import *
import random
import math
import pygame


def fight():
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


def Maze():
    wn = Screen()
    wn.bgcolor("black")
    wn.title("A maze game")
    wn.setup(700, 700)

    images=["cat_right_small.gif",
            "cat_left_small.gif",
            r"tre_small.gif",
            "m2.gif",
            "m2_left.gif"]
    for image in images:
        register_shape(image)

    class pen(Turtle):
        def __init__(self):
            Turtle.__init__(self)
            self.shape("square")
            self.color("white")
            self.penup()
            self.speed(0)

    class Player(Turtle):
        def __init__(self):
            Turtle.__init__(self)
            self.shape("cat_right_small.gif")
            self.color("blue")
            self.penup()
            self.speed(0)
            self.gold = 0

        def go_down(self):
            move_to_x = self.xcor()
            move_to_y = self.ycor() - 24

            if (move_to_x, move_to_y) not in wall:
                self.goto(move_to_x, move_to_y)

        def go_up(self):
            move_to_x = self.xcor()
            move_to_y = self.ycor() + 24

            if (move_to_x, move_to_y) not in wall:
                self.goto(move_to_x, move_to_y)

        def go_right(self):
            move_to_x = self.xcor() + 24
            move_to_y = self.ycor()
            self.shape("cat_right_small.gif")
            if (move_to_x, move_to_y) not in wall:
                self.goto(move_to_x, move_to_y)

        def go_left(self):
            move_to_x = self.xcor() - 24
            move_to_y = self.ycor()
            self.shape("cat_left_small.gif")
            if (move_to_x, move_to_y) not in wall:
                self.goto(move_to_x, move_to_y)

        def is_collision(self, other):
            a = self.xcor() - other.xcor()
            b = self.ycor() - other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2))
            if distance < 5:
                return True
            else:
                return False

    class Enemy(Turtle):
        def __init__(self, x, y):
            Turtle.__init__(self)
            self.shape("m2.gif")
            self.color("red")
            self.penup()
            self.speed(0)
            self.gold = 25
            self.goto(x, y)
            self.direction = random.choice(["up", 'right', 'down', 'left'])

        def move(self):
            if self.direction == "up":
                dx = 0
                dy = 24
            elif self.direction == "down":
                dx = 0
                dy = -24
            elif self.direction == "right":
                dx = 24
                dy = 0
                self.shape("m2_left.gif")
            elif self.direction == "left":
                dx = -24
                dy = 0
                self.shape("m2.gif")
            else:
                dx = 0
                dy = 0

            if self.is_close(player):
                if player.xcor() < self.xcor():
                    self.direction = "left"
                elif player.xcor() > self.xcor():
                    self.direction = "right"
                elif player.ycor() < self.ycor():
                    self.direction = "down"
                elif player.ycor() > self.ycor():
                    self.direction = "up"

            move_to_x = self.xcor() + dx
            move_to_y = self.ycor() + dy

            if (move_to_x, move_to_y) not in wall:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(["up", 'right', 'down', 'left'])

            ontimer(self.move, t=random.randint(100, 300))

        def is_close(self, other):
            a = self.xcor() - other.xcor()
            b = self.ycor() - other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2))
            if distance < 75:
                return True
            else:
                return False

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    class Treasure(Turtle):
        def __init__(self, x, y):
            Turtle.__init__(self)
            self.shape(r"tre_small.gif")
            self.color("gold")
            self.penup()
            self.speed(0)
            self.gold = 100
            self.goto(x, y)

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    levels = [""]
    level_1 = [
        "XXXXXXXXXXXXXXXXXXXXXXXX",
        "XP XXXXXXX        TXXXXX",
        "X  XXXXXXX  XXXXX  XXXXX",
        "X       XX  XX     XXXXX",
        "X       XX  XX     XXXXX",
        "XXXXXX        XXXX EXXXX",
        "XXXXXX  XXXXXXXXXXXXXXXX",
        "X         XXXXXXXXXXXXXX",
        "X             EXXXXXXXXX",
        "XXXXXXXXX      XXXXXX  X",
        "XXXXXXXXXXXXX  XXXXXX  X",
        "XXX  XXXXXXXX          X",
        "XXX                   EX",
        "XXX            XXXXXXXXX",
        "XXXXXXXXXXXX   XXXXXXXXX",
        "XXXXXXXXXXXX           X",
        "XX   TXXXXXX           X",
        "XX    XXXXXXXXXXX  XXXXX",
        "XX     XXXXXXXXXX  XXXXX",
        "XX       EXXXXX        X",
        "XXX                    X",
        "XXXXXXXXXXXXXXXXXXXXXXXX",
    ]
    levels.append(level_1)
    treasures = []
    enemies = []

    def setup_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)

                if character == "X":
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                    wall.append((screen_x, screen_y))
                if character == "P":
                    player.goto(screen_x, screen_y)
                if character == "T":
                    treasures.append(Treasure(screen_x, screen_y))
                if character == "E":
                    enemies.append(Enemy(screen_x, screen_y))

    pen = pen()
    player = Player()
    wall = []
    setup_maze(levels[1])

    listen()
    onkeypress(player.go_left, "a")
    onkeypress(player.go_right, "d")
    onkeypress(player.go_up, "w")
    onkeypress(player.go_down, "s")
    wn.tracer(0)

    for enemy in enemies:
        ontimer(enemy.move, t=250)

    while True:
        for treasure in treasures:
            if player.is_collision(treasure):
                player.gold += treasure.gold
                print(player.gold)
                treasure.destroy()
                treasures.remove(treasure)

        for enemy in enemies:
            if player.is_collision(enemy):
                print("player died")

        wn.update()

    wn.mainloop()


def sky():
    pygame.init()
    cat_sound=pygame.mixer.Sound(r"Cat.wav")
    dog_sound=pygame.mixer.Sound(r"Dog.wav")
    images=["cat_right_small.gif",
            "cat_left_small.gif",
            r"milk.gif",
            r"dog.gif",
            r"background.gif"]

    for img in images:
        register_shape(img)

    score = 0
    wn1 = Screen()
    wn1.setup(width=700, height=500)
    wn1.title("Cat Sky Game")
    wn1.bgcolor("green")
    wn1.bgpic(r"background.gif")
    wn1.tracer(0)

    class Cat(Turtle):
        def __init__(self):
            Turtle.__init__(self)
            self.speed(0)
            self.shape("cat_left_small.gif")
            self.color("white")
            self.penup()
            self.goto(0, -200)
            self.direction = "left"

    class Milk(Turtle):
        def __init__(self):
            Turtle.__init__(self)
            self.speed(0)
            self.shape(r"milk.gif")
            self.color("white")
            self.penup()
            x = random.randint(-300, 300)
            self.goto(x, 200)
            self.ss = random.choice([0.5, 0.6, 0.7, 0.8, 0.3, 0.4, 0.2])

    class Dog(Turtle):
        def __init__(self):
            Turtle.__init__(self)
            self.speed(0)
            self.shape(r"dog.gif")
            self.color("red")
            self.penup()
            x = random.randint(-300, 300)
            self.goto(x, 200)
            self.ss = random.choice([0.5, 0.6, 0.7, 0.8, 0.3, 0.4, 0.2])

    pen = Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.shape("square")
    pen.color('black')
    pen.penup()
    pen.goto(0, 210)
    pen.write(f"Score {score}", align="center", font=("Courier", 16, "normal"))

    def print_new_results(score):
        pen.clear()
        pen.write(f"Score {score}", align="center", font=("Courier", 16, "normal"))

    cat = Cat()
    milks = []
    dogs = []
    for _ in range(8):
        milks.append(Milk())
    for _ in range(8):
        dogs.append(Dog())

    def left():
        cat.shape("cat_left_small.gif")
        cat.direction = 'left'

    def right():
        cat.shape("cat_right_small.gif")
        cat.direction = 'right'

    wn1.listen()
    wn1.onkeypress(left, "a")
    wn1.onkeypress(right, 'd')

    while True:
        if cat.direction == "left":
            if cat.xcor() < -320:
                cat.setx(cat.xcor())
            else:
                cat.setx(cat.xcor() - 0.5)
        if cat.direction == "right":
            if cat.xcor() > 320:
                cat.setx(cat.xcor())
            else:
                cat.setx(cat.xcor() + 0.5)

        for milk in milks:
            milk.sety(milk.ycor() - milk.ss)
            if milk.ycor() < -250:
                x = random.randint(-300, 300)
                milk.goto(x, 230)

            if milk.distance(cat) < 30:
                cat_sound.play()
                x = random.randint(-300, 300)
                milk.goto(x, 230)
                score += 10
                print_new_results(score)

        for dog in dogs:
            dog.sety(dog.ycor() - dog.ss)
            if dog.ycor() < -250:
                x = random.randint(-300, 300)
                dog.goto(x, 230)

            if dog.distance(cat) < 30:
                dog_sound.play()
                x = random.randint(-300, 300)
                dog.goto(x, 230)
                score -= 10
                print_new_results(score)
        wn1.update()

    wn1.mainloop()


def main():
    win = Screen()
    win.bgpic(r"main_background.gif")
    register_shape("cat-air.gif")
    win.setup(1000, 500)

    t1 = Turtle()
    t1.penup()
    t1.shape("circle")
    t1.shapesize(10)
    t1.speed(0)

    t2 = Turtle()
    t2.penup()
    t2.shape("circle")
    t2.shapesize(10)
    t2.setx(-300)
    t2.speed(0)

    t3 = Turtle()
    t3.penup()
    t3.shape("circle")
    t3.shapesize(10)
    t3.setx(300)
    t3.speed(0)

    t = Turtle()
    t.shape("cat-air.gif")
    t.color("red")
    t.penup()
    t.goto(0, -200)
    t.speed(0)
    t.direction = "stop"


    def up():
        t.goto(t.xcor(), t.ycor() + 20)

    def down():
        t.goto(t.xcor() + 20, t.ycor() - 20)

    def left():
        t.goto(t.xcor() - 20, t.ycor())

    def right():
        t.goto(t.xcor() + 20, t.ycor())

    win.listen()

    win.onkeypress(up, "w")
    win.onkeypress(down, "s")
    win.onkeypress(left, "a")
    win.onkeypress(right, "d")

    while True:
        win.update()
        sleep(0.1)

        if t.distance(t1) <= 50:
            win.clear()
            fight()
        elif t.distance(t2) <= 50:
            win.clear()
            Maze()
        elif t.distance(t3) <= 50:
            win.clear()
            sky()


main()
