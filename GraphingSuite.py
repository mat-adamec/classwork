import networkx as nx
import sys
import math
import numpy as np
from collections import deque
from itertools import combinations

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peak(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = deque([])
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.popleft()
    def peak(self):
        return self.items[0]
    def size(self):
        return len(self.items)

def GraphGenerator(file):
    path = open(file)
    
    n = int(path.readline())
    
    connections = path.read().split("\n")
    connections = [i.split(" ") for i in connections]
    while([""] in connections):
        connections.remove([""])
    graph = nx.Graph()
    for j in range(0, len(connections)):
        graph.add_edge(connections[j][0], connections[j][1], weight=float(connections[j][2]))
    
    return graph
        
def DepthFirstSearch(graph):
    vertices = sorted(graph.nodes())
    cycle = False
    gray = []
    black = []
    for vertex in vertices:
        if (vertex not in gray) & (vertex not in black):
            S = Stack()
            S.push(vertex)
            gray.append(vertex)
            while(S.size() > 0):
                x = S.peak()
                y = [i for i in sorted(graph.neighbors(x)) if (i not in gray) & (i not in black)]
                if y != []:
                    y = y[0]
                    cyc = [j for j in graph.neighbors(y) if (j in gray) & (j != x)]
                    if cyc != []:
                        cycle = True
                    S.push(y)
                    gray.append(y)
                else:
                    S.pop()
                    black.append(x)
    output = gray
    return output, cycle
        
def BreadthFirstSearch(graph):
    vertices = sorted(graph.nodes())
    gray = []
    black = []
    output = []
    for vertex in vertices:
        if (vertex not in gray) & (vertex not in black):
            Q = Queue()
            Q.enqueue(vertices[0])
            gray.append(vertices[0])
            while(Q.size() > 0):
                x = Q.peak()
                weighted = sorted(graph[x].items(), key=lambda lowest: lowest[1]['weight'])
                for y in weighted:
                    if (y[0] not in gray) & (y[0] not in black):
                        Q.enqueue(y[0])
                        gray.append(y[0])
                z = Q.dequeue()
                output.append(z)
                black.append(z)
    return output

def MinimumSpanningTree(graph):
    weighted = sorted(graph.edges(data='weight'), key=lambda x: x[2])
    newGraph = nx.Graph()
    for edge in weighted:
        newGraph.add_edge(edge[0], edge[1], weight=edge[2])
        out, cyc = DepthFirstSearch(newGraph)
        if cyc != False:
            newGraph.remove_edge(edge[0], edge[1])
    newWeight = sorted(newGraph.edges(data='weight'), key=lambda x: x[2])
    sumWeight = 0
    for edge in newWeight:
        sumWeight += edge[2]
    sumWeight = round(sumWeight, 5)
    print('Minimum Spanning Tree:')
    print('V = ' + ', '.join(sorted(newGraph.nodes())))
    print('E = ' + ', '.join(str(tup) for tup in newWeight))
    print('Total Weight: ' + str(sumWeight))
    
def ShortestPath(graph):
    nodes = sorted(graph.nodes())
    D = np.zeros((len(nodes), len(nodes)))
    S = np.ones((len(nodes), len(nodes)))
    S.fill(None)
    wtTotal = 1
    for edge in graph.edges(data='weight'):
        wtTotal += edge[2]
    for i in range(0, len(D)):
        for j in range(0, len(D)):
            if graph.has_edge(nodes[i], nodes[j]):
                D[i][j] = graph.get_edge_data(nodes[i], nodes[j])['weight']
                S[i][j] = j
            elif i == j:
                D[i][j] = 0
            else:
                D[i][j] = wtTotal
    for k in range(0, len(D)):
        for i in range(0, len(D)):
            for j in range(0, len(D)):
                orig = D[i][j]
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                if orig != D[i][j]:
                    S[i][j] = S[i][k]
    print('Shortest Paths')
    for pair in list(combinations(range(0, len(D)), 2)):
        hasPath = True
        p = [nodes[pair[0]]]
        x = nodes[pair[0]]
        while x != pair[1]:
            x = S[int(x)][pair[1]]
            if np.isnan(x):
                hasPath = False
                break
            p.append(nodes[int(x)])
        path = ''
        pathWeight = 0
        for one, two in zip(p[:-1], p[1:]):
            if hasPath:
                try:
                    pathWeight += graph.get_edge_data(one, two)['weight']
                    if two != p[-1]:
                        path += '(' + str(one) + ', ' + str(two) + ', ' + str(graph.get_edge_data(one, two)['weight']) + ') -> '
                    else:
                        path += '(' + str(one) + ', ' + str(two) + ', ' + str(graph.get_edge_data(one, two)['weight']) + ')'
                except TypeError:
                    hasPath = False
                    pass
        if hasPath:
            print(str(pair[0]) + ' -> ' + str(pair[1]) + ' = ' + path)
            print('Path Weight = ' + str(pathWeight))
        else:
            print(str(pair[0]) + ' -> ' + str(pair[1]) + ' = ' + 'Disconnected Graph (No Path)')
        
            
#file = str(sys.argv[1])
graph = GraphGenerator(file)
print('Depth First Search Traversal:')
print(', '.join(DepthFirstSearch(graph)[0]) + '\n')
print('Breadth First Search Traversal:')
print(', '.join(BreadthFirstSearch(graph)) + '\n')
MinimumSpanningTree(graph)
print('')
ShortestPath(graph)