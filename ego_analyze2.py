# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:42:35 2017

@author: Gabriel Sison
"""
import matplotlib.pyplot as plt
import networkx as nx
import community as com
import numpy as np

import seaborn as sns
sns.set(color_codes=True)


def read_files(afile):
    with open(afile, 'r') as inp:
        x = inp.readlines()
    means, std = x[0], x[1]
    means = means.strip().strip('[').strip(']').split(",")
    means = [np.float(v.strip()) for v in means]
    std = std.strip('[]').split(",")
    std = [np.float(v.strip()) for v in std]
    return means, std

def com_count(Folder, ps, trials = 5, label = "", m = None):
    means = []
    stds = []
    for p in ps:
        coms = []
        for trial in range(trials):
            if m is None:
                name = "{}/p{}-trial{}.gz".format(Folder,str(p),str(trial))
            else:
                name = "{}/m{}p{}-trial{}.gz".format(Folder,str(m),str(p),
                                                    str(trial))
            G = nx.read_gpickle(name)
            coms += [np.max(com.best_partition(G).values()) + 1]
            print name
        means = means + [np.mean(coms)]
        stds = stds + [np.std(coms)]
    plt.errorbar(ps,means,yerr = stds, label=label)
    if m is None:
        m = ""
    with open(Folder+"{}comcount.txt".format(str(m)), 'w') as output:
        output.write(str(means))
        output.write("\n")
        output.write(str(stds))

def plot_file(Folder, ps, label, m = None, color = None):
    if m is None:
        m = ""
    afile = Folder+"{}comcount.txt".format(str(m))
    means, std = read_files(afile)
    if color is not None:
        plt.errorbar(ps, means, yerr = std, label = label, color = color)
    else:
        plt.errorbar(ps, means, yerr = std, label = label)

if __name__ == "__main__":
    ps = np.linspace(0.05,1.0,20)
#    com_count("Results5", ps, 5, "m=2 EGO")
#    com_count("Results6", ps, 5, "m=5 EGO")
#    com_count("Results3", ps, 5, "m=2 TC")
#    com_count("Results4", ps, 5, "m=5 TC")
#    com_count("Results5", ps, 5, "m=10 EGO", 10)
#    com_count("Results6", ps, 5, "m=20 EGO", 20)
#    com_count("Results3", ps, 5, "m=10 TC", 10)
#    com_count("Results4", ps, 5, "m=20 TC", 20)
#    com_count("ExK/Results_1", ps, 5, "m=2 EGO2")
#    com_count("ExK/Results_2", ps, 5, "m=5 EGO2")
#    com_count("ExK/Results_3", ps, 5, "m=10 EGO2")
#    com_count("ExK/Results_4", ps, 5, "m=20 EGO2")
#    com_count("ExK2/Results_1", ps, 5, "m=2 EGO2")
#    com_count("ExK2/Results_2", ps, 5, "m=5 EGO2")
#    com_count("ExK2/Results_3", ps, 5, "m=10 EGO2")
#    com_count("ExK2/Results_4", ps, 5, "m=20 EGO2")
#    plt.legend()
#    plt.plot()
    plot_file("Results5", ps, "m=2 EGO", color = "blue")
    plot_file("Results3", ps, "m=2 TC",  color = "green")
    plot_file("ExK/Results_1", ps, "m=2 EGO2",  color = "red")
    plot_file("ExK2/Results_1", ps, "m=2 Global", color = "black")
    plt.legend()
    plt.ylim(ymin = 0)
    
    pass
