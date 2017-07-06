# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:42:35 2017

@author: Gabriel Sison
"""
import matplotlib.pyplot as plt
import ego_gen as eg
import numpy as np

def read_files(afile):
    with open(afile, 'r') as inp:
        x = inp.readlines()
    means, std = x[0], x[1]
    means = means.strip().strip('[').strip(']').split(",")
    means = [np.float(v.strip()) for v in means]
    std = std.strip('[]').split(",")
    std = [np.float(v.strip()) for v in std]
    return means, std

def plot_file(Folder, ps, label, m = None, color = None):
    if m is None:
        m = ""
    afile = Folder+"{}.txt".format(str(m))
    means, std = read_files(afile)
    if color is not None:
        plt.errorbar(ps, means, yerr = std, label = label, color = color)
    else:
        plt.errorbar(ps, means, yerr = std, label = label)

if __name__ == "__main__":
    ps = np.linspace(0.05,1.0,20)
#    
#    eg.density_calc("ExK2/Results_1", ps, 1, "m=2 Global")
#    eg.density_calc("ExK2/Results_2", ps, 1, "m=5 Global")
#    eg.density_calc("ExK2/Results_3", ps, 1, "m=10 Global")
#    eg.density_calc("ExK2/Results_4", ps, 1, "m=20 Global")
#    plt.clf()
#    eg.density_calc("Results5", ps, 20, "m=2 EGO")
#    eg.density_calc("Results6", ps, 20, "m=5 EGO")
#    eg.density_calc("Results3", ps, 20, "m=2 TC")
#    eg.density_calc("Results4", ps, 20, "m=5 TC")
#    plt.clf()
#    eg.density_calc("Results5", ps, 20, "m=10 EGO", 10)
#    eg.density_calc("Results6", ps, 20, "m=20 EGO", 20)
#    eg.density_calc("Results3", ps, 20, "m=10 TC", 10)
#    eg.density_calc("Results4", ps, 20, "m=20 TC", 20)
#    plt.clf()
#    eg.density_calc("ExK/Results_1", ps, 20, "m=2 EGO2")
#    eg.density_calc("ExK/Results_2", ps, 20, "m=5 EGO2")
#    eg.density_calc("ExK/Results_3", ps, 20, "m=10 EGO2")
#    eg.density_calc("ExK/Results_4", ps, 20, "m=20 EGO2")

    plt.clf()
#    eg.modularity_calc("ExK/Results_4", ps, 20, "m=10 EGO2")
    plt.figure(num=None, figsize=(12, 12), dpi=80, 
               facecolor='w', edgecolor='k')
    plot_file("Results5", ps, "m=2 EGO", color = "blue")
    plot_file("Results3", ps, "m=2 TC",  color = "green")
    plot_file("ExK/Results_1", ps, "m=2 EGO2",  color = "red")
#    plot_file("ExK2/Results_1", ps, "m=2 Global")
    plt.plot(ps, [0.521974348281]*20, label = "m=2 random", c= "cyan")
    plt.ylim(0,1)
    plt.legend(loc = 2)
    plt.title("Modularity vs p")
    plt.ylabel("Modularity")
    plt.xlabel("p")
    plt.savefig("M=2.png")
    plt.clf()

    plt.figure(num=None, figsize=(12, 12), dpi=80, 
               facecolor='w', edgecolor='k')
    plot_file("Results6", ps, "m=5 EGO", color = "blue")
    plot_file("Results4", ps, "m=5 TC",  color = "green")
    plot_file("ExK/Results_2", ps, "m=5 EGO2",  color = "red")
#    plot_file("ExK2/Results_2", ps, "m=2 Global")
    plt.plot(ps, [0.270814107471]*20, label = "m=5 random", c= "cyan")
    plt.ylim(0,1)
    plt.legend(loc = 2)
    plt.title("Modularity vs p")
    plt.ylabel("Modularity")
    plt.xlabel("p")
    plt.savefig("M=5.png")
    plt.clf()

    plt.figure(num=None, figsize=(12, 12), dpi=80, 
               facecolor='w', edgecolor='k')
    plot_file("Results5", ps, "m=10 EGO", m = 10, color = "blue")
    plot_file("Results3", ps, "m=10 TC", m = 10,  color = "green")
    plot_file("ExK/Results_3", ps, "m=10 EGO2",  color = "red")
#    plot_file("ExK2/Results_3", ps, "m=10 Global")
    plt.plot(ps, [0.179784240619]*20, label = "m=10 random", c= "cyan")
    plt.ylim(0,1)
    plt.legend(loc = 2)
    plt.title("Modularity vs p")
    plt.ylabel("Modularity")
    plt.xlabel("p")
    plt.savefig("M=10.png")
    plt.clf()


    plt.figure(num=None, figsize=(12, 12), dpi=80, 
               facecolor='w', edgecolor='k')
    plot_file("Results6", ps, "m=20 EGO", m = 20, color = "blue")
    plot_file("Results4", ps, "m=20 TC", m = 20,  color = "green")
    plot_file("ExK/Results_4", ps, "m=20 EGO2",  color = "red")
 #   plot_file("ExK2/Results_4", ps, "m=20 Global")
    plt.plot(ps, [0.142141155424]*20, label = "m=20 random", c= "cyan")
    plt.ylim(0,1)
    plt.legend(loc = 2)
    plt.title("Modularity vs p")
    plt.ylabel("Modularity")
    plt.xlabel("p")
    plt.savefig("M=20.png")
    plt.clf()
    plt.savefig("all.png")
#    eg.modularity_calc("Results5", ps, 5, "m=2 EGO")
#    eg.modularity_calc("Results6", ps, 5, "m=5 EGO")
#    eg.modularity_calc("Results3", ps, 5, "m=2 TC")
#    eg.modularity_calc("Results4", ps, 5, "m=5 TC")
#    eg.modularity_calc("Results5", ps, 5, "m=10 EGO", 10)
#    eg.modularity_calc("Results6", ps, 5, "m=20 EGO", 20)
#    eg.modularity_calc("Results3", ps, 5, "m=10 TC", 10)
#    eg.modularity_calc("Results4", ps, 5, "m=20 TC", 20)
#    eg.modularity_calc("ExK/Results_1", ps, 5, "m=2 EGO2")
#    eg.modularity_calc("ExK/Results_2", ps, 5, "m=5 EGO2")
#    eg.modularity_calc("ExK/Results_3", ps, 5, "m=10 EGO2")
#    try:
#        eg.modularity_calc("ExK/Results_4", ps, 5, "m=20 EGO2")
#    except Exception as e:
#        pass
#    plt.plot(ps, [0.270814107471]*20, label = "m=5 random")
#    plt.plot(ps, [0.521974348281]*20, label = "m=2 random")
#    plt.ylim(0,1)
#    plt.legend(loc = 2)
#    plt.title("Modularity vs p")
#    plt.ylabel("Modularity")
#    plt.xlabel("p")
#    plt.savefig("Compiled3.png")
    
    pass
