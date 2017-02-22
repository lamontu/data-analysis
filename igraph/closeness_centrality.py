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

print("vertex :  degree")
for p in g.vs:
    print(p['name'], ': ', p.degree())
print()

paths = g.get_all_shortest_paths('7')
print("paths using vertex index:")
for p in paths:
    print(p)
print()

names = g.vs['name']
cc = 0
print("path using vertex name:")
for p in paths:
    print([names[x] for x in p])
    cc += len(p) - 1
# Calculate closeness centrality of a vertex
closeness_centrality = (len(paths) - 1) / float(cc)
print("closeness_centrality: ", closeness_centrality)

ccvs = []
# Get the closeness centrality of each vertex
for p in zip(g.vs, g.closeness()):
    ccvs.append({'name': p[0]['name'], 'cc': p[1]})
sorted_ccvs = sorted(ccvs, key=lambda k: k['cc'], reverse=True)
for x in sorted_ccvs:
    print(x)
