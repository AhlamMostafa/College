import turtle
wn=turtle.Screen()
wn.setup(700,700)
pen=turtle.Turtle()
pen.color("black","yellow")
pen.begin_fill()
pen.up()
pen.goto(-310,310)
pen.pd()
pen.fd(50)
pen.right(35)
pen.fd(130)
pen.left(45)
pen.fd(65)
pen.right(40)
pen.fd(130)
pen.left(110)
pen.fd(80)
pen.right(35)
pen.fd(100)
pen.right(110)
pen.fd(100)
pen.right(50)
pen.fd(130)
pen.left(40)
pen.fd(50)
pen.right(30)
pen.fd(20)
pen.left(47)
pen.fd(35)
pen.right(65)
pen.fd(100)
pen.penup()
pen.goto(20,-70)
pen.pd()
pen.left(140)
pen.fd(180)
pen.right(150)
pen.fd(30)
pen.left(130)
pen.fd(30)
pen.right(145)
pen.fd(240)
pen.left(80)
pen.fd(60)
#tail
pen.left(130)
pen.fd(40)

pen.right(45)
pen.fd(30)

pen.left(40)
pen.fd(90)

pen.right(60)
pen.fd(180)

pen.right(90+45)
pen.fd(120)

pen.right(76)
pen.fd(70)

pen.left(76)
pen.fd(40)

pen.right(50)
pen.fd(25)

pen.left(90)
pen.fd(40)

pen.right(70)
pen.fd(55)

pen.left(120)
pen.fd(20)

pen.right(90)
pen.fd(30)

pen.left(115)
pen.fd(50)

pen.right(95)
pen.fd(37)

pen.right(80)
pen.fd(60)
#
# pen.right(80)
# pen.fd(80)
#
pen.right(40)
pen.fd(25)

pen.left(40)
pen.fd(120)

pen.left(30)
pen.fd(120)

xx=pen.xcor()
yy=pen.ycor()
pen.right(40)
pen.fd(50)


pen.right(76)
pen.fd(120)
x=pen.xcor()
y=pen.ycor()

pen.left(110)
pen.fd(50)


pen.right(65)
pen.fd(70)

pen.right(77)
pen.fd(80)

pen.left(82)
pen.fd(55)

pen.right(45)
pen.fd(60)

pen.right(42)
pen.fd(80)

pen.left(85)
pen.fd(90)

pen.right(30)
pen.fd(97)
pen.end_fill()


pen.penup()
pen.goto(x,y)
pen.pd()
pen.begin_fill()
pen.right(100)
pen.fd(60)

pen.left(75)
pen.fd(80)



pen.left(90)
pen.fd(130)
pen.end_fill()
pen.begin_fill()
pen.penup()
pen.goto(xx,yy)
pen.pd()

pen.left(90)
pen.fd(60)

pen.right(90)
pen.fd(40)

pen.right(90)
pen.fd(70)

pen.end_fill()
pen.penup()
pen.goto(-100,-30)
pen.pd()
pen.circle(20,-180)
pen.penup()
pen.setx(-97)
pen.pd()
pen.circle(20,180)


pen.fillcolor("black")
pen.begin_fill()
pen.penup()
pen.goto(-150,110)
pen.pd()
pen.circle(30)
pen.end_fill()


pen.begin_fill()
pen.penup()
pen.goto(50,110)
pen.pd()
pen.circle(30)
pen.end_fill()


pen.fillcolor("white")
pen.begin_fill()
pen.penup()
pen.goto(-150,110)
pen.pd()
pen.circle(10)
pen.end_fill()



pen.begin_fill()
pen.penup()
pen.goto(50,110)
pen.pd()
pen.circle(10)
pen.end_fill()


turtle.done()