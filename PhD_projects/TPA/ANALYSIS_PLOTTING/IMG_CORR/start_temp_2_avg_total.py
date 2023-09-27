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
temp=np.array(str(sys.argv[5]).split(','),int)
dim=np.int(sys.argv[6])
###################################################################################


def files(res2):
        f=open(res2,'r')
        a=f.readlines()
        f.close
        
        coord=[]
        for i in range(0,len(a)):
            x=a[i].split()
            x=np.array(x,float)
            coord.append(x[1]-x[2])
        coord=np.array(coord,float)
        return (coord)



def files2_pi(resc,res2,nbonds,bead,kick):

        f=open(res2,'r')
        a=f.readlines()
        f.close
        
        f=open(resc,'r')
        aa=f.readlines()
        f.close


        frames=int(len(a)/nbonds)
        d1=[]
        d2=[]
        d3=[]
        for i in range(frames):
            for j in range(int(nbonds/2)):
                t1=j+(i)*nbonds
                t2=j+int(nbonds/2)+(i)*nbonds
                x=a[t1].split()[1]
                y=a[t1].split()[2]
                x1=float(x)-float(y)
                x=a[t2].split()[1]
                y=a[t2].split()[2]
                x2=float(x)-float(y)
                x3=(x1+x2)*0.5
                d1.append(x1)
                d2.append(x2)
                d3.append(x3)
        d1=np.array(d1)
        d2=np.array(d2)
        d3=np.array(d3)
        del a

        ggg,xedges=np.histogram(d1, bins=100,range=[-1.5, 1.5], density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        react1=xcenters[np.argmax(ggg)]

        ss=xcenters[xcenters > 0.2]
        gg=ggg[xcenters > 0.2]
        prod1=ss[np.argmax(gg)]


        ggg,xedges=np.histogram(d2, bins=100,range=[-1.5, 1.5], density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        react2=xcenters[np.argmax(ggg)]

        ss=xcenters[xcenters > 0.2]
        gg=ggg[xcenters > 0.2]
        prod2=ss[np.argmax(gg)]

        print (react1,react2,prod1,prod2)


        frames=int(len(aa)/nbonds)
        k1=[]
        k2=[]
        k3=[]

        for iii in range(bead):
            for i in range(frames):
                for j in range(int(nbonds/2)):
                    t1=j+(i)*nbonds
                    t2=j+int(nbonds/2)+(i)*nbonds
                    x=aa[t1].split()[1]
                    y=aa[t1].split()[2]
                    x1=float(x)-float(y)
                    x=aa[t2].split()[1]
                    y=aa[t2].split()[2]
                    x2=float(x)-float(y)
                    x3=(x1+x2)*0.5
                    k1.append(x1)
                    k2.append(x2)
                    k3.append(x3)

        k1=np.array(k1,float)
        k2=np.array(k2,float)
        k3=np.array(k3,float)
        del aa

        kkk1=[]
        kkk2=[]
        kkk3=[]

        pcc0=0.2
        for j in range(len(d1)):
            if k1[j] >= -1*pcc0 and k1[j] <= pcc0 and k2[j] >= -1*pcc0 and k2[j] <= pcc0:
                     value=(((d1[j]-d3[j])**2 + (d2[j]-d3[j])**2)*0.5)**0.5
                     kkk2.append(value)

        kkk2=np.array(kkk2,float)

        if kick ==1:
            pcc1=0.02
            pcc2=0.06
        elif kick ==2:
            pcc1=0.025
            pcc2=0.035


        for j in range(len(d1)):
            if k1[j] >= (react1 - pcc1) and k1[j] <= (react1 + pcc1) and k2[j] >= (react2 - pcc1) and k2[j] <= (react2 + pcc1) :
                     value=(((d1[j]-d3[j])**2 + (d2[j]-d3[j])**2)*0.5)**0.5
                     kkk1.append(value)
            elif k1[j] >= (prod1 - pcc2) and k1[j] <= (prod1 + pcc2) and k2[j] >= (prod2 - pcc2) and k2[j] <= (prod2 + pcc2):
                     value=(((d1[j]-d3[j])**2 + (d2[j]-d3[j])**2)*0.5)**0.5
                     kkk3.append(value)



        kkk1=np.array(kkk1,float)
        kkk3=np.array(kkk3,float)

        print (len(kkk1),len(kkk2),len(kkk3)) 

        ax = fig.add_subplot(2,2,1)
        if kick==1:

              ggg,xedges=np.histogram(kkk1, bins=20,range=[0,1], density=True)
              xcenters = (xedges[:-1] + xedges[1:]) / 2
              plt.plot(xcenters-xcenters[0],ggg, '-ob', markersize=1, lw=1  ,mfc='white',label=sec[kick-1]+':M1-M1')
              dx=(xedges[1]-xedges[0])

              ggg,xedges=np.histogram(kkk2, bins=20,range=[0,1], density=True)
              xcenters = (xedges[:-1] + xedges[1:]) / 2
              plt.plot(xcenters-xcenters[0],ggg, '-or', markersize=1, lw=1  ,mfc='white',label=sec[kick-1]+':S-S')
              dx=(xedges[1]-xedges[0])

              ggg,xedges=np.histogram(kkk3, bins=20,range=[0,1], density=True)
              xcenters = (xedges[:-1] + xedges[1:]) / 2
              plt.plot(xcenters-xcenters[0],ggg, '-og', markersize=1, lw=1  ,mfc='white',label=sec[kick-1]+':M2-M2')
              dx=(xedges[1]-xedges[0])

        elif kick==2:

              ggg,xedges=np.histogram(kkk1, bins=20,range=[0,1], density=True)
              xcenters = (xedges[:-1] + xedges[1:]) / 2
              plt.plot(xcenters-xcenters[0],ggg, '--xb', markersize=4, lw=1  ,mfc='white',label=sec[kick-1]+':M1-M1')
              dx=(xedges[1]-xedges[0])

              ggg,xedges=np.histogram(kkk2, bins=20,range=[0,1], density=True)
              xcenters = (xedges[:-1] + xedges[1:]) / 2
              plt.plot(xcenters-xcenters[0],ggg, '--xr', markersize=4, lw=1  ,mfc='white',label=sec[kick-1]+':S-S')
              dx=(xedges[1]-xedges[0])

              ggg,xedges=np.histogram(kkk3, bins=20,range=[0,1], density=True)
              xcenters = (xedges[:-1] + xedges[1:]) / 2
              plt.plot(xcenters-xcenters[0],ggg, '--xg', markersize=4, lw=1  ,mfc='white',label=sec[kick-1]+':M2-M2')
              dx=(xedges[1]-xedges[0])



        plt.ylabel(r'P($\Delta$)',size=10)
        plt.xlabel(r'$\Delta$ (Å)',size=10)
        ax.legend(prop={'size': 6},loc=0,ncol=2)
        plt.xticks(np.arange(-1.0,1.1,0.2),size=10)
        plt.yticks(size=10)
        plt.xlim(0.0,0.6)
        return ()

def files2_bo(res3,nbonds,bead,kick):

        f=open(res3,'r')
        a=f.readlines()
        f.close
        

        frames=int(len(a)/nbonds)
        d1=[]
        d2=[]
        d3=[]
        for i in range(frames):
            for j in range(int(nbonds/2)):
                t1=j+(i)*nbonds
                t2=j+int(nbonds/2)+(i)*nbonds
                x=a[t1].split()[1]
                y=a[t1].split()[2]
                x1=float(x)-float(y)
                x=a[t2].split()[1]
                y=a[t2].split()[2]
                x2=float(x)-float(y)
                x3=(x1+x2)*0.5
                d1.append(x1)
                d2.append(x2)
                d3.append(x3)
        d1=np.array(d1)
        d2=np.array(d2)
        d3=np.array(d3)


        del a        

        kkk1=[]
        kkk2=[]
        kkk3=[]

        for j in range(len(d3)):
            if d3[j] < -0.5:
                     value=(((d1[j]-d3[j])**2 + (d2[j]-d3[j])**2)*0.5)**0.5
                     kkk1.append(value)
            elif d3[j] >= -0.2 and d3[j] <= 0.2:
                     value=(((d1[j]-d3[j])**2 + (d2[j]-d3[j])**2)*0.5)**0.5
                     kkk2.append(value)
            elif d3[j] > 0.5:
                     value=(((d1[j]-d3[j])**2 + (d2[j]-d3[j])**2)*0.5)**0.5
                     kkk3.append(value)
            


        kkk1=np.array(kkk1,float)
        kkk2=np.array(kkk2,float)
        kkk3=np.array(kkk3,float)

        ax = fig.add_subplot(2,2,kick)


        ggg,xedges=np.histogram(kkk1, bins=20,range=[0,1], density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,ggg, '-o', markersize=1, lw=1  ,mfc='white',label=sec[kick-1]+':M1-M1')
        dx=(xedges[1]-xedges[0])

        ggg,xedges=np.histogram(kkk2, bins=20,range=[0,1], density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,ggg, '-o', markersize=1, lw=1  ,mfc='white',label=sec[kick-1]+':S-S')
        dx=(xedges[1]-xedges[0])

        ggg,xedges=np.histogram(kkk3, bins=20,range=[0,1], density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,ggg, '-o', markersize=1, lw=1  ,mfc='white',label=sec[kick-1]+':M2-M2')
        dx=(xedges[1]-xedges[0])


        plt.ylabel(r'P($\Delta$)',size=10)
        plt.xlabel(r'$\Delta$ (Å)',size=10)
        plt.legend(prop={'size': 5},loc=0)
        plt.xticks(np.arange(-1.0,1.1,0.2),size=10)
        plt.yticks(size=10)
        plt.xlim(-0.1,0.6)
        return ()

#############1.histogram########################################## 
new_colour = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf']

fig = plt.figure()

#for i in range(1,tot+1):
for i in [1,2]:
    res2="del{}".format(i)
    resc="ddel{}".format(i)
    res3="dell{}".format(i)

    files2_pi(resc,res2,dim,beads[i-1],i) 
#    files2_bo(res3,dim,beads[i-1],i) 

####################################################################################################################################




plt.subplots_adjust(wspace=0.3,hspace=0.5)
plt.savefig("fig_temp_1_3.jpg", dpi=500, bbox_inches = 'tight',    pad_inches = 0.1)
fig.savefig('fig_temp_1_3.pdf')
#plt.show()







