import numpy as np
import sys

def LinearSolver(filename):
    file = open(filename)
    
    n = int(file.readline())
    
    matrix = []

    for i in range(0, n):
        matrix.append(file.readline().strip('\n').split(' '))
           
    b = file.readline().strip('\n').split(' ')
    b = [float(x) for x in b]
    
    for sublist in matrix:
        for x in range(0, len(sublist)):
            sublist[x] = float(sublist[x])
            
    matrix = np.array(matrix)
    b = np.transpose(np.array([b]))
    matrix = np.hstack((matrix, b))
    
    def ForwardElimination(matrix):
        triangular = np.copy(matrix)
        for i in range(0, n-1):
            pivotrow = i
            # Finding best pivot row
            for j in range(i+1, n):
                if np.abs(triangular[j, i]) > np.abs(triangular[pivotrow, i]):
                    pivotrow = j
            for k in range(i, n+1):
                triangular[i, k], triangular[pivotrow, k] = triangular[pivotrow, k], triangular[i, k]
            # Actual solution
            for j in range(i+1, n):
                if triangular[i, i] == 0:
                    print('Inconsistent System')
                    return
                else:
                    t = triangular[j, i]/triangular[i,i]
                    for k in range(i, n+1):
                        triangular[j, k] = triangular[j, k] - triangular[i, k] * t
        return triangular

    def BackSubstitution(triangular):
        x = np.zeros((n, 1))
        for i in range(n-1, -1, -1):
            x[i] = triangular[i, n]
            for j in range(i+1, n):
                x[i] = x[i] - x[j] * triangular[i, j]
            if triangular[i, i] == 0:
                print('Inconsistent System')
                return
            else:
                x[i] = x[i]/triangular[i, i]
        elstr = ''
        for element in x:
            elstr += str(element[0]) + ' '
        print(elstr)
        return
    
    triangular = ForwardElimination(matrix)
    if type(triangular) != np.ndarray:
        return
    else:
        BackSubstitution(triangular)

LinearSolver(sys.argv[1])