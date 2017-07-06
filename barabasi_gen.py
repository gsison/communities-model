# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:13:43 2017

@author: Gabriel
"""

import networkx as nx
import numpy.random as nrand
import numpy as np
import community as com

from copy import deepcopy as dcopy


def get_probs(G):
    degrees = G.degree(weight = "weight")
    denom = np.sum(degrees.values())*1.
    return [degrees[x]/denom for x in G.nodes()]

def weighted_barabasi(n, m, delta):
    if m < 1 or  m >=n:
        raise nx.NetworkXError(\
              "Barabási-Albert network must have m>=1 and m<n, m=%d,n=%d"%(m,n))

    # Add m initial nodes (m0 in barabasi-speak)
    G=nx.empty_graph(m)
    G.name="barabasi_albert_graph(%s,%s)"%(n,m)
    targets=list(range(m))
    source=m
    while source<n:
        # Add edges to m nodes from the source.
        G.add_weighted_edges_from(zip([source]*m,targets,[1.]*m))
        degrees = G.degree(weight = "weight")
        for target in targets:
            wdeg = degrees[target]
            for a, b in G.edges_iter(target):
                G[a][b]["weight"] += (G[a][b]["weight"]*delta)/wdeg

        probs = get_probs(G)
        targets = nrand.choice(G.nodes(), m, p = probs)
        
        source += 1
    return G

def weighted_cbarabasi(n, m, delta, sigma,wdelta = None):
    if m < 1 or  m >=n:
        raise nx.NetworkXError(\
              "Barabási-Albert network must have m>=1 and m<n, m=%d,n=%d"%(m,n))

    # Add m initial nodes (m0 in barabasi-speak)
    G=nx.empty_graph(m)
    G.name="barabasi_albert_graph(%s,%s)"%(n,m)
    targets=list(range(m))
    source=m
    if wdelta is None:
        wdelta = lambda : 1.0
    while source<n:
        # Add edges to m nodes from the source.
        G.add_weighted_edges_from(zip([source]*m,targets,[1.]*m))
        degrees = G.degree(weight = "weight")
        for target in targets:
            wdeg = degrees[target]
            for a, b in G.edges_iter(target):
                G[a][b]["weight"] += (G[a][b]["weight"]*delta)/wdeg
        if nrand.rand() < sigma:
            s, t = nrand.choice(targets), nrand.choice(range(source))

            if G.has_edge(s, t):
                G[s][t]['weight'] += wdelta()
            else:
                G.add_edge(s, t, weight= wdelta())

        probs = get_probs(G)
        targets = nrand.choice(G.nodes(), m, p = probs)
        
        source += 1
    return G

        # Add edges to m nodes from the source.

if __name__ == "__main__":
    mod = []
    for i in range(30):
        g = nx.erdos_renyi_graph(5000, 0.00399279855971)
        mod.append(com.modularity(com.best_partition(g), g))
    print np.mean(mod)
    mod = []
    for i in range(30):
        g = nx.erdos_renyi_graph(5000, 0.00796959391878)
        mod.append(com.modularity(com.best_partition(g), g))
    print np.mean(mod)
    
