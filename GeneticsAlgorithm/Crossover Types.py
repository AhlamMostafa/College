import random
import numpy as np


def crossover_SinglePoint(p1,p2):
    l=random.randint(1,len(p1)-1)
    l1=p1[:l]+p2[l:]
    l2=p2[:l]+p1[l:]
    return l1,l2

def crossover_TwoPoints(p1,p2):
    r=random.randint(1,len(p1)-1)
    l=random.randint(1,len(p1)-1)
    temp=0
    if r>l:
        temp=r
        r=l
        l=temp
    elif r==l:
        while r==l:
            r = random.randint(1, len(p1) - 1)
    l1=p1[:r]+p2[r:l]+p1[l:]
    l2=p2[:r]+p1[r:l]+p2[l:]
    return l1,l2

def crossover_uniform(p1,p2):
    mask=[]
    for _ in range(len(p1)):
        mask.append(random.choice([0,1]))
    l1=[]
    l2=[]
    for i in range(len(p1)):
        if mask[i]==0:
            l1.append(p2[i])
            l2.append(p1[i])
        else:
            l1.append(p1[i])
            l2.append(p2[i])
    return l1,l2

def crossover_ThreeParent(p1,p2,p3):
    l=[]
    for i,j,k in zip(p1,p2,p3):
        if i==j:
            l.append(i)
        else:
            l.append(k)
    return l

def crossover_Shuffle(p1,p2):
    l1=p1[::]
    random.shuffle(l1)
    l2=p2[::]
    random.shuffle(l2)
    return l1,l2

def ordered_crossover(p1,p2):
    # index=np.random.randint(1,len(p1)-1)
    # c1=p1[:index]+p2[index:]
    # c2=p2[:index]+p2[index:]
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


def cx_crossover(p1, p2):
    map, i = {}, 0
    map[p1[i]] = p2[i]
    while True:
        if map[p1[i]] in map.keys():
            break
        i = p1.index(map[p1[i]])
        map[p1[i]] = p2[i]
    length = len(p1)
    c1, c2 = [None] * length, [None] * length
    for i in range(length):
        if p1[i] in map.keys() and p2[i] is map[p1[i]]:
            c1[i] = p1[i]
            c2[i] = p2[i]
        else:
            c1[i] = p2[i]
            c2[i] = p1[i]
    return c1, c2

def pmx_crossover(p1, p2):
    idx1, idx2 = sorted(random.sample(range(len(p1)), 2))
    c1 = p1[:]
    c2 = p2[:]
    for i in range(idx1, idx2):
        c1[i], c2[i] = c2[i], c1[i]

    for i in range(len(c1)):
        if idx1 <= i < idx2:
            continue
        while c1[i] in c1[idx1:idx2]:
            idx = c1.index(c1[i], idx1, idx2)
            c1[i], c2[idx] = c2[idx], c1[i]

    for i in range(len(c2)):
        if idx1 <= i < idx2:
            continue
        while c2[i] in c2[idx1:idx2]:
            idx = c2.index(c2[i], idx1, idx2)
            c1[idx], c2[i] = c2[i], c1[idx]

    return c1, c2