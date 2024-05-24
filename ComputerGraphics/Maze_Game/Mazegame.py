import math
import random
import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("A maze game")
wn.setup(700,700)

images=["cat_right_small.gif",
        "cat_left_small.gif",
        r"tre_small.gif",
        "m2.gif",
        "m2_left.gif"]
for image in images:
    turtle.register_shape(image)


class pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("cat_right_small.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold=0
    def go_down(self):
        move_to_x=self.xcor()
        move_to_y=self.ycor()-24

        if (move_to_x,move_to_y) not in wall:
            self.goto(move_to_x,move_to_y)
    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()+24

        if (move_to_x, move_to_y) not in wall:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()
        self.shape("cat_right_small.gif")
        if (move_to_x, move_to_y) not in wall:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        self.shape("cat_left_small.gif")
        if (move_to_x, move_to_y) not in wall:
            self.goto(move_to_x, move_to_y)

    def is_collision(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=math.sqrt((a**2)+(b**2))
        if distance<5:
            return True
        else:
            return False
class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("m2.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction=random.choice(["up",'right','down','left'])


    def move(self):
        if self.direction=="up":
            dx=0
            dy=24
        elif self.direction=="down":
            dx=0
            dy=-24
        elif self.direction=="right":
            dx=24
            dy=0
            self.shape("m2_left.gif")
        elif self.direction=="left":
            dx=-24
            dy=0
            self.shape("m2.gif")
        else:
            dx=0
            dy=0


        if self.is_close(player):
            if player.xcor()<self.xcor():
                self.direction="left"
            elif player.xcor()>self.xcor():
                self.direction = "right"
            elif player.ycor()<self.ycor():
                self.direction = "down"
            elif player.ycor()>self.ycor():
                self.direction="up"

        move_to_x=self.xcor()+dx
        move_to_y=self.ycor()+dy

        if (move_to_x,move_to_y) not in wall:
            self.goto(move_to_x,move_to_y)
        else:
            self.direction = random.choice(["up", 'right', 'down', 'left'])

        turtle.ontimer(self.move,t=random.randint(100,300))

    def is_close(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=math.sqrt((a**2)+(b**2))
        if distance<75:
            return True
        else:
            return False


    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(r"tre_small.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold=100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

levels=[""]
level_1=[
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
treasures=[]
enemies=[]
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character=level[y][x]
            screen_x=-288+(x*24)
            screen_y=288-(y*24)

            if character=="X":
                pen.goto(screen_x,screen_y)
                pen.stamp()
                wall.append((screen_x,screen_y))
            if character=="P":
                player.goto(screen_x,screen_y)
            if character=="T":
                treasures.append(Treasure(screen_x,screen_y))
            if character=="E":
                enemies.append(Enemy(screen_x,screen_y))

pen=pen()
player=Player()
wall=[]
setup_maze(levels[1])

turtle.listen()
turtle.onkeypress(player.go_left,"a")
turtle.onkeypress(player.go_right,"d")
turtle.onkeypress(player.go_up,"w")
turtle.onkeypress(player.go_down,"s")
wn.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move,t=250)

while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold+=treasure.gold
            print(player.gold)
            treasure.destroy()
            treasures.remove(treasure)

    for enemy in enemies:
        if player.is_collision(enemy):
            print("player died")

    wn.update()

wn.mainloop()

