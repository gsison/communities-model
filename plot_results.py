# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 20:09:14 2017

@author: Gabriel Sison
"""

import numpy as np
import matplotlib.pyplot as plt

def size(maxi = 21, ylim = (0.0,1.0)):
    data = np.load("size.npy")
    x = np.linspace(1,20,maxi)
    
    for aline in data[0:1]:
        y = np.mean(aline, 0)
        print len(x), len(y)
        ystd = np.std(aline,0)
        plt.errorbar(x, y, yerr=ystd)
#        plt.ylim((0.5,1.0))
        
        plt.ylim((0.0,1.0))
        plt.title("Modularity vs Average Weight")
        plt.ylabel("Average Modularity")
        plt.xlabel("Average Weight")
    
    plt.savefig("Modularity vs Average Weight")
    plt.show()

def stdev(maxi = 20, ylim = (0.0,1.0)):
    data = np.load("STD.npy")
    x = np.linspace(0.1,6.0,maxi)
    
    for aline in data[0:1]:
        y = np.mean(aline, 0)
        ystd = np.std(aline,0)
        plt.errorbar(x, y, yerr=ystd)
#        plt.ylim((0.5,1.0))
        plt.ylim((0.0,1.0))
        plt.title("Modularity vs STDev")
        plt.ylabel("Average Modularity")
        plt.xlabel("Standard Dev")
    
    plt.savefig("Modularity vs Standard Deviation")
    plt.show()

def multidist(maxi = 20, ylim = (0,1.0)):
    data = np.load("commu.npy")
    x = np.linspace(0.1,1.0,maxi)
    
    for aline in data[0:1]:
        y = np.mean(aline, 0)
        ystd = np.std(aline,0)
        plt.errorbar(x, y, yerr=ystd)
#        plt.ylim((0.5,1.0))
        plt.ylim(ylim)
        plt.title("Modularity vs Ratio")
        plt.ylabel("Average Modularity")
        plt.xlabel("Ratio")
    
    plt.savefig("Modularity vs Ratio")
    plt.show()
    return x, y, ystd

def multidist2(maxi = 20, ylim = (0,1.0)):
    data = np.load("ratio.npy")
    x = np.linspace(0.1,1.0,maxi)
    
    for aline in data[0:1]:
        y = np.mean(aline, 0)
        ystd = np.std(aline,0)
        plt.errorbar(x, y, yerr=ystd)
#        plt.ylim((0.5,1.0))
        plt.ylim(ylim)
        plt.title("Modularity vs Ratio")
        plt.ylabel("Average Modularity")
        plt.xlabel("Ratio")
    
    plt.savefig("Modularity vs Ratio")
    plt.show()
    return x, y, ystd

def density(maxi = 20, ylim = (0.0,1.0)):
    data = np.load("density.npy")
    x = np.linspace(0.1,1.0,maxi)
    
    for aline in data[0:1]:
        y = np.mean(aline, 0)
        ystd = np.std(aline,0)
        plt.errorbar(x, y, yerr=ystd)
#        plt.ylim((0.5,1.0))
        plt.ylim(ylim)
        plt.title("Density vs Average Modularity")
        plt.ylabel("Average Modularity")
        plt.xlabel("Density")
    
    plt.savefig("Density vs Average Weight")
    plt.show()
    return x, y, ystd

def BA():
    data = np.load("barabasi.npy")
    x = np.linspace(0.1,1.0,19)
    
    for aline in data[0:1]:
        y = np.mean(aline, 0)[:19]
        print len(y)
        ystd = np.std(aline,0)[:19]
        plt.errorbar(x, y, yerr=ystd)
        plt.ylim((0.0,1.0))
        plt.title("Delta vs Average Modularity")
        plt.ylabel("Average Modularity")
        plt.xlabel("Delta")
    
    plt.savefig("Delta vs Modularity")
    plt.show()
    
def BA2(ylim = (0.0,1.0)):
    data = np.load("cbarabasi.npy")
    x = np.linspace(0.1,1.0,19)
    
    for aline in data[0:1]:
        y = np.mean(aline, 0)[:19]
        print len(y)
        ystd = np.std(aline,0)[:19]
        plt.errorbar(x, y, yerr=ystd)
        plt.ylim((0.0,1.0))
        plt.title("Sigma vs Average Modularity")
        plt.ylabel("Average Modularity")
        plt.xlabel("Sigma")
    
    plt.savefig("Sigma vs Modularity")
    plt.show()

def BA3():
    data = np.load("clbarabasi.npy")
    x = np.linspace(0.1,1.0,19)
    
    for aline in data[0:1]:
        y = np.mean(aline, 0)[:19]
        print len(y)
        ystd = np.std(aline,0)[:19]
        plt.errorbar(x, y, yerr=ystd)
        plt.ylim((0.0,0.2))
        plt.title("Sigma vs Average Clustering")
        plt.ylabel("Average Clustering")
        plt.xlabel("Sigma")
    
    plt.savefig("Sigma vs Average Clustering")
    plt.show()

a, b, c = density(20,(0,0.2))
plt.errorbar(a,b,c)
e, f, g = multidist(ylim = (0,0.2))

plt.clf()

#
#plt.errorbar(a,b,c)
#plt.ylim((0,0.2))
#plt.errorbar(e,f,g, label = "Distinct Communities, Density = 95%")
#plt.title("Density vs Average Modularity")
#plt.ylabel("Average Modularity")
#plt.xlabel("Density")
#plt.legend()
#plt.show()

multidist2(5, ylim = (0,0.2))