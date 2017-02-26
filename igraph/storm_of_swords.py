# _*_ coding: utf-8 _*_

import csv
from igraph import Graph as IGraph

edges = []
first_line = True
with open('stormofswords.csv', 'r') as f:
    for row in csv.reader(f.read().splitlines()):
        if first_line == True:
            first_line = False
            continue
        u, v, w = [i for i in row]
        edges.append((u, v, int(w)))

g = IGraph.TupleList(edges, directed=True, vertex_name_attr='name',
                     edge_attrs=None, weights=True)

print("# Graph g is weighted?")
print(g.is_weighted())

names = g.vs['name']
weights = g.es['weight']
print(names[:10])
print(weights[:10])
print("# Role number:")
print(g.vcount())

print("# Network diameter:", g.diameter())
max_shortest_path = [names[x] for x in g.get_diameter()]
print("# Max shortest path:")
print(g.get_diameter())
print(max_shortest_path)

print("# Shortest path length between Jon and Margaery:")
# from: 'Jon', to: 'Margaery', this parameter can be a list
print(g.shortest_paths('Jon', 'Margaery'))
# [0] means the path to the first target vertex
paths_JM = [names[x] for x in g.get_shortest_paths('Jon', 'Margaery')[0]]
print(paths_JM)

print("# All path start from vertex 'Jon':")
paths_Jon = g.get_all_shortest_paths('Jon')
"""
for p in paths_Jon:
    print([names[x] for x in p])
"""
print()

print("# Max degree:")
print(g.maxdegree())

# Degree Centrality
print("# Vertex with degree > 15:")
for p in g.vs:
    if p.degree() > 15:
        print(p['name'], p.degree())

# Wighted Degree Centrality
print("# Vertex with weighted_degree > 250:")
for p in g.vs:
    weighted_degree = sum([x.degree() for x in p.neighbors()])
    if weighted_degree > 250:
        print(p['name'], weighted_degree)
print()

print("# Neighbor average degree > 20:")
for p in zip(g.vs, g.knn()[0]):
    if p[1] > 20:
        print(p[0]['name'], p[1])
print()

print("# Neighbors average degree:")
knn1 = g.knn()
for x in knn1:
    print("## Length of the list:",len(x))
    print(x)
print()

# Explain the g.knn()[1]
sum_neighbors_degree = 0
count = 0
#degree = 1
degree = 36
for p in g.vs:
    if p.degree() == degree:
        count += 1
        sum_neighbors_degree += sum([x.degree() for x in p.neighbors()]) / degree
print("Average neighbors degree of vertex with degree 36:")
print(sum_neighbors_degree / count)
print()

print("# Closeness Centrality")
ccvs = []
for p in zip(g.vs, g.closeness()):
    ccvs.append({'name': p[0]['name'], 'cc': p[1]})
sorted_ccvs = sorted(ccvs, key=lambda k: k['cc'], reverse=True)
for x in sorted_ccvs[:5]:
    print(x)
print()

print("# Betweenness Centrality")
btvs = []
for p in zip(g.vs, g.betweenness()):
    btvs.append({'name': p[0]['name'], 'bt': p[1]})
sorted_btvs = sorted(btvs, key=lambda k: k['bt'], reverse=True)
for x in sorted_btvs[:5]:
    print(x)
print()

print("# PageRank")
pg = g.pagerank()
pgvs = []
for p in zip(g.vs, pg):
    pgvs.append({'name': p[0]['name'], 'pg': p[1]})
sorted_pgvs = sorted(pgvs, key=lambda k: k['pg'], reverse=True)
for x in sorted_pgvs[:5]:
    print(x)
print()

print("# Community Detection")
clusters = IGraph.community_walktrap(g, weights='weight').as_clustering()
nodes = [{'name': node['name']} for node in g.vs]
community = {}
for node in nodes:
    idx = g.vs.find(name=node['name']).index
    node['community'] = clusters.membership[idx]
    if node['community'] not in community:
        community[node['community']] = [node['name']]
    else:
        community[node['community']].append(node['name'])
for c, l in community.items():
    print("Community ", c, ": ", l)
