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

def minima2(X,Y,ggg,sss,count):
    vv1x=[]
    vv1y=[]
    vv1z=[]
    for iii in range(len(ggg)):
      for jjj in range(len(ggg)):

             vv1z.append(ggg[iii][jjj])
             vv1x.append(X[iii][jjj])
             vv1y.append(Y[iii][jjj])

    vv1z=np.array(vv1z,float)
    vv1x=np.array(vv1x,float)
    vv1y=np.array(vv1y,float)
       
    ax = fig.add_subplot(2,2,count)
    plt.plot([vv1x[np.argmin(vv1z)]],[vv1y[np.argmin(vv1z)]],'--o', markersize=2, lw=1  ,color='black',mfc='white') 

def minima(X,Y,ggg,sss,count):
    vv1z=[]
    vv2z=[]
    vv3z=[]
    vv4z=[]
    vv1x=[]
    vv2x=[]
    vv3x=[]
    vv4x=[]
    vv1y=[]
    vv2y=[]
    vv3y=[]
    vv4y=[]
    vv1s=[]
    vv2s=[]
    vv3s=[]
    vv4s=[]
    for iii in range(len(ggg)):
      for jjj in range(len(ggg)):

        if X[iii][jjj] >= 0.0 and Y[iii][jjj] >= 0.0:
             vv1z.append(ggg[iii][jjj])
             vv1x.append(X[iii][jjj])
             vv1y.append(Y[iii][jjj])
             vv1s.append(sss[iii][jjj])
        elif X[iii][jjj] < 0.0 and Y[iii][jjj] >= 0.0:
             vv2z.append(ggg[iii][jjj])
             vv2x.append(X[iii][jjj])
             vv2y.append(Y[iii][jjj])
             vv2s.append(sss[iii][jjj])
        if X[iii][jjj] < 0.0 and Y[iii][jjj] < 0.0:
             vv3z.append(ggg[iii][jjj])
             vv3x.append(X[iii][jjj])
             vv3y.append(Y[iii][jjj])
             vv3s.append(sss[iii][jjj])
        if X[iii][jjj] >= 0.0 and Y[iii][jjj] < 0.0:
             vv4z.append(ggg[iii][jjj])
             vv4x.append(X[iii][jjj])
             vv4y.append(Y[iii][jjj])
             vv4s.append(sss[iii][jjj])

    vv1z=np.array(vv1z,float)
    vv2z=np.array(vv2z,float)
    vv3z=np.array(vv3z,float)
    vv4z=np.array(vv4z,float)
    vv1x=np.array(vv1x,float)
    vv2x=np.array(vv2x,float)
    vv3x=np.array(vv3x,float)
    vv4x=np.array(vv4x,float)
    vv1y=np.array(vv1y,float)
    vv2y=np.array(vv2y,float)
    vv3y=np.array(vv3y,float)
    vv4y=np.array(vv4y,float)
    vv1s=np.array(vv1s,float)
    vv2s=np.array(vv2s,float)
    vv3s=np.array(vv3s,float)
    vv4s=np.array(vv4s,float)

    print(count-2)
    print (vv1x[np.argmin(vv1z)],vv1y[np.argmin(vv1z)],np.amin(vv1z)*(temp[i-1]/298)*0.02568*1000,vv1s[np.argmin(vv1z)]*(temp[i-1]/298)*0.02568*1000)
    print (vv3x[np.argmin(vv3z)],vv3y[np.argmin(vv3z)],np.amin(vv3z)*(temp[i-1]/298)*0.02568*1000,vv3s[np.argmin(vv3z)]*(temp[i-1]/298)*0.02568*1000)

    ax = fig.add_subplot(2,2,count)
    plt.plot([vv1x[np.argmin(vv1z)],vv3x[np.argmin(vv3z)]],[vv1y[np.argmin(vv1z)],vv3y[np.argmin(vv3z)]],'--o', markersize=2, lw=1  ,color='black',mfc='white')


#    x, y = vv1x[np.argmin(vv1z)], vv1y[np.argmin(vv1z)]
#    text = ' {:.2f}'.format(np.amin(vv1z)*(temp[i-1]/298)*0.02568*1000)
#    ax.annotate(text, xy=(x,y),size=4,weight='bold',color='black')

