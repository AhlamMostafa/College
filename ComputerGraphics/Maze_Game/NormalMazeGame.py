import math
import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("A maze game")
wn.setup(700,700)

images=["D:\Maze_Game\cat_right_small.gif",
        "D:\Maze_Game\cat_left_small.gif",
        "D:\Maze_Game\home.gif"]
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
        self.shape("D:\Maze_Game\cat_right_small.gif")
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
        self.shape("D:\Maze_Game\cat_right_small.gif")
        if (move_to_x, move_to_y) not in wall:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        self.shape("D:\Maze_Game\cat_left_small.gif")
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

class Home(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("D:\Maze_Game\home.gif")
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
"XPXXXXXXXXXXXXXXXXXXXXXX",
"X       XX         XXXXX",
"X XXXXXXXX  XXXXX     XX",
"X           XXXXX  XX XX",
"X XXXXXXXX  XX     XX XX",
"X XXXX   X  X  XXX XX XX",
"X XXXX   XXXX  XXX XXXXX",
"XXX      XXXX  XXX XXXXX",
"X              XXX XXXXX",
"XXX XXXXX XXXXXXXX     X",
"XXX XXXXX XXX  XXXXXX  X",
"XXX XXXXX XXX    XXXX  X",
"XXX    XXXXXX    XXXX  X",
"XXXXX          XXXXXXXXX",
"XXXXXXXXXXXX   XXXXXXXXX",
"XXXXXXXXXXXX   XXXXXXXXX",
"XX                     X",
"XX  XXXXX  XXXXX  XXXXXX",
"XX  XXXXX  XXXXX  XXXXXX",
"XXXXXXXXX  XXXXXXXXXXXXX",
"XXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXHX",
]
levels.append(level_1)
homes=[]

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
            if character=="H":
                homes.append(Home(screen_x,screen_y))




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


while True:
    for home in homes:
        if player.is_collision(home):
            print("You Win")
            home.destroy()
            homes.remove(home)

    wn.update()

wn.mainloop()

