import os
import numpy as np
import matplotlib.pyplot as plt



class Edge():
    def __init__(self) -> None:
        self.From = None
        self.To = None
        self.Rating = None
        self.Time = None

fileName = 'soc-sign-bitcoinalpha.csv'
file = open(os.path.join(fileName), 'r+')
lines = file.readlines()

# Read all edges from the file and add bring them in memory
edges = []
nodes = set()

for line in lines:
    if line.startswith('#'):
        continue
    else:
        edgeInfo = line.replace('\n', '')
        edgeInfoParsed = edgeInfo.split(',')
        
        edge = Edge()
        edge.From = int(edgeInfoParsed[0])
        edge.To = int(edgeInfoParsed[1])
        edge.Rating = edgeInfoParsed[2]
        edge.Time = edgeInfoParsed[3]

        edges.append(edge)

        nodes.add(edge.From)
        nodes.add(edge.To)


print(len(nodes))

sortedNodes = sorted(nodes)



def buildAdjacencyMatrix():
    matrix = np.zeros((len(nodes) , len(nodes)))
    for edge in edges:
        matrix[ sortedNodes.index(edge.From)][sortedNodes.index(edge.To)] += 1
    
    # print(matrix)
    return matrix

adj_matrix = buildAdjacencyMatrix()

# Graph definition for adjacency representation 
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.adj_list[node1].append(node2)

# build graph form the data
def buildAdjacencyList():
    g = Graph()
    for edge in edges:
        g.add_edge(edge.From, edge.To)

    # print(g.adj_list)
    return g

buildAdjacencyList()

def Average(lst):
    return sum(lst) / len(lst)

def findMaxIndex(array):
    return max( (v, i) for i, v in enumerate(array) )[1]


#In Degree calculation

num_nodes = len(nodes)
in_degree = [0] * num_nodes

for row in adj_matrix:
    for col, val in enumerate(row):
        if val == 1:
            in_degree[col] += 1

# Max in degree
print("Average In Degree:")
print(Average(in_degree))
print("Node with Max in Degree:")
print(sortedNodes[findMaxIndex(in_degree)])

#Out degree calculation
num_nodes = len(adj_matrix)
out_degree = [0] * num_nodes

for row_index, row in enumerate(adj_matrix):
    for col_index, val in enumerate(row):
        if val == 1:
            out_degree[row_index] += 1

# Max out degree
print("Average Out Degree:")
print(Average(out_degree))
print("Node with Max Out Degree:")
print(sortedNodes[findMaxIndex(out_degree)])

#Calculate density of the directed graph

num_nodes = len(adj_matrix)
num_possible_edges = num_nodes * (num_nodes - 1)
num_edges = sum(sum(row) for row in adj_matrix)
density = num_edges / num_possible_edges
print('Density of the graph: ')
print(density)

#Plot in degree distribution
plt.hist(in_degree, bins=range(12))
plt.title("In-degree Histogram")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

#Plot out degree distribution
plt.hist(out_degree, bins=range(12))
plt.title("Out-degree Histogram")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

#Calculate the local clustering coefficient of each node and plot the clustering-coefficient
#distribution (lcc vs frequency of lcc) of the network


def local_clustering_coefficient(adj_matrix, node):
    neighbors = np.nonzero(adj_matrix[node])[0]
    k = len(neighbors)
    if k < 2:
        return 0
    else:
        count = 0
        for i in range(k):
            for j in range(i+1, k):
                if adj_matrix[neighbors[i]][neighbors[j]] == 1:
                    count += 1
        return 2 * count / (k * (k - 1))

# Calculate the local clustering coefficient of each node
clustering_coefficients = []
for i in range(len(adj_matrix)):
    cc = local_clustering_coefficient(adj_matrix, i)
    clustering_coefficients.append(cc)

# Plot the clustering-coefficient distribution
plt.hist(clustering_coefficients, bins=np.arange(0, 1.1, 0.1))
plt.title("Clustering Coefficient Distribution")
plt.xlabel("Local Clustering Coefficient")
plt.ylabel("Frequency")
plt.show()