def summation(X,Y,ggg):
    vv1z=[]
    vv2z=[]
    vv3z=[]
    vv4z=[]
    for iii in range(len(ggg)):
      for jjj in range(len(ggg)):

        if X[iii][jjj] >= 0.0 and Y[iii][jjj] >= 0.0:
             vv1z.append(ggg[iii][jjj])
        elif X[iii][jjj] < 0.0 and Y[iii][jjj] >= 0.0:
             vv2z.append(ggg[iii][jjj])
        if X[iii][jjj] < 0.0 and Y[iii][jjj] < 0.0:
             vv3z.append(ggg[iii][jjj])
        if X[iii][jjj] >= 0.0 and Y[iii][jjj] < 0.0:
             vv4z.append(ggg[iii][jjj])

    vv1z=np.array(vv1z,float)
    vv2z=np.array(vv2z,float)
    vv3z=np.array(vv3z,float)
    vv4z=np.array(vv4z,float)

    print ('summation')
    print (np.sum(vv1z),np.sum(vv2z),np.sum(vv3z),np.sum(vv4z))


##################################################################
#############1.histogram########################################## 
new_colour = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf']
sec2 = ['(a)','(b)','(c)','(d)','(e)','(f)']

fig = plt.figure()

for i in range(1,tot+1):
    res2="del{}".format(i)
    coord=files(res2)

    x=coord[:,1]-coord[:,2]
    xx0,yy0=files2(x,dim)

    fold=1
    x0=np.split(xx0,fold)
    y0=np.split(yy0,fold)

    
    ax = fig.add_subplot(2,2,i)
    xedges,yedges=np.histogram2d(x0[0], y0[0], bins=(bin1,bin2),range=[[-2.0,2.0], [-2.0,2.0]], normed=True)[1:]
    xcenters = (xedges[:-1] + xedges[1:]) / 2
    ycenters = (yedges[:-1] + yedges[1:]) / 2
    X, Y = np.meshgrid(xcenters, ycenters)
    dx=(xedges[1]-xedges[0])
    dy=(yedges[1]-yedges[0])

    kkk=np.zeros((fold,bin1,bin2),float)
    for j in range(fold):
        gg=np.histogram2d(x0[j], y0[j], bins=(bin1,bin2),range=[[-2.0,2.0], [-2.0,2.0]], normed=True)[0]
        gg=gg.T
        gg [gg == 0] = 10**(-100)
    #    gg=-1*(temp[i-1]/298)*0.02568*1000*np.log(gg*dx*dy)   #meV
        gg=-1*np.log(gg*dx*dy)   #KbT
        gg[gg > 100]=np.inf
        kkk[j]=gg

    ggg=np.mean(kkk,axis=0)
    sss=np.std(kkk,axis=0)

    summation(X,Y,np.exp(-1*ggg))

    v=np.amin(ggg)
    ggg=ggg-v

#######################################################################################################################
    e1=[]
    e2=[]
    for kk in range(bin1):
        e1.append(X[kk][kk])
        e2.append(ggg[kk][kk])

    e1=np.array(e1)
    e2=np.array(e2)

    for ij in range(bin1):
            f=open('data_1d.dat','a')
            f.write("%.3f \t  %.3f \n" %(e2[ij],e1[ij]))
            f.close()
    f=open('data_1d.dat','a')
    f.write("%.s \n" %('&'))
    f.close()


    for ij in range(bin1):
        for ik in range(bin2):
            f=open('data_2d.dat','a')
            f.write("%.3f \t  %.3f \t %.3f \t %.3f \n" %(ggg[ij][ik],sss[ij][ik],X[ij][ik],Y[ij][ik]))
            f.close()
    f=open('data_2d.dat','a')
    f.write("%.s \n" %('&'))
    f.close()


    if i > 1:
       minima(X,Y,ggg,sss,i)
    else:
       minima2(X,Y,ggg,sss,i)

    plt.xticks(np.arange(-1.5,1.6,0.5),size=10,rotation=45)
    plt.yticks(np.arange(-1.5,1.6,0.5),size=10)
    plt.xlabel(r'$\delta_1$ (Å)',size=12)
    if i > 0:
       plt.ylabel(r'$\delta_2$ (Å)',size=12)
    plt.xlim(-1.4,1.4)
    plt.ylim(-1.4,1.4)
    plt.axhline(y=0.0, color = 'k',linewidth=1, linestyle = '--')
    plt.axvline(x=0.0, color = 'k',linewidth=1, linestyle = '--')

    plt.contourf(X, Y, ggg, [0,1,2,3,4,5,6,7,8,9,10],cmap=plt.cm.get_cmap('jet'))
    CS=ax.contour(X, Y, ggg, [0,1,2,3,4,5,6,7,8,9,10],cmap=plt.cm.get_cmap('jet'))

    cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
    cbar.ax.tick_params(labelsize=10)
    if  i == 2:
         cbar.set_label(r'Free Energy ($k_BT$) ', size=10)




    del X,Y,xcenters,ycenters,xedges,yedges,x,x0,y0

