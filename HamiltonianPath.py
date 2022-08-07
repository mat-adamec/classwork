import networkx as nx
import sys

def HamiltonianPath(file):
    path = open(file)
    
    n = int(path.readline())
    
    connections = path.read().split("\n")
    connections = [i.split(" ") for i in connections]
    while([""] in connections):
        connections.remove([""])
    
    graph = nx.Graph()
    for j in range(0, n):
        for k in range(1, len(connections[j])):
            graph.add_edge(connections[j][0], connections[j][k])

    def HamWalk(G, p):
        if(len(p) == G.number_of_nodes()):
            return p
        else:
            for vertex in sorted(G.neighbors(p[-1])):
                if not (vertex in p):
                    return HamWalk(G, p+[vertex])
        return False
    
    def HamMain(G):
        path = False
        for vertex in sorted(G.nodes()):
            path = HamWalk(G, [vertex])
            if path != False:
                return path
        return path
    
    path = HamMain(graph)
    
    if path == False:
        print('No Hamiltonian Path')
    else:
        print('Hamiltonian Path: ' + ' '.join(path))
    
file = str(sys.argv[1])
HamiltonianPath(file)