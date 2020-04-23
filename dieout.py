#!/usr/bin/python3

import random

N = 100
U = [0 for x in range(N)]

infected = random.randint(0,N)
U[infected] = 1

p = 0.3
while sum(U) > 0:
    newU = [0 for x in range(N)] # create a copy of U
    for i in range(N):
        if U[i] == 1:
            if random.random() < p:
                newU[i] = 0
            else:
                newU[i] = U[i]
        else:
            if random.random() > p and (U[(i-1)%N] == 1 or U[(i+1)%N] == 1):
                newU[i] = 1
            else:
                newU[i] = U[i]
    U = [x for x in newU] # copy back to U
    print(sum(U))
                
