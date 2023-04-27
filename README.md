# CSE508_Winter2023_A3_Group_No.79
Assignment 3 repo

# Q1 objectives:
Pick a real-world directed network dataset (with number of nodes > 100) from here. [2
points] Represent the network in terms of its ‘adjacency matrix’ as well as ‘edge list’.
[28 points] Briefly describe the dataset chosen and report the following:
1. Number of Nodes
2. Number of Edges
3. Avg In-degree
4. Avg. Out-Degree
5. Node with Max In-degree
6. Node with Max out-degree
7. The density of the network
Further, perform the following tasks:
1. [5 points] Plot degree distribution of the network (in case of a directed graph, plot in-degree and
out-degree separately).
2. [10 points] Calculate the local clustering coefficient of each node and plot the clustering-coefficient
distribution (lcc vs frequency of lcc) of the network.

Solution:

DataSet selection:

We have picked the following data-set for this assignment.

https://snap.stanford.edu/data/wiki-Vote.html


DataSet Description: Directed graph
1. Number of nodes: 3,783
2. Number of Edges: 24,186
3. Average In Degree: 6.39
4. Average Out Degree: 6.39
5. Node with Max In-Degree: Node 1 with value 398
6. Node with Max Out-Degree: Node 1 with value 490
7. Density of the network: 0.0016904649973936393

Following formula is used to calculate the Density
density = (number of edges) / (number of possible edges)
        = (number of edges) / ((N)*(N-1)) --Where n is number of nodes



# Q2: objectives
For the dataset chosen in the above question, calculate the following:
1. [15 points] PageRank score for each node
2. [15 points] Authority and Hub score for each node

Solution:
Output:
      Node  Node_id  pageRank      Hubs  Authorities
      
0        1        0  0.022534  0.005426     0.005426

1        2        1  0.006895  0.006920     0.006920

2        3        2  0.008294  0.006310     0.006310

3        4        3  0.007146  0.004013     0.004013

4        5        4  0.005705  0.004776     0.004776

...    ...      ...       ...       ...          ...

3778  7600     3778  0.000917  0.001632     0.001632

3779  7601     3779  0.000554  0.001203     0.001203

3780  7602     3780  0.000598  0.001390     0.001390

3781  7603     3781  0.003075  0.003550     0.003550

3782  7604     3782  0.002171  0.003373     0.003373


[3783 rows x 5 columns]
