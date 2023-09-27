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
#from mpl_toolkits.mplot3d import Axes3D # This import has side effects required for the kwarg projection='3d' in the call to fig.add_subplot
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import random
import sys
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter



import os

###################################################################################
tot=np.int(sys.argv[1])
###################################################################################

def safe_ln(x, minval=10**(-50)):
    return np.log(x.clip(min=minval))

def files(res2):
        f=open(res2,'r')
        a=f.readlines()
        f.close
        coord1=[]
        coord2=[]
        coord3=[]
        for t in range(len(a)):
              x=a[t].split()
              coord1.append(x[1])
              coord2.append(x[2])
              coord3.append(x[3])
        del x

        coord1=np.array(coord1,float)
        coord2=np.array(coord2,float)
        coord3=np.array(coord3,float)
        return (-1*coord1,coord2,coord3)

def files2(res2):
        f=open(res2,'r')
        a=f.readlines()
        f.close
        coord1=[]
        coord2=[]
        coord3=[]
        for t in range(len(a)):
              x=a[t].split()

              coord1.append(x[1])
              coord2.append(x[2])
              coord3.append(x[3])
        del x

        coord1=np.array(coord1,float)
        coord2=np.array(coord2,float)
        coord3=np.array(coord3,float)
        return (-1*coord1,coord2,coord3)

############################
fig = plt.figure()

for i in range(1,tot+1):
    res2="del{}".format(i)
    if i==1:
       x0,y0,z0=files(res2)
    elif i==2:
       x0,y0,z0=files2(res2)

############################################    
    gg,xedges,yedges=np.histogram2d(x0, y0, bins=(100,100),range=[[-1.5, 1.5], [0, 2]], normed=True)
    gg= gg.T ###transpose (please find reason)
    ggg,xedges,yedges=np.histogram2d(x0, z0, bins=(100,100),range=[[-1.5, 1.5], [0,2]], normed=True)
    ggg= ggg.T ###transpose (please find reason)
    ##########################################################################

    ax = fig.add_subplot(2,2,i)

    xcenters = (xedges[:-1] + xedges[1:]) / 2
    ycenters = (yedges[:-1] + yedges[1:]) / 2
    X, Y = np.meshgrid(xcenters, ycenters)
    plt.axvline(x=0.0, color = 'k',linewidth=1.0, linestyle = '--')
    plt.xlim(-1.5,1.5)
    plt.ylim(0.3,1.6)
    plt.xlabel(r'$\delta_{1,2}$ (Å)',size=14)
    plt.ylabel(r'$d_{X-H}$ (Å)',size=14)
    plt.xticks(np.arange(-1.5,1.6,1.0),size=12)
    plt.yticks(np.arange(0.2,2.0,0.4),size=12)
#    plt.title(legend,size=14)


    plt.contourf(X, Y, ggg, [0.001,0.01,0.1,1,10,100,1000], cmap=plt.cm.get_cmap('Blues'),norm = LogNorm(),alpha=0.5)
    plt.contour(X, Y, ggg, [0.001,0.01,0.1,1,10,100,1000], cmap=plt.cm.get_cmap('Blues'),norm = LogNorm(),alpha=0.5)

    plt.contourf(X, Y, gg, [0.001,0.01,0.1,1,10,100,1000], cmap=plt.cm.get_cmap('Greens'),norm = LogNorm(),alpha=0.5)
    plt.contour(X, Y, gg, [0.001,0.01,0.1,1,10,100,1000], cmap=plt.cm.get_cmap('Greens'),norm = LogNorm(),alpha=0.5)

#    cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
#    cbar.ax.tick_params(labelsize=6)
#    cbar.set_label(r'prob. density ', size=14)


    del X,Y,gg,xcenters,ycenters,xedges,yedges
####################################################################

for i in range(1,tot+1):
    res2="ddel{}".format(i)
    x0,y0,z0=files(res2)

############################################    
    gg,xedges,yedges=np.histogram2d(x0, y0, bins=(100,100),range=[[-1.5, 1.5], [0, 2]], normed=True)
    gg= gg.T ###transpose (please find reason)
    ggg,xedges,yedges=np.histogram2d(x0, z0, bins=(100,100),range=[[-1.5, 1.5], [0,2]], normed=True)
    ggg= ggg.T ###transpose (please find reason)
    ##########################################################################
    ax = fig.add_subplot(2,2,i+2)
  

    xcenters = (xedges[:-1] + xedges[1:]) / 2
    ycenters = (yedges[:-1] + yedges[1:]) / 2
    X, Y = np.meshgrid(xcenters, ycenters)

    plt.axvline(x=0.0, color = 'k',linewidth=1.0, linestyle = '--')
    plt.xlim(-1.5,1.5)
    plt.ylim(0.3,1.6)
    plt.xlabel(r'$\delta_{1,2}$ (Å)',size=14)
    plt.ylabel(r'$d_{X-H}$ (Å)',size=14)
    plt.xticks(np.arange(-1.5,1.6,1.0),size=12)
    plt.yticks(np.arange(0.2,2.0,0.4),size=12)
#    plt.title(legend,size=14)


    plt.contourf(X, Y, ggg, [0.001,0.01,0.1,1,10,100,1000], cmap=plt.cm.get_cmap('Blues'),norm = LogNorm(),alpha=0.5)
    plt.contour(X, Y, ggg, [0.001,0.01,0.1,1,10,100,1000], cmap=plt.cm.get_cmap('Blues'),norm = LogNorm(),alpha=0.5)

    plt.contourf(X, Y, gg, [0.001,0.01,0.1,1,10,100,1000], cmap=plt.cm.get_cmap('Greens'),norm = LogNorm(),alpha=0.5)
    plt.contour(X, Y, gg, [0.001,0.01,0.1,1,10,100,1000], cmap=plt.cm.get_cmap('Greens'),norm = LogNorm(),alpha=0.5)

#    cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
#    cbar.ax.tick_params(labelsize=6)
#    cbar.set_label(r'prob. density ', size=14)


    del X,Y,gg,xcenters,ycenters,xedges,yedges
####################################################################





plt.subplots_adjust(wspace=0.7,hspace=0.7)
fig.savefig('fig_conv_1_1.pdf')
plt.savefig("fig_conv_1_1.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
#plt.show()

