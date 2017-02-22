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

pg = g.pagerank()

pgvs = []
for p in zip(g.vs, pg):
    pgvs.append({'name': p[0]['name'], 'pg': p[1]})
sorted_pgvs = sorted(pgvs, key=lambda k: k['pg'], reverse=True)
for x in sorted_pgvs:
    print(x)
