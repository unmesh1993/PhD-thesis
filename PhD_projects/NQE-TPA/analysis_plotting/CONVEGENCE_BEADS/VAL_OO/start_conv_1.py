# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:41:36 2018

@author: unmesh
"""
import numpy as np
import matplotlib 
matplotlib.use('Agg')
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D # This import has side effects required for the kwarg projection='3d' in the call to fig.add_subplot
import matplotlib.pyplot as plt
import random
import sys
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#from sklearn.neighbors.kde import KernelDensity
#from scipy.stats import gaussian_kde
#from scipy.stats import kurtosis, skew


import os

os.system('rm log_1.dat')
###################################################################################
tot=np.int(sys.argv[1])
fold=np.int(sys.argv[2])
beads=np.array(str(sys.argv[3]).split(','),int)
sec=str(sys.argv[4]).split(',')
temp=np.array(str(sys.argv[5]).split(','),float)
dim=np.int(sys.argv[6])
###################################################################################


def files(res2):
        f=open(res2,'r')
        a=f.readlines()
        f.close
        
        coord=[]
        for i in range(0,len(a)):
            x=a[i].split()
            coord.append(x)
        coord=np.array(coord,float)
        return (coord)

##################################################################
#############1.histogram########################################## 
new_colour = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf']

fig = plt.figure()

gg=np.zeros((tot,20),float)
min02=np.zeros((tot),float)
max02=np.zeros((tot),float)
mean02=np.zeros((tot),float)
std02=np.zeros((tot),float)




for i in range(1,tot+1):
    res2="del{}".format(i)
    coord=files(res2)

    x0=coord[:,3]
    min02[i-1]=np.amin(x0)
    max02[i-1]=np.amax(x0)
    mean02[i-1]=np.mean(x0)
    std02[i-1]=np.std(x0)
    del x0
####################################################################################################################################

ax1 = fig.add_subplot(311)

plt.errorbar(beads,mean02,yerr=std02,markersize=4, capsize=4,fmt='--or',mfc='white')

ax1.set_xscale('log', basex=2)
plt.xticks(beads,sec,size=10)

for i, txt in enumerate(mean02.round(decimals=2)):
    x, y = beads[i], mean02[i]
    text = ' μ={:.2f}\n σ={:.2f}'.format(mean02[i], std02[i])
    ax1.annotate(text, xy=(x,y),size=7,weight='bold',color='blue')

plt.ylabel(r'$d_{O-O}$ (Å)',size=10)
plt.xlabel('Number of beads (P)',size=10)

####################################################################################################################################

for i in range(1,tot+1):
    res2="del{}".format(i)
    coord=files(res2)

    x0=coord[:,4]
    min02[i-1]=np.amin(x0)
    max02[i-1]=np.amax(x0)
    mean02[i-1]=np.mean(x0)
    std02[i-1]=np.std(x0)
    del x0
####################################################################################################################################

ax1 = fig.add_subplot(312)

plt.errorbar(beads,mean02,yerr=std02,markersize=4, capsize=4,fmt='--or',mfc='white')

ax1.set_xscale('log', basex=2)
plt.xticks(beads,sec,size=10)

for i, txt in enumerate(mean02.round(decimals=2)):
    x, y = beads[i], mean02[i]
    text = ' μ={:.0f}\n σ={:.0f}'.format(mean02[i], std02[i])
    ax1.annotate(text, xy=(x,y),size=7,weight='bold',color='blue')

plt.ylabel(r'$\angle OHO$ ($^{\circ}$)',size=10)
plt.xlabel('Number of beads (P)',size=10)

####################################################################################################################################






plt.subplots_adjust(wspace=0.4,hspace=0.6)
fig.savefig('fig_conv_1_1.pdf')
plt.savefig("fig_conv_1_1.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
#plt.show()

