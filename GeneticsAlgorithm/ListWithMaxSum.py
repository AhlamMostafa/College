import random

genset= list(range(101))
target_lenght=5
pop_size=4


def init_parent(length):
    l=[]
    for _ in range(length):
        l.append(random.choice(genset))
    return l

def init_pop(pop_size,lenght):
    pop=[]
    for _ in range(pop_size):
        pop.append(init_parent(lenght))
    return pop



def get_fitness(pop):
    l=[]
    for i in pop:
        l.append(sum(i))
    return l

def cross_uniform(p1,p2):
    mask=[]
    for _ in range(len(p1)):
        mask.append(random.choice([0,1]))
    c1=[]
    c2=[]
    for i in range(len(p1)):
        if mask[i]==1:
            c1.append(p1[i])
            c2.append(p2[i])
        else:
            c1.append(p2[i])
            c2.append(p1[i])
    return c1,c2

def mutation(parent):
    index=random.randint(0,len(parent)-1)
    new,alt=random.sample(genset,2)
    if parent[index]==new:
        parent[index]=alt
    else:
        parent[index]=new

    return parent

def display(pop):
    index_of_best_parent = best_fit.index(max(best_fit))
    fit=sum(pop[index_of_best_parent])
    print(f"{pop[index_of_best_parent]} with fitness equal to {fit} " )

best_pop=init_pop(pop_size,target_lenght)
best_fit=get_fitness(best_pop)

max_iterations=100

while max_iterations!=0:
    index_of_best_parent=best_fit.index(max(best_fit))
    index_of_second_parent=best_fit.index(sorted(best_fit,reverse=True)[1])

    best_parent=best_pop[index_of_best_parent]
    second_parent=best_pop[index_of_second_parent]

    c1,c2=cross_uniform(best_parent,second_parent)

    c1=mutation(c1)
    c2=mutation(c2)

    index_of_worst_parent=best_fit.index(sorted(best_fit,reverse=True)[-1])
    index_of_second_worst_parent=best_fit.index(sorted(best_fit,reverse=True)[-2])
    best_pop[index_of_worst_parent]=c1
    best_pop[index_of_second_worst_parent]=c2

    best_fit = get_fitness(best_pop)
    display(best_pop)
    max_iterations-=1