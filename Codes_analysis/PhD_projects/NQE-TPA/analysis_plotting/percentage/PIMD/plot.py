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

#from sklearn.neighbors.kde import KernelDensity
#from scipy.stats import gaussian_kde
#from scipy.stats import kurtosis, skew


import os

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w



tot=int(sys.argv[1])
w=int(sys.argv[2])
sec=str(sys.argv[3]).split(',')
e=int(sys.argv[4])
#############1.histogram########################################## 

fig = plt.figure()

countx=np.zeros((tot,20),float)
county=np.zeros((tot,20),float)

countxx=np.zeros((tot,20),float)
countyy=np.zeros((tot,20),float)

for i in range(1,tot+1):
    res2="del{}".format(i)

    f=open(res2,'r')
    a=f.readlines()
    f.close

    frames=int(len(a)/e)
    cord=np.zeros((40,frames),float)

    for j in range(0,frames):
       for k in range (0,40):
           tt=j*40+k
           x=a[tt].split()
           x=np.array(x,float)
           cord[k][j]=-x[0]

    for j in range(20):
           a=cord[j][:]
           b1=a[a > 0]
           b2=a[a <= 0]
           countxx[i-1][j] = (len(b1)/frames)*100
    
    for j in range(20,40):
           a=cord[j][:]
           b1=a[a > 0]
           b2=a[a <= 0]
           countyy[i-1][j-20] = (len(b1)/frames)*100


    leo=np.zeros(4,int)
    for j in range(0,40,2):
        for k in range(frames):
           a1=cord[j][k]
           a2=cord[j+1][k]

           if a1 <= 0 and a2 <= 0:
               leo[0]=leo[0]+1
           if a1 <= 0 and a2 > 0:
               leo[1]=leo[1]+1
           if a1 > 0 and a2 <= 0:
               leo[2]=leo[2]+1
           if a1 > 0 and a2 > 0:
               leo[3]=leo[3]+1

          


    cool=np.ravel(cord)
    b1=cool[cool > 0]

    print ('temp=', sec[i-1],(len(b1)/(40*frames)))
    print (np.round(countxx[i-1][:],1))
    print (np.round(countyy[i-1][:],1))
    print (leo[0]/(20*frames)+leo[3]/(20*frames),leo[1]/(20*frames)+leo[2]/(20*frames))