####################################################################################################################################
for i in range(1,tot+1):

    res2="ddel{}".format(i)
    coord=files(res2)

    x=coord[:,1]-coord[:,2]
    xx0,yy0=files2(x,dim)

    fold=1
    xxx0=cut(xx0,fold,beads[i-1],i)
    yyy0=cut(yy0,fold,beads[i-1],i)

    x0=np.split(xxx0,fold)
    y0=np.split(yyy0,fold)


    ax = fig.add_subplot(2,2,i+2)
    xedges,yedges=np.histogram2d(x0[0], y0[0], bins=(bin1,bin2),range=[[-2.0,2.0], [-2.0,2.0]], normed=True)[1:]
    xcenters = (xedges[:-1] + xedges[1:]) / 2
    ycenters = (yedges[:-1] + yedges[1:]) / 2
    X, Y = np.meshgrid(xcenters, ycenters)
    dx=(xedges[1]-xedges[0])
    dy=(yedges[1]-yedges[0])

    kkk=np.zeros((fold,bin1,bin2),float)
    for j in range(fold):
        gg=np.histogram2d(x0[j], y0[j], bins=(bin1,bin2),range=[[-2.0,2.0], [-2.0,2.0]], normed=True)[0]
        gg=gg.T
        gg [gg == 0] = 10**(-100)
    #    gg=-1*(temp[i-1]/298)*0.02568*1000*np.log(gg*dx*dy)   #meV
        gg=-1*np.log(gg*dx*dy)   #KbT
        gg[gg > 100]=np.inf
        kkk[j]=gg

    ggg=np.mean(kkk,axis=0)
    sss=np.std(kkk,axis=0)
        
    summation(X,Y,np.exp(-1*ggg))

    v=np.amin(ggg)
    ggg=ggg-v

#######################################################################################################################
    e1=[]
    e2=[]
    for kk in range(bin1):
        e1.append(X[kk][kk])
        e2.append(ggg[kk][kk])

    e1=np.array(e1)
    e2=np.array(e2)

    for ij in range(bin1):
            f=open('data_1d.dat','a')
            f.write("%.3f \t  %.3f \n" %(e2[ij],e1[ij]))
            f.close()
    f=open('data_1d.dat','a')
    f.write("%.s \n" %('&'))
    f.close()


    for ij in range(bin1):
        for ik in range(bin2):
            f=open('data_2d.dat','a')
            f.write("%.3f \t  %.3f \t %.3f \t %.3f \n" %(ggg[ij][ik],sss[ij][ik],X[ij][ik],Y[ij][ik]))
            f.close()
    f=open('data_2d.dat','a')
    f.write("%.s \n" %('&'))
    f.close()

    minima(X,Y,ggg,sss,i+2)
    legend=sec[i-1] 

    plt.xticks(np.arange(-1.5,1.6,0.5),size=10,rotation=45)
    plt.yticks(np.arange(-1.5,1.6,0.5),size=10)
    plt.xlabel(r'$\delta_1$ (Å)',size=12)
    if i > 0:
       plt.ylabel(r'$\delta_2$ (Å)',size=12)
    plt.xlim(-1.4,1.4)
    plt.ylim(-1.4,1.4)
    plt.axhline(y=0.0, color = 'k',linewidth=1.0, linestyle = '--')
    plt.axvline(x=0.0, color = 'k',linewidth=1.0, linestyle = '--')

    plt.contourf(X, Y, ggg, [0,1,2,3,4,5,6,7,8,9,10],cmap=plt.cm.get_cmap('jet'))
    CS=ax.contour(X, Y, ggg, [0,1,2,3,4,5,6,7,8,9,10],cmap=plt.cm.get_cmap('jet'))
#    ax.clabel(CS, inline=True, fontsize=10)
    cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
    cbar.ax.tick_params(labelsize=10)
    if  i == 2:
         cbar.set_label(r'Free Energy ($k_BT$) ', size=10)




    del X,Y,xcenters,ycenters,xedges,yedges,x,x0,y0





####################################################################################################################################

plt.subplots_adjust(wspace=0.5,hspace=0.7)
fig.savefig('fig_conv_1_1.pdf')
plt.savefig("fig_conv_1_1.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
#plt.show()

