# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 01:19:27 2017

@author: Gabriel
"""

import networkx as nx
import community as c
import numpy as np

trials = 30

for k in [2,5,10,20]:
    x = range(trials)
    
    for i in range(trials):
        g = nx.barabasi_albert_graph(5000,k)
        x[i] = c.modularity(c.best_partition(g),g)
    
    print np.mean(x)
