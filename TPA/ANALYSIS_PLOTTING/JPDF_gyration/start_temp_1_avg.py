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
from matplotlib.colors import LogNorm


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
for i in range(1,tot+1):
    res2="del{}".format(i)
    coord=files(res2)
    x0=coord[:,0]
    yyy0=coord[:,3]
    xxx0=-x0

    fold=1
    x0=np.split(xxx0,fold)
    y0=np.split(yyy0,fold)

    ax = fig.add_subplot(3,2,i)
    for axis in ['top','bottom','left','right']:
       ax.spines[axis].set_linewidth(2)
    gg=np.zeros((100,100),float)
    for j in range(fold):
        ggg,xedges,yedges=np.histogram2d(x0[j], y0[j], bins=(100,100),range=[[-1.5,1.5], [0.0,0.8]], normed=True)
        ggg=ggg.T
        gg=gg+ggg/fold

    xcenters = (xedges[:-1] + xedges[1:]) / 2
    ycenters = (yedges[:-1] + yedges[1:]) / 2
    X, Y = np.meshgrid(xcenters, ycenters)

    legend=sec[i-1]


    plt.xticks(np.arange(-1.5,1.6,0.5),size=16)
    plt.yticks(np.arange(0,0.5,0.2),size=16)
#    plt.xlabel(r'$\delta^c_o$ (Å)',size=16)
    if i ==1:
       plt.ylabel(r'$r_G$ (Å)',size=16)
    plt.xlim(-0.8,0.8)
    plt.ylim(0.00,0.401)
    ax.tick_params(axis='x', labelsize= 16,colors='black',width=2,length=8)
    ax.tick_params(axis='y', labelsize= 16,colors='black',width=2,length=8)
    plt.axvline(x=0.0, color = 'k',linewidth=2, linestyle = '--')

    plt.contourf(X, Y, gg, [0.01,0.1,1,10,100],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
    CS=ax.contour(X, Y, ggg, [0.01,0.1,1,10,100],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
    cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
    if i==2:
       cbar.ax.tick_params(labelsize=12)
       cbar.set_label(r'prob. density ', size=12)


    del X,Y,xcenters,ycenters,xedges,yedges,x0,y0

#plt.subplots_adjust(wspace=0.3,hspace=0.3)
#fig.savefig('fig_conv_1_1.pdf')
#plt.savefig("fig_conv_1_1.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)

########################################################################################
#fig = plt.figure()
for i in range(1,tot+1):
    res2="del{}".format(i)
    coord=files(res2)
    x0=coord[:,0]
    yyy0=coord[:,4]
    xxx0=-x0

    fold=1
    x0=np.split(xxx0,fold)
    y0=np.split(yyy0,fold)

    ax = fig.add_subplot(3,2,i+2)
    for axis in ['top','bottom','left','right']:
       ax.spines[axis].set_linewidth(2)

    gg=np.zeros((100,100),float)
    for j in range(fold):
        ggg,xedges,yedges=np.histogram2d(x0[j], y0[j], bins=(100,100),range=[[-1.5,1.5], [0.0,0.8]], normed=True)
        ggg=ggg.T
        gg=gg+ggg/fold


    xcenters = (xedges[:-1] + xedges[1:]) / 2
    ycenters = (yedges[:-1] + yedges[1:]) / 2
    X, Y = np.meshgrid(xcenters, ycenters)

    legend=sec[i-1]


    plt.xticks(np.arange(-1.5,1.6,0.5),size=16)
    plt.yticks(np.arange(0,0.5,0.2),size=16)
#    plt.xlabel(r'$\delta^c_o$ (Å)',size=16)
    if i==1:
       plt.ylabel(r'$r_G^{\parallel}$ (Å)',size=16)
    plt.xlim(-0.8,0.8)
    plt.ylim(0.00,0.401)
    ax.tick_params(axis='x', labelsize= 16,colors='black',width=2,length=8)
    ax.tick_params(axis='y', labelsize= 16,colors='black',width=2,length=8)
    plt.axvline(x=0.0, color = 'k',linewidth=2, linestyle = '--')

    plt.contourf(X, Y, gg, [0.01,0.1,1,10,100],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
    CS=ax.contour(X, Y, ggg, [0.01,0.1,1,10,100],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
    cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
    if i ==2:
        cbar.ax.tick_params(labelsize=12)
        cbar.set_label(r'prob. density ', size=12)



    del X,Y,xcenters,ycenters,xedges,yedges,x0,y0

#plt.subplots_adjust(wspace=0.3,hspace=0.3)
#fig.savefig('fig_conv_1_2.pdf')
#plt.savefig("fig_conv_1_2.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)

    
########################################################################################
#fig = plt.figure()
gg=np.zeros((tot,100,100),float)
for i in range(1,tot+1):
    res2="del{}".format(i)
    coord=files(res2)
    x0=coord[:,0]
    yyy0=coord[:,5]
    xxx0=-x0

    fold=1
    x0=np.split(xxx0,fold)
    y0=np.split(yyy0,fold)

    ax = fig.add_subplot(3,2,i+4)
    for axis in ['top','bottom','left','right']:
       ax.spines[axis].set_linewidth(2)

    gg=np.zeros((100,100),float)
    for j in range(fold):
        ggg,xedges,yedges=np.histogram2d(x0[j], y0[j], bins=(100,100),range=[[-1.5,1.5], [0.0,0.8]], normed=True)
        ggg=ggg.T
        gg=gg+ggg/fold

    legend=sec[i-1]

    xcenters = (xedges[:-1] + xedges[1:]) / 2
    ycenters = (yedges[:-1] + yedges[1:]) / 2
    X, Y = np.meshgrid(xcenters, ycenters)

    legend=sec[i-1]


    plt.xticks(np.arange(-1.5,1.6,0.5),size=16)
    plt.yticks(np.arange(0,0.5,0.2),size=16)
    plt.xlabel(r'$\delta^c_{1,2}$ (Å)',size=16)
    if i==1:
       plt.ylabel(r'$r_G^{\bot}$ (Å)',size=16)
    plt.xlim(-0.8,0.8)
    plt.ylim(0.00,0.401)
    ax.tick_params(axis='x', labelsize= 16,colors='black',width=2,length=8)
    ax.tick_params(axis='y', labelsize= 16,colors='black',width=2,length=8)
    plt.axvline(x=0.0, color = 'k',linewidth=2, linestyle = '--')

    plt.contourf(X, Y, gg, [0.01,0.1,1,10,100],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
    CS=ax.contour(X, Y, ggg, [0.01,0.1,1,10,100],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())

    cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
    if i ==2:
       cbar.ax.tick_params(labelsize=12)
       cbar.set_label(r'prob. density ', size=12)


    del X,Y,xcenters,ycenters,xedges,yedges,x0,y0
    

plt.subplots_adjust(wspace=0.4,hspace=0.5)
fig.savefig('fig_conv_1_3.pdf')
plt.savefig("fig_conv_1_3.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)

########################################################################################

