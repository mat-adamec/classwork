import sys
import numpy as np

def DynamicKnapsack(filename):
    file = open(filename)
    
    (n, W) = [int(x) for x in file.readline().strip('\n').split(' ')]
    weights = [int(wt) for wt in file.readline().strip('\n').split(' ')]
    values = [int(val) for val in file.readline().strip('\n').split(' ')]
    
    V = np.zeros(shape=(n+1, W+1))
    for j in range(0, W+1):
        V[0][j] = 0
    for i in range(0, n+1):
        V[i][0] = 0
        
    for i in range(1, n+1):
        for j in range(1, W+1):
            if j < weights[i-1]:
                V[i][j] = V[i-1][j]
            else:
                V[i][j] = max(V[i-1][j], values[i-1] + V[i-1][j-weights[i-1]])

    S = set([])
    i = n
    j = W
    while (i >= 1) & (j >= 1):
        while (i >= 1) & (V[i][j] == V[i-1][j]):
            i = i-1
        S.add((i, weights[i-1], values[i-1]))
        j = j - weights[i-1]
        i = i - 1
    print('Tableau')
    print(V)
    print('Maximum Capacity: ' + str(W))
    print('Original Knapsack Items: ' + str([(ind, wt, val) for (ind, wt, val) in zip(range(1,n+1), weights, values)]))
    print('Optimal Knapsack Items: ' + str(sorted(S)))
    optWeight = 0
    optVal = 0
    for opt in S:
        optWeight += opt[1]
        optVal += opt[2]
    print('Optimal Weight: ' + str(optWeight))
    print('Optimal Value: ' + str(optVal))

DynamicKnapsack(sys.argv[1])