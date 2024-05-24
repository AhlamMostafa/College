import numpy as np
import random

# Define the cities and distances
pop_size=20
cities = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
geneset=list(cities.values())
distances = [
    [0, 12, 10, 19, 8],  # Distances from A
    [12, 0, 3, 7, 2],    # Distances from B
    [10, 3, 0, 6, 20],   # Distances from C
    [19, 7, 6, 0, 4],    # Distances from D
    [8, 2, 20, 4, 0]     # Distances from E
]


def get_parent(length):
    gene=[]
    gene.extend(random.sample(geneset,length))
    return gene


def get_pop(pop_size,length):
    pop=[]
    for _ in range(pop_size):
        pop.append(get_parent(length))
    return pop


# Fitness function
def get_fit(pop):
    fit=[]
    for route in pop:
        total_distance = 0
        for i in range(len(route)):
            total_distance += distances[route[i-1]][route[i]]
        fit.append(1 / total_distance)
    return fit


def ordered_crossover(p1,p2):
    l,r=sorted(np.random.randint(1,len(p1)-2,2))
    c1,c2=[],[]
    map1=p1[l:r+1]
    map2=p2[l:r+1]
    for i in p2:
        if i in map1:
            pass
        else:
            c1.append(i)
    for j in p1:
        if j in map2:
            pass
        else:
            c2.append(j)
    x=0
    for k in range(l,r+1):
        c1.insert(k,map1[x])
        c2.insert(k,map2[x])
        x+=1
    return c1,c2


def mutation(p):
    c=p[::]
    l,r=np.random.randint(0,len(p)-1,2)
    c[l],c[r]=c[r],c[l]
    return c


best_pop=get_pop(pop_size,len(cities))
best_fit=get_fit(best_pop)
max_iterations=100
while max_iterations>=0:
    index_of_best_parent=best_fit.index(sorted(best_fit)[-1])
    index_of_second_best_parent = best_fit.index(sorted(best_fit)[-2])

    c1,c2=ordered_crossover(best_pop[index_of_best_parent],best_pop[index_of_second_best_parent])
    c1=mutation(c1)
    c2=mutation(c2)
    index_of_worst_parent = best_fit.index(sorted(best_fit)[0])
    index_of_second_worst_parent = best_fit.index(sorted(best_fit)[1])

    best_pop[index_of_worst_parent], best_pop[index_of_second_worst_parent] = c1 , c2

    best_fit=get_fit(best_pop)
    index_of_best_parent = best_fit.index(sorted(best_fit)[-1])
    best_result =[best_pop[index_of_best_parent],sorted(best_fit)[-1]]
    max_iterations-=1

print(best_result)