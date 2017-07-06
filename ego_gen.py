# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 23:44:18 2017

@author: Gabriel Sison
"""
from __future__ import division
import networkx as nx
import numpy.random as nrand
import numpy as np
import community as com
import matplotlib.pyplot as plt


def egraphsetup(m, G, radius = 1):
    egraph = nx.ego_graph(G, m, radius, center = True)
    enodes = egraph.nodes()
    edegrees = egraph.degree(enodes)           #removal is done for weigted
    enodes.remove(m)                      #network compatability           
    edegrees = [edegrees[x] for x in enodes]
    return enodes, edegrees
    

def ego_graph_edge_addition(G, p, m, radius = 1):
    nodes = G.nodes()
    source = len(nodes)
    nrand.shuffle(nodes) #Selects the first
    first = nodes.pop()  #target node
    enodes, edegrees = egraphsetup(first, G, radius) #Simple check if the first node is disconnected
    added = 1
    while added < m:
        if enodes: #if egograph is empty, go to random attachment
            if (nrand.rand() < p): 
                eprobs = edegrees/np.sum(edegrees) #renormalizes probs
                target = nrand.choice(enodes,p=eprobs)
                i = enodes.index(target)                   #removing used nodes
                enodes.pop(i)                              #removing used nodes
                edegrees = np.delete(edegrees, i)          #removing used nodes
                nodes.remove(target)      #added nodes shouldn't be selected twice
            else:
                target = nodes.pop()
                if target in enodes:
                    i = enodes.index(target)              #removing used nodes
                    enodes.pop(i)                         #removing used nodes
                    edegrees = np.delete(edegrees, i)
            G.add_edge(source, target)
        else:
            target = nodes.pop()
            G.add_edge(source, target)
        added += 1
    #Don't forget to attach the initial node! We do this here so that 
    #the source is not part of the ego graph
    G.add_edge(source, first) 

def global_graph_edge_addition(G, p, m):
    nodes = G.nodes()
    source = len(nodes)
    nrand.shuffle(nodes) #Selects the first
    first = nodes.pop()  #target node
    enodes = G[first].keys() #Simple check if the first node is disconnected
    edegrees = [G.degree(anode) for anode in enodes]
    added = 1
    while added < m:
        if enodes: #if egograph is empty, go to random attachment
            if (nrand.rand() < p): 
                eprobs = edegrees/np.sum(edegrees) #renormalizes probs
                target = nrand.choice(enodes,p=eprobs)
                i = enodes.index(target)                   #removing used nodes
                enodes.pop(i)                              #removing used nodes
                edegrees = np.delete(edegrees, i)          #removing used nodes
                nodes.remove(target)      #added nodes shouldn't be selected twice
            else:
                target = nodes.pop()
                if target in enodes:
                    i = enodes.index(target)              #removing used nodes
                    enodes.pop(i)                         #removing used nodes
                    edegrees = np.delete(edegrees, i)
            G.add_edge(source, target)
        else:
            target = nodes.pop()
            G.add_edge(source, target)
        added += 1
    #Don't forget to attach the initial node! We do this here so that 
    #the source is not part of the ego graph
    G.add_edge(source, first) 


def triadic_closure_addition(G, p, m):
    nodes = G.nodes()
    source = len(nodes)
    nrand.shuffle(nodes) #Selects the first
    first = nodes.pop()  #target node
    neighbors = G.neighbors(first) #Simple check if the first node is disconnected
    nrand.shuffle(neighbors)
    added = 1
    while added < m:
        if neighbors:
            if (nrand.rand() < p): #if egograph is empty, go to erdos-
                target = neighbors.pop()
                nodes.remove(target)
            else:
                target = nodes.pop()
                if target in neighbors:
                    neighbors.remove(target)
            G.add_edge(source, target)
        else:
            target = nodes.pop()
            G.add_edge(source, target)
        added += 1
    #Don't forget to attach the initial node! We do this here so that 
    #the source is not part of the ego graph
    G.add_edge(source, first) 



def egograph_connection_model(p, n, m, graph_seed, radius = 1):
    """
    The ego-graph model, based on triadic closure and ego-preferential
    attachment
    p = probablity of connection within the ego-graph
    n = target number of nodes
    m = number of edges added per timestep
    graph_seed = If int, and empty graph of that size is generated
    if graph, the graph is used as the initial step
    """
    try:
        G = nx.empty_graph(graph_seed)
    except:
        G = graph_seed
    nodes = len(G.nodes())
    while nodes < n:
        ego_graph_edge_addition(G, p, m, radius)
        nodes += 1
    return G

def triadic_closure_model(p, n, m, graph_seed):
    """
    The triadic closure model
    p = probablity of connection within the ego-graph
    n = target number of nodes
    m = number of edges added per timestep
    graph_seed = If int, and empty graph of that size is generated
    if graph, the graph is used as the initial step
    """
    try:
        G = nx.empty_graph(graph_seed)
    except:
        G = graph_seed
    nodes = len(G.nodes())
    while nodes < n:
        triadic_closure_addition(G, p, m)
        nodes += 1
    return G

def triadic_closure_global_model(p, n, m, graph_seed):
    """
    The triadic closure model
    p = probablity of connection within the ego-graph
    n = target number of nodes
    m = number of edges added per timestep
    graph_seed = If int, and empty graph of that size is generated
    if graph, the graph is used as the initial step
    """
    try:
        G = nx.empty_graph(graph_seed)
    except:
        G = graph_seed
    nodes = len(G.nodes())
    while nodes < n:
        global_graph_edge_addition(G, p, m)
        nodes += 1
    return G


def modularity_calc(Folder, ps, trials = 5, label = "", m = None):
    means = []
    stds = []
    for p in ps:
        mods = []
        for trial in range(trials):
            if m is None:
                name = "{}/p{}-trial{}.gz".format(Folder,str(p),str(trial))
            else:
                name = "{}/m{}p{}-trial{}.gz".format(Folder,str(m),str(p),str(trial))
            G = nx.read_gpickle(name)
            mods += [com.modularity(com.best_partition(G), G)]
            print name
        means = means + [np.mean(mods)]
        stds = stds + [np.std(mods)]
    plt.errorbar(ps,means,yerr = stds, label=label)
    if m is None:
        m = ""
    with open(Folder+"{}.txt".format(str(m)), 'w') as output:
        output.write(str(means))
        output.write("\n")
        output.write(str(stds))

def density_calc(Folder, ps, trials = 5, label = "",m = None):
    means = 0.
    for p in ps:
        mods = 0.
        for trial in range(trials):
            if m is None:
                name = "{}/p{}-trial{}.gz".format(Folder,str(p),str(trial))
            else:
                name = "{}/m{}p{}-trial{}.gz".format(Folder,str(m),str(p),str(trial))
            G = nx.read_gpickle(name)
            mods += nx.density(G)
        means += mods/(trials*1.)
    print label, (means*1.)/(len(ps)*1.)


if __name__ == "__main__":
    ps = np.linspace(0.05,1.0,20)

#    for p in ps:
#        for trial in range(5,20):
#            name = "Results5/p{}-trial{}.gz".format(str(p),str(trial))
#            G = egograph_connection_model(p, 5000, 2, 2)
#            nx.write_gpickle(G,name)
#            print name
#    for p in ps:
#        for trial in range(5,20):
#            name = "Results6/p{}-trial{}.gz".format(str(p),str(trial))
#            G = egograph_connection_model(p, 5000, 5, 5)
#            nx.write_gpickle(G,name)
#            print name
#    for p in ps:
#        for trial in range(5,20):
#            name = "Results5/m10p{}-trial{}.gz".format(str(p),str(trial))
#            G = egograph_connection_model(p, 5000, 10, 10)
#            nx.write_gpickle(G,name)
#            print name
#    for p in ps:
#        for trial in range(5,20):
#            name = "Results6/m20p{}-trial{}.gz".format(str(p),str(trial))
#            G = egograph_connection_model(p, 5000, 20, 20)
#            nx.write_gpickle(G,name)
#            print name    
#    for p in ps:
#        for trial in range(5,20):
#            name = "ExK2/Results_1/p{}-trial{}.gz".format(str(p),str(trial))
#            G = triadic_closure_global_model(p, 5000, 2, 2)
#            nx.write_gpickle(G,name)
#            print name
#    for p in ps:
#        for trial in range(5,20):
#            name = "ExK2/Results_2/p{}-trial{}.gz".format(str(p),str(trial))
#            G = triadic_closure_global_model(p, 5000, 5, 5)
#            nx.write_gpickle(G,name)
#            print name    
#    for p in ps:
#        for trial in range(5,20):
#            name = "ExK2/Results_3/p{}-trial{}.gz".format(str(p),str(trial))
#            G = triadic_closure_global_model(p, 5000, 10, 10)
#            nx.write_gpickle(G,name)
#            print name    
#    for p in ps:
#        for trial in range(5,20):
#            name = "ExK2/Results_4/p{}-trial{}.gz".format(str(p),str(trial))
#            G = triadic_closure_global_model(p, 5000, 20, 20)
#            nx.write_gpickle(G,name)
#            print name
#    for p in ps:
#        for trial in range(5,20):
#            name = "Results3/p{}-trial{}.gz".format(str(p),str(trial))
#            G = triadic_closure_model(p, 5000, 2, 2)
#            nx.write_gpickle(G,name)
#            print name
#    for p in ps:
#        for trial in range(5,20):
#            name = "Results4/p{}-trial{}.gz".format(str(p),str(trial))
#            G = triadic_closure_model(p, 5000, 5, 5)
#            nx.write_gpickle(G,name)
#            print name
#    for p in ps:
#        for trial in range(5,20):
#            name = "Results3/m10p{}-trial{}.gz".format(str(p),str(trial))
#            G = triadic_closure_model(p, 5000, 10, 10)
#            nx.write_gpickle(G,name)
#            print name
#    for p in ps:
#        for trial in range(5,20):
#            name = "Results4/m20p{}-trial{}.gz".format(str(p),str(trial))
#            G = triadic_closure_model(p, 5000, 20, 20)
#            nx.write_gpickle(G,name)
#            print name
#    for p in ps:
#        for trial in range(5,20):
#            name = "ExK/Results_1/p{}-trial{}.gz".format(str(p),str(trial))
#            G = egograph_connection_model(p, 5000, 2, 2, 2)
#            nx.write_gpickle(G,name)
#            print name
#    for p in ps:
#        for trial in range(5,20):
#            name = "ExK/Results_2/p{}-trial{}.gz".format(str(p),str(trial))
#            G = egograph_connection_model(p, 5000, 5, 5, 2)
#            nx.write_gpickle(G,name)
#            print name    
#    for p in ps:
#        for trial in range(5,20):
#            name = "ExK/Results_3/p{}-trial{}.gz".format(str(p),str(trial))
#            G = egograph_connection_model(p, 5000, 10, 10, 2)
#            nx.write_gpickle(G,name)
#            print name    
#    for p in ps:
#        for trial in range(7,13):
#            name = "ExK/Results_4/p{}-trial{}.gz".format(str(p),str(trial))
#            G = egograph_connection_model(p, 5000, 20, 20, 2)
#            nx.write_gpickle(G,name)
#            print name
#    for p in ps:
#        for trial in range(5,7):
#            name = "ExK/Results_4/p{}-trial{}.gz".format(str(p),str(trial))
#            G = egograph_connection_model(p, 5000, 20, 20, 2)
#            nx.write_gpickle(G,name)
#            print name
#    plt.clf()
#    plt.figure(num=None, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
#    modularity_calc("Results5", ps, 5, "m=2 EGO")
#    modularity_calc("Results6", ps, 5, "m=5 EGO")
#    modularity_calc("Results3", ps, 5, "m=2 TC")
#    modularity_calc("Results4", ps, 5, "m=5 TC")
#    plt.plot(ps, [0.270814107471]*10, label = "m=5 random")
#    plt.plot(ps, [0.521974348281]*10, label = "m=2 random")
#    plt.ylim(0,1)
#    plt.legend(loc = 2)
#    plt.title("Modularity vs p")
#    plt.ylabel("Modularity")
#    plt.xlabel("p")
#    plt.savefig("Compiled.png")
#    plt.savefig("EGO Modularity M=2.png")
#    plt.clf()
#    plt.savefig("EGO Modularity M=5.png")
#    plt.clf()
#    density_calc("Results3",ps,5)
#    density_calc("Results4",ps,5)
#    sam = []
#    for trial in range(20):
#        G = nx.erdos_renyi_graph(5000, 0.000799839967994)
#        sam += [com.modularity(com.best_partition(G), G)]
#    print np.mean(sam)
#    print np.std(sam)
#    sam = []
#    for trial in range(20):
#        G = nx.erdos_renyi_graph(5000, 0.00199727625525)
#        sam += [com.modularity(com.best_partition(G), G)]
#    print np.mean(sam)
#    print np.std(sam)
