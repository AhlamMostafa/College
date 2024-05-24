import numpy as np
import random

pop_size=20
n=8
geneset=list(range(n))


def get_parent(length):
    board=[]
    board.extend(random.sample(geneset,length))
    return board

def get_pop(pop_size,length):
    pop=[]
    for _ in range(pop_size):
        pop.append(get_parent(length))

    return pop

def get_fitness(pop):
    fit=[]

    for board in pop:
        sc=0
        for i in range(len(board)):
            r=board[i]
            for j in range(len(board)):
                if i==j:
                    continue
                else:
                    d=abs(i-j)
                    if board[j] in [r,r-d,r+d]:
                        sc+=1
        fit.append(-sc)
    return fit


def pmx_crossover(parent1, parent2):
    idx1, idx2 = sorted(random.sample(range(len(parent1)), 2))
    offspring1 = parent1[:]
    offspring2 = parent2[:]
    for i in range(idx1, idx2):
        # Swap the values between the two parents
        offspring1[i], offspring2[i] = offspring2[i], offspring1[i]

    # Repair the offspring to ensure no duplicate values
    for i in range(len(offspring1)):
        if idx1 <= i < idx2:
            continue
        while offspring1[i] in offspring1[idx1:idx2]:
            idx = offspring1.index(offspring1[i], idx1, idx2)
            offspring1[i], offspring2[idx] = offspring2[idx], offspring1[i]

    for i in range(len(offspring2)):
        if idx1 <= i < idx2:
            continue
        while offspring2[i] in offspring2[idx1:idx2]:
            idx = offspring2.index(offspring2[i], idx1, idx2)
            offspring1[idx], offspring2[i] = offspring2[i], offspring1[idx]

    return offspring1, offspring2


def mutation(p):
    l,r=sorted(list(np.random.randint(0,len(p)-1,2)))
    c=p[::]
    c[l],c[r]=c[r],c[l]
    return c

best_pop=get_pop(pop_size,8)
best_fit=get_fitness(best_pop)
max_iterations=100
while max_iterations>=0:
    index_of_best_parent=best_fit.index(sorted(best_fit)[-1])
    index_of_second_best_parent = best_fit.index(sorted(best_fit)[-2])

    c1,c2=pmx_crossover(best_pop[index_of_best_parent],best_pop[index_of_second_best_parent])
    c1=mutation(c1)
    c2=mutation(c2)
    index_of_worst_parent = best_fit.index(sorted(best_fit)[0])
    index_of_second_worst_parent = best_fit.index(sorted(best_fit)[1])

    best_pop[index_of_worst_parent], best_pop[index_of_second_worst_parent] = c1 , c2

    best_fit=get_fitness(best_pop)
    index_of_best_parent = best_fit.index(sorted(best_fit)[-1])
    best_result =[best_pop[index_of_best_parent],sorted(best_fit)[-1]]
    max_iterations-=1

print(f"the best result is{best_result[0]} with fitness={best_result[1]}")