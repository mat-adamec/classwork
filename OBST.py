import sys
import numpy as np

inf = 999999999999999999

class Node:
    def __init__(self, left=None, right=None, root=None, parent=None):
        self.left = left
        self.right = right
        self.root = root
        self.parent = parent
    def getChildren(self):
        return((self.left, self.right))
    def getParent(self):
        return(self.parent)
    def rightChild(self, right):
        self.right = right
    def leftChild(self, left):
        self.left = left
    def parent(self, parent):
        self.parent = parent
    def getRoot(self):
        return self.root + 1
    
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def OptimalBST(filename):
    file = open(filename)
    
    n = int(file.readline())
    
    keys = []
    
    for i in range(0,n):
        line = file.readline().strip('\n').split(' ')
        keys.append((line[0], float(line[1])))
    
    keys = sorted(keys, key=lambda x: x[0])
    
    C = np.zeros(shape=(n+2,n+1))
    C.fill(np.nan)
    R = np.zeros(shape=(n,n))
    R.fill(np.nan)
    
    for i in range(0, n):
        C[i+1][i] = 0
        C[i+1][i+1] = keys[i][1]
        R[i][i] = i
    C[n+1][n] = 0
    
    for d in range(0, n):
        for i in range(1, n-d+1):
            j = i + d
            minimum = inf
            probSum = 0
            for k in range(i, j+1):
                probSum += keys[k-1][1]
                q = C[i][k-1] + C[k+1][j]
                if q < minimum:
                    minimum = q
                    R[i-1][j-1] = k
            C[i][j] = minimum + probSum
    
    nodes = []
    root = Node(root=R[0][n-1]-1)
    nodes.append((root, root.getRoot()))
    S = Stack()
    S.push((root, 0, n-1))
    counter = 0
    
    while S.size() != 0:
        (u, i, j) = S.pop()
        k = R[int(i)][int(j)]-1
        if (i < k) & (k > 0):
            w = Node(root=R[int(i)][int(k-1)]-1, parent=u)
            u.leftChild(w)
            S.push((w, i, k-1))
            nodes.append((w, w.getRoot()))
        if k < j:
            v = Node(root=R[int(k+1)][int(j)]-1, parent=u)
            u.rightChild(v)
            S.push((v, k+1, j))
            nodes.append((v, v.getRoot()))

    print('C = ' + str(C))
    print('R = ' + str(R))
    nodes = sorted(nodes, key=lambda x: x[1])
    for node in nodes:
        print('Node')
        print('\tKey: ' + keys[int(node[1]-1)][0])
        print('\tProbability: ' + str(keys[int(node[1]-1)][1]*100) + '%')
        if node[0].getParent() != None:
            print('\tParent: ' + str(keys[int(node[0].getParent().getRoot()-1)][0]))
        else:
            print('\tParent: None')
        if node[0].getChildren()[0] != None:
            print('\tLeft Child: ' + str(keys[int(node[0].getChildren()[0].getRoot()-1)][0]))
        else:
            print('\tLeft Child: None')
        if node[0].getChildren()[1] != None:
            print('\tRight Child: ' + str(keys[int(node[0].getChildren()[1].getRoot()-1)][0]))
        else:
            print('\tRight Child: None')
            
OptimalBST(sys.argv[1])