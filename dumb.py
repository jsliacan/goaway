#! /usr/bin/python3

import random

import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
containers = range(G.order())

deg_seq1 = [G.degree(i) for i in range(G.order())]
plt1 = plt.hist(deg_seq1, bins=containers, alpha=0.5)

k = 10
sample = random.sample(G.nodes(), k) # initialize
whole_bunch = list()

for node in sample:
    whole_bunch.extend(list(G.neighbors(node)))

whole_bunch = list(set(whole_bunch)) # setify!
deg_seq = [G.degree(node) for node in whole_bunch]
plt2 = plt.hist(deg_seq, bins=containers, alpha=0.5)

plt.show()
