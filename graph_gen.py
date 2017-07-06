# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 10:45:37 2017

@author: Gabriel
"""

import networkx as nx
import numpy as np
import numpy.random as rand
import community as com
import itertools

def all_pairs(a_list):
    return [x for x in itertools.combinations(a_list, 2)]


def all_pairs2(a_list):
    v = [[x]*len(a_list) for x in a_list]
    a = [item for sublist in v for item in sublist]
    return a, 
    
def target_density(iterable, density):
    tot = len(iterable)
    target = int(density * tot)
    b = rand.choice(len(iterable), target)
    out = np.array(iterable)
    return out[b]

def rand_dense_graph(N, density, weights):
    g = nx.Graph()
    edges = all_pairs(range(N))
    edges = target_density(edges, density)
    g.add_weighted_edges_from([(a,b,c) for (a,b),c in zip(edges, weights)])
    return g

def rand_dense_graph_com(N, density, weight1, weight2):
    g = nx.Graph()
    edges = all_pairs(range(N))
    edges = target_density(edges, density)
    leng = len(weight1)/2
    q = [(u, v, w) for (u, v), w in 
    zip(edges, weight1[:leng]) if (u<N/2. and v<N/2.)]
    p = [(u, v, w) for (u, v), w in 
    zip(edges, weight1[leng:]) if (u>N/2. and v>N/2.)]
    r = [(u, v, w) for (u, v), w in 
    zip(edges, weight2[:leng]) if (u>N/2. and v<N/2.)]
    s = [(u, v, w) for (u, v), w in 
    zip(edges, weight2[leng:]) if (u<N/2. and v>N/2.)]
    g.add_weighted_edges_from(q+p+r+s)
    return g
    


if __name__ == "__main__":
    N= 400
    density = 0.95
    mean = 600
    scale = 500
    weights = rand.normal(mean, scale, N).clip(min = 0)
    
    
    g = rand_dense_graph(N,density,weights)
    print com.modularity(com.best_partition(g), g)
