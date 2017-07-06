# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 19:08:10 2017

@author: Gabriel Sison
"""

#import networkx as nx
import numpy as np
import numpy.random as rand
import community as com
import barabasi_gen as bg
import matplotlib.pyplot as plt
import networkx as nx

import graph_gen as gg

def get_max_edges(N, density):
    return int(N*N*(0.5)*density) + 1

def meansim(N, density, count, trials = 30):
    means = np.linspace(1,20,count)
    scales = means/10
    
    data = np.zeros((3,trials,count))

    null1 = {}
    null2 = {}
    for i in range(400):
        null1[i] = 0
        null2[i] = i
    inc = 0
    for mean, scale in zip(means, scales):
        for trial in range(trials):
            print mean, trial
            Ne = get_max_edges(N, density)
            weights = rand.normal(mean, scale, Ne).clip(min = 0)
            g = gg.rand_dense_graph(N,density,weights)
            data[0,trial,inc] = com.modularity(com.best_partition(g), g)
            data[1,trial,inc] = com.modularity(null1, g)
            data[2,trial,inc] = com.modularity(null2, g)
            if not trial:
                plt.hist(weights)
                plt.savefig('EW'+str(mean).zfill(4)+'.png')
                plt.clf()
        inc += 1
    np.save("size", data)
    
def scalesim(N, mean, density, count, trials = 5):
    scales = np.linspace(0.1,5.0,count)*mean
    data = np.zeros((3,trials,count))

    null1 = {}
    null2 = {}
    for i in range(400):
        null1[i] = 0
        null2[i] = i
    inc = 0
    for scale in scales:
        for trial in range(trials):
            print scale, trial
            Ne = get_max_edges(N, density)
            weights = rand.normal(mean, scale, Ne).clip(min = 0)
            g = gg.rand_dense_graph(N,density,weights)
            data[0,trial,inc] = com.modularity(com.best_partition(g), g)
#            data[1,trial,inc] = com.modularity(null1, g)
#            data[2,trial,inc] = com.modularity(null2, g)
            if not trial:
                plt.hist(weights)
                plt.savefig('EWSTD'+str(mean).zfill(4)+'.png')
                plt.clf()
        inc += 1
    np.save("STD", data)    

def densim(N, mean, count, trials = 30):
    scale = mean/10.
    
    data = np.zeros((3,trials,count))
    densities = np.linspace(0.1,1,count)    
    
    null1 = {}
    null2 = {}
    for i in range(400):
        null1[i] = 0
        null2[i] = i
    inc = 0
    for density in densities:
        for trial in range(trials):
            print density, trial
            Ne = get_max_edges(N, density)
            weights = rand.normal(mean, scale, Ne).clip(min = 0)
            g = gg.rand_dense_graph(N,density,weights)
            data[0,trial,inc] = com.modularity(com.best_partition(g), g)
            data[1,trial,inc] = com.modularity(null1, g)
            data[2,trial,inc] = com.modularity(null2, g)
            if not trial:
                plt.hist(weights)
                plt.savefig('EW'+str(mean).zfill(4)+'.png')
                plt.clf()
        inc += 1
    np.save("density", data)

def multidistsim(N, mean1, mean2, density, count, trials = 30):
    scale1 = mean1/10.
    scale2 = mean2/10.
    
    data = np.zeros((3,trials,count))
    ratios = np.linspace(0.1,1,count)    
    
    null1 = {}
    null2 = {}
    for i in range(400):
        null1[i] = 0
        null2[i] = i
    inc = 0
    for ratio in ratios:
        for trial in range(trials):
            print ratio, trial
            Ne = get_max_edges(N, density)
            N1 = int(Ne*ratio)
            N2 = Ne - N1
            weight1 = rand.normal(mean1, scale1, N1).clip(min = 0)
            weight2 = rand.normal(mean2, scale2, N2).clip(min = 0)
            weights = weight1.tolist() + weight2.tolist()
            g = gg.rand_dense_graph(N,density,weights)
            data[0,trial,inc] = com.modularity(com.best_partition(g), g)
            data[1,trial,inc] = com.modularity(null1, g)
            data[2,trial,inc] = com.modularity(null2, g)
            if not trial:
                plt.hist(weights)
                plt.savefig('Multi'+str(ratio).ljust(4,'0')+'.png')
                plt.clf()
        inc += 1
    np.save("ratio", data)
    
def multidistsim2(N, mean1, mean2, density, count, trials = 30):
    scale1 = mean1/10.
    scale2 = mean2/10.
    
    data = np.zeros((3,trials,count))
    ratios = np.linspace(0.1,1,count)    
    
    null1 = {}
    null2 = {}
    for i in range(400):
        null1[i] = 0
        null2[i] = i
    inc = 0
    for ratio in ratios:
        for trial in range(trials):
            print ratio, trial
            Ne = get_max_edges(N, density)
            N1 = int(Ne*ratio)
            N2 = Ne - N1
            weight1 = rand.normal(mean1, scale1, N1).clip(min = 0)
            weight2 = rand.normal(mean2, scale2, N2).clip(min = 0)
            weights = weight1.tolist() + weight2.tolist()
            g = gg.rand_dense_graph(N,density,weights)
            data[0,trial,inc] = com.modularity(com.best_partition(g), g)
            data[1,trial,inc] = com.modularity(null1, g)
            data[2,trial,inc] = com.modularity(null2, g)
            if not trial:
                plt.hist(weights)
                plt.savefig('Multi'+str(ratio).ljust(4,'0')+'.png')
                plt.clf()
        inc += 1
    np.save("ratio", data)

def comu_sim(N, mean1, mean2, density, count, trials = 30):
    scale1 = mean1/10.
    scale2 = mean2/10.
    
    data = np.zeros((3,trials,count))
    ratios = np.linspace(0.1,1,count)    
    
    null1 = {}
    null2 = {}
    for i in range(400):
        null1[i] = 0
        null2[i] = i
    inc = 0
    for ratio in ratios:
        for trial in range(trials):
            print ratio, trial
            Ne = get_max_edges(N, density)
            weight1 = rand.normal(mean1, scale1, Ne).clip(min = 0).tolist()
            weight2 = rand.normal(mean2, scale2, Ne).clip(min = 0).tolist()
            g = gg.rand_dense_graph_com(N,density,weight1, weight2)
            data[0,trial,inc] = com.modularity(com.best_partition(g), g)
            data[1,trial,inc] = com.modularity(null1, g)
            data[2,trial,inc] = com.modularity(null2, g)
#            if not trial:
#                plt.hist(weights)
#                plt.savefig('Multi'+str(ratio).ljust(4,'0')+'.png')
#                plt.clf()
        inc += 1
    np.save("commu", data)

def basim(N, M, count):
    trials = 30
    data = np.zeros((3,trials,count))
    deltas = np.linspace(0.1,1.,count)
    M = 10
    
    null1 = {}
    null2 = {}
    for i in range(400):
        null1[i] = 0
        null2[i] = i
    inc = 0
    for delta in deltas:
        for trial in range(trials):
            print trial
            g = bg.weighted_barabasi(N,M,delta)
            data[0,trial,inc] = com.modularity(com.best_partition(g), g)
            data[1,trial,inc] = com.modularity(null1, g)
            data[2,trial,inc] = com.modularity(null2, g)
            if not trial:
                weights = nx.degree(g, weight = "weight").values()
                plt.hist(weights)
                plt.savefig('EWBA'+str(delta).zfill(4)+'.png')
                plt.clf()
        inc += 1
    np.save("barabasi", data)

def basim2(N, M, count, delta, trials = 30):
    
    data = np.zeros((3,trials,count))
    sigmas = np.linspace(0.1,1.,count)
    M = 10
    
    null1 = {}
    null2 = {}
    for i in range(400):
        null1[i] = 0
        null2[i] = i
    inc = 0
    for sigma in sigmas:
        for trial in range(trials):
            print trial
            g = bg.weighted_cbarabasi(N,M,delta,sigma)
            data[0,trial,inc] = com.modularity(com.best_partition(g), g)
            data[1,trial,inc] = com.modularity(null1, g)
            data[2,trial,inc] = com.modularity(null2, g)
            if not trial:
                weights = nx.degree(g, weight = "weight").values()
                plt.hist(weights)
                plt.savefig('EWBAC'+str(delta).zfill(4)+'.png')
                plt.clf()
        inc += 1
    np.save("cbarabasi", data)

def basim2c(N, M, count, delta, trials = 30):
    
    data = np.zeros((3,trials,count))
    sigmas = np.linspace(0.1,1.,count)
    M = 10
    
    null1 = {}
    null2 = {}
    for i in range(400):
        null1[i] = 0
        null2[i] = i
    inc = 0
    for sigma in sigmas:
        for trial in range(trials):
            print trial
            g = bg.weighted_cbarabasi(N,M,delta,sigma)
            data[0,trial,inc] = nx.average_clustering(g)
#            data[1,trial,inc] = com.modularity(null1, g)
#            data[2,trial,inc] = com.modularity(null2, g)
            if not trial:
                weights = nx.degree(g, weight = "weight").values()
                plt.hist(weights)
                plt.savefig('EWBAC'+str(delta).zfill(4)+'.png')
                plt.clf()
        inc += 1
    np.save("clbarabasi", data)




if __name__ == "__main__":
    N = 400
    density = 0.95
    mean = 1.0
    mean1 = 1.0
    mean2 = 8.0
    
#    count = 20
#    meansim(N, density, count)

    count = 5
    trials = 5
#    scalesim(N, mean, density, count, trials = trials)
#    densim(N, mean, count, trials = trials)
    multidistsim2(N, mean1, mean2, density, count, trials = trials)
#    multidistsim2(N, mean1, mean2, density, count, trials = trials)
#    comu_sim(N, mean1, mean2, density, count, trials = trials)
#    basim2c(400,10,20,0.5)
