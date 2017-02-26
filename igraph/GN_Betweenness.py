# _*_ coding: utf-8 _*_

import csv
from igraph import Graph as IGraph

edges = []
with open('net.csv', 'r') as f:
    for row in csv.reader(f.read().splitlines()):
        u, v = [i for i in row]
        edges.append((u, v))

g = IGraph.TupleList(edges, directed=False, vertex_name_attr='name',
                     edge_attrs=None, weights=False)
print("Graph g:")
print(g)
print()

names = g.vs['name']

# Get the edge betweenness of each edge
btes = []
for p in zip(g.es(), g.edge_betweenness()):
    e = p[0].tuple
    btes.append({'edge': (names[e[0]], names[e[1]]), 'bt': p[1]})
sorted_btes = sorted(btes, key=lambda k: k['bt'], reverse=True)
for x in sorted_btes:
    print(x)
print()

# Find communities: remove edges with high betweenness
communities = g.community_edge_betweenness(directed=False, weights=None)
print(communities)
print(g.vs['name'])
