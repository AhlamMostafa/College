import turtle
import random
import time
import pygame

homes_shapes=['h2.gif','h3.gif','h4.gif','h5.gif','h6.gif']
environment=['BG.gif','h1.gif']
for home in homes_shapes:
    turtle.register_shape(home)
for ele in environment:
    turtle.register_shape(ele)



class Building(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(random.choice(homes_shapes))


pygame.init()
home_sound=pygame.mixer.Sound("home_sound.wav")
wn=turtle.Screen()
wn.title("StackBuilder")
wn.bgpic('BG.gif')
wn.bgcolor("lightblue")
wn.setup(600,600)

pn=turtle.Turtle()
pn.hideturtle()
pn.penup()
pn.goto(-280,-258)
pn.pd()
pn.write("By: Ahlam Mostafa",font=("Courier",12,"bold"))

first_home=turtle.Turtle()
first_home.shape("h1.gif")
first_home.color("red")
first_home.speed(0)
first_home.penup()
first_home.goto(0,-250)


my_homes = [[-27.5,27.5]]
gene_set_1 = list(range(-60, 0))
gene_set_2 = list(range(0, 60))
pop_size = 10
pC = 0.9
pM = 0.5

import random

def get_parent():
    x = random.choice(gene_set_1)
    y = random.choice(gene_set_2)
    return [x, y]


def get_pop(size):
    pop = []
    for _ in range(size):
        pop.append(get_parent())

    return pop


def get_fit(newpop):
    fit = []
    for i in newpop:
        mid_point=((i[0]+i[1])/2)
        fit.append((1/(1000+mid_point)))

    return fit


def crossover(p1, p2):
    pc = random.random()
    c1=[]
    c2=[]
    if pc < pC:
        c1.append(p1[0])
        c1.append(p2[1])
        c2.append(p2[0])
        c2.append(p1[1])
        return c1, c2
    else:
        return p1, p2


def mutation(p1):
    pm = random.random()
    if pm < pM:
        c1 = p1[::]
        index = random.choice([0, 1])
        if (-c1[0])+c1[1]>70:
            if index == 1:
                if c1[index]>my_homes[len(my_homes)-1][0]:
                    c1[index] -= 2
            else:
                if c1[index]<my_homes[len(my_homes)-1][1]:
                    c1[index] += 2
        else:
            if index == 1:
                if c1[index]>my_homes[len(my_homes)-1][0]:
                    c1[index] += 2
            else:
                if c1[index]<my_homes[len(my_homes)-1][1]:
                    c1[index] -= 2

        return c1
    else:
        return p1

n=10
homes_num = 10

while homes_num > 0:
    max_iterations = 30
    best_pop = get_pop(pop_size)
    fit = get_fit(best_pop)
    while max_iterations > 0:

        index_of_best_parent = fit.index(sorted(fit)[-1])
        index_of_second_best_parent = fit.index(sorted(fit)[-2])
        best_parent = best_pop[index_of_best_parent]
        second_best_parent = best_pop[index_of_second_best_parent]

        c1, c2 = crossover(best_parent, second_best_parent)
        c1 = mutation(c1)
        c2 = mutation(c2)

        index_of_worst_parent = fit.index(sorted(fit)[0])
        index_of_second_worst_parent = fit.index(sorted(fit)[1])

        best_pop[index_of_worst_parent] = c1
        best_pop[index_of_second_worst_parent] = c2
        fit = get_fit(best_pop)

        if max_iterations == 1:
            my_homes.append(best_pop[fit.index(sorted(fit)[-1])])

        max_iterations -= 1

    homes_num -= 1



for h in range(1,n):
    time.sleep(0.2)
    home=Building()
    home.hideturtle()
    home.penup()
    home.goto(0,250)
    home.showturtle()
    home_x, home_y = (my_homes[h][0] + my_homes[h][1]) / 2, -250 + (55 * h)
    home.goto(home_x, home_y)
    home_sound.play()


print(my_homes)
wn.mainloop()