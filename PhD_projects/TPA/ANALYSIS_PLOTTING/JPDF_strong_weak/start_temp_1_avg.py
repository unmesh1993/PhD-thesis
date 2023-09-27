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
from mpl_toolkits.axes_grid1 import make_axes_locatable

import os

os.system('rm data_2d.dat')
os.system('rm data_1d.dat')
###################################################################################
tot=np.int(sys.argv[1])
fold=np.int(sys.argv[2])
beads=np.array(str(sys.argv[3]).split(','),int)
sec=str(sys.argv[4]).split(',')
temp=np.array(str(sys.argv[5]).split(','),float)
dim=np.int(sys.argv[6])
###################################################################################
bin1=bin2=100
const=0
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

def files2(x,nbonds):
        frames=int(len(x)/nbonds)
        d1=[]
        d2=[]
        for i in range(frames):
            for j in range(int(nbonds/2)):
                t=j+(i)*nbonds
                d1.append(x[t])
                del t
                t=j+int(nbonds/2)+(i)*nbonds
                d2.append(x[t])
                del t
        d1=np.array(d1)
        d2=np.array(d2)
        return (d1,d2)

def cut(xx0,fol,bead,count):
        dd=np.split(xx0,bead)
        s=[]
        for i in range (len(dd[0])):
            for j in range (bead):
               s.append(dd[j][i])
        s=np.array(s,float)
        del dd
        return (s)


##################################################################
#############1.histogram########################################## 
new_colour = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf']
sec2 = ['(a)','(b)','(c)','(d)','(e)','(f)']

fig = plt.figure()

for i in range(1,tot+1):
    res2="del{}".format(i)
    coord=files(res2)
    x0=coord[:,1]-coord[:,2]

    res2="shell{}".format(i)
    coord=files(res2)
    y0=coord[:,2]

    res2="hell{}".format(i)
    coord=files(res2)
    z0=coord[:,2]

    ax = fig.add_subplot(2,2,i)
    gg1,xedges,yedges=np.histogram2d(x0, y0, bins=(bin1,bin2),range=[[-2.0,2.0], [1.0,4.0]], normed=True)
    xcenters = (xedges[:-1] + xedges[1:]) / 2
    ycenters = (yedges[:-1] + yedges[1:]) / 2
    X, Y = np.meshgrid(xcenters, ycenters)
    dx=(xedges[1]-xedges[0])
    dy=(yedges[1]-yedges[0])

    gg1=gg1.T
    gg1 [gg1 == 0] = 10**(-100)
    gg1=-1*np.log(gg1*dx*dy)   #KbT
    gg1[gg1 > 100]=np.inf
    v=np.amin(gg1)
    ggg1=gg1-v


    gg2,xedges,yedges=np.histogram2d(x0, z0, bins=(bin1,bin2),range=[[-2.0,2.0], [1.0,4.0]], normed=True)
    xcenters = (xedges[:-1] + xedges[1:]) / 2
    ycenters = (yedges[:-1] + yedges[1:]) / 2
    X, Y = np.meshgrid(xcenters, ycenters)
    dx=(xedges[1]-xedges[0])
    dy=(yedges[1]-yedges[0])

    gg2=gg2.T
    gg2 [gg2 == 0] = 10**(-100)
    gg2=-1*np.log(gg2*dx*dy)   #KbT
    gg2[gg2 > 100]=np.inf
    v=np.amin(gg2)
    ggg2=gg2-v

#######################################################################################################################
    plt.xticks(np.arange(-1.5,1.6,0.5),size=10,rotation=45)
    plt.yticks(np.arange(1,4,0.2),size=10)
    plt.xlabel(r'$\delta_{1,2}$ (Å)',size=12)
    plt.ylabel(r'$d_{H\cdots O}$ (Å)',size=12)
    plt.xlim(-1.4,1.4)
    plt.ylim(2.0,3.0)
    plt.axhline(y=0.0, color = 'k',linewidth=1, linestyle = '--')
    plt.axvline(x=0.0, color = 'k',linewidth=1, linestyle = '--')


#    plt.contourf(X, Y, ggg2, [0.0,1.0,2.0,3.0,4.0,5.0],cmap=plt.cm.get_cmap('Reds_r'),alpha=0.2)
    CS=ax.contour(X, Y, ggg2, [0.0,1.0,2.0,3.0,4.0,5.0],cmap=plt.cm.get_cmap('Reds_r'),alpha=0.8)
