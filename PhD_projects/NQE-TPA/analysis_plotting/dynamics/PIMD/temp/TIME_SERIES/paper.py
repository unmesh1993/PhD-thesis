#!/usr/bin/env python3
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
import os

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


os.system('rm check.dat')

tot=int(sys.argv[1])
w=int(sys.argv[2])
e=int(sys.argv[3])
#############1.histogram########################################## 

fig = plt.figure()

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

###

for i in range(1,tot+1):
    res2="del{}".format(i)
    coord=files(res2)

    ptc=coord[:,1]-coord[:,2]


    coord1=[]
    coord2=[]
    cord=[]
    t=0
    for j in range(e,len(ptc),40):
       x1=ptc[j]
       x2=ptc[j+20]
    
       coord1.append(x1)
       coord2.append(x2)
       cord.append(t/2000.0)
       t=t+1
    
    coord1=np.array(coord1,float)
    coord2=np.array(coord2,float)
    cord=np.array(cord,float)
    
    #############
    
    
    ax1 = fig.add_subplot(2,1,1)
    Y1=coord1
    YY1=moving_average(Y1, w)
    ax1.plot(cord[w-1:],YY1,lw=0.5)
    plt.ylabel('$\delta^c_o $ (Å)',size=16)
    ax1.yaxis.label.set_color('black')  
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax1.set_yticks(np.arange(-1.5,1.5,0.5))
    ax1.set_xticks(np.arange(0,28,0.5))
    ax1.set_xlabel(r'Time (ps)',size=16)
    ax1.set_ylim(-0.8,0.8)
    ax1.set_xlim(5,8)
    ax1.tick_params(axis='x', labelsize= 16,colors='black',length=8,width=1.5)
    ax1.tick_params(axis='y', labelsize= 16,colors='black',length=8,width=1.5)
    plt.title('$\delta_1$')
#    ax1.legend(loc=1,prop={'size': 16},ncol=2)

    ax1 = fig.add_subplot(2,1,2)
    Y1=coord2
    YY1=moving_average(Y1, w)
    ax1.plot(cord[w-1:],YY1,lw=0.5)
    plt.ylabel('$\delta^c_o $ (Å)',size=16)
    ax1.yaxis.label.set_color('black')
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax1.set_yticks(np.arange(-1.5,1.5,0.5))
    ax1.set_xticks(np.arange(0,28,0.5))
    ax1.set_xlabel(r'Time (ps)',size=16)
    ax1.set_ylim(-0.8,0.8)
    ax1.set_xlim(5,8)
    ax1.tick_params(axis='x', labelsize= 16,colors='black',length=8,width=1.5)
    ax1.tick_params(axis='y', labelsize= 16,colors='black',length=8,width=1.5)
    plt.title('$\delta_2$')
#    ax1.legend(loc=1,prop={'size': 16},ncol=2)


    
    



################################################################################
plt.subplots_adjust(wspace=0.3,hspace=0.8)
plt.savefig("pimd_70.jpg", dpi=500, bbox_inches = 'tight',    pad_inches = 0.1)
fig.savefig('pimd_70.pdf')
#plt.show()









