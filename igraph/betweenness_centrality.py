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

# Calculate the betweenness centrality of a vertex
shortest_paths = []
target = 7
for v in g.vs:
    paths = g.get_all_shortest_paths(v['name'])
    for p in paths:
        if target in p and target != p[0] and target != p[-1]:
            shortest_paths.append(p)

names = g.vs['name']
betweenness = 0
terminates = []
for x in shortest_paths:
    # Remove duplicated path:
    if set((x[0], x[-1])) not in terminates:
        terminates.append(set((x[0], x[-1])))
        betweenness += 1
print("betweenness centrality of vertex", names[target], ": ", betweenness)

# Get the betweenness centrality of each vertex:
btvs = []
for p in zip(g.vs, g.betweenness()):
    btvs.append({'name': p[0]['name'], 'bt': p[1]})
sorted_btvs = sorted(btvs, key=lambda k: k['bt'], reverse=True)
for x in sorted_btvs:
    print(x)