#    plt.contourf(X, Y, ggg1, [0.0,1.0,2.0,3.0,4.0,5.0],cmap=plt.cm.get_cmap('Greens_r'),alpha=0.5)
    CS=ax.contour(X, Y, ggg1, [0.0,1.0,2.0,3.0,4.0,5.0],cmap=plt.cm.get_cmap('Greens_r'),alpha=0.8)

#    cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
#    cbar.ax.tick_params(labelsize=10)
#    if  i == 2:
#         cbar.set_label(r'-log(probability)', size=10)




    del X,Y,xcenters,ycenters,xedges,yedges,x0,y0

####################################################################################################################################
for i in range(1,tot+1):
    res2="ddel{}".format(i)
    coord=files(res2)
    x0=coord[:,1]-coord[:,2]

    res2="dshell{}".format(i)
    coord=files(res2)
    y0=coord[:,2]

    res2="dhell{}".format(i)
    coord=files(res2)
    z0=coord[:,2]

    ax = fig.add_subplot(2,2,i+2)
    gg1,xedges,yedges=np.histogram2d(x0, y0, bins=(bin1,bin2),range=[[-2.0,2.0], [1.0,4.0]], normed=True)
    xcenters = (xedges[:-1] + xedges[1:]) / 2
    ycenters = (yedges[:-1] + yedges[1:]) / 2
    X, Y = np.meshgrid(xcenters, ycenters)
    dx=(xedges[1]-xedges[0])
    dy=(yedges[1]-yedges[0])

    gg1=gg1.T
    gg1 [gg1 == 0] = 10**(-100)
    gg1=-1*np.log(gg1*dx*dy)   #KbT
    gg1[gg1 > 100]=np.inf
    v=np.amin(gg1)
    ggg1=gg1-v


    gg2,xedges,yedges=np.histogram2d(x0, z0, bins=(bin1,bin2),range=[[-2.0,2.0], [1.0,4.0]], normed=True)
    xcenters = (xedges[:-1] + xedges[1:]) / 2
    ycenters = (yedges[:-1] + yedges[1:]) / 2
    X, Y = np.meshgrid(xcenters, ycenters)
    dx=(xedges[1]-xedges[0])
    dy=(yedges[1]-yedges[0])

    gg2=gg2.T
    gg2 [gg2 == 0] = 10**(-100)
    gg2=-1*np.log(gg2*dx*dy)   #KbT
    gg2[gg2 > 100]=np.inf
    v=np.amin(gg2)
    ggg2=gg2-v

#######################################################################################################################
    plt.xticks(np.arange(-1.5,1.6,0.5),size=10,rotation=45)
    plt.yticks(np.arange(1,4,0.2),size=10)
    plt.xlabel(r'$\delta_{1,2}$ (Å)',size=12)
    plt.ylabel(r'$d_{H\cdots O}$ (Å)',size=12)
    plt.xlim(-1.4,1.4)
    plt.ylim(2.0,3.0)
    plt.axhline(y=0.0, color = 'k',linewidth=1, linestyle = '--')
    plt.axvline(x=0.0, color = 'k',linewidth=1, linestyle = '--')


#    plt.contourf(X, Y, ggg2, [0.0,1.0,2.0,3.0,4.0,5.0],cmap=plt.cm.get_cmap('Reds_r'),alpha=0.2)
    CS=ax.contour(X, Y, ggg2, [0.0,1.0,2.0,3.0,4.0,5.0],cmap=plt.cm.get_cmap('Reds_r'),alpha=0.8)
#    plt.contourf(X, Y, ggg1, [0.0,1.0,2.0,3.0,4.0,5.0],cmap=plt.cm.get_cmap('Greens_r'),alpha=0.2)
    CS=ax.contour(X, Y, ggg1, [0.0,1.0,2.0,3.0,4.0,5.0],cmap=plt.cm.get_cmap('Greens_r'),alpha=0.8)

#    cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
#    cbar.ax.tick_params(labelsize=10)
#    if  i == 2:
#         cbar.set_label(r'-log(probability)', size=10)




    del X,Y,xcenters,ycenters,xedges,yedges,x0,y0

####################################################################################################################################




####################################################################################################################################

plt.subplots_adjust(wspace=0.5,hspace=0.7)
fig.savefig('fig_conv_1_1.pdf')
plt.savefig("fig_conv_1_1.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
#plt.show()

