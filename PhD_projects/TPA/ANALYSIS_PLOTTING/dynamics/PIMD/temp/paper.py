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
sec=str(sys.argv[3]).split(',')
e=int(sys.argv[4])
#############1.histogram########################################## 

fig = plt.figure()


###
f=open('del1','r')
a=f.readlines()
f.close

coord1=[]
coord2=[]
cord=[]
start=0
t=0
for j in range(e+start*40,len(a),40):
   x=a[j].split()


   coord1.append(x)
   cord.append(t/2000.0)
   t=t+1

coord1=np.array(coord1,float)
cord=np.array(cord,float)

del a
###
coord1p1=[]
coord1p2=[]
coord2p1=[]
coord2p2=[]

f=open('del8','r')
a=f.readlines()
f.close

dog1=[]
for j in range(e+start*40,len(a),40):
   x=a[j].split()


   dog1.append(x)

dog1=np.array(dog1,float)

del a
#############

ax1 = fig.add_subplot(2,1,1)
for axis in ['top','bottom','left','right']:
     ax1.spines[axis].set_linewidth(1.5)

Y1=coord1[:,1]-coord1[:,2]
YY1=moving_average(Y1, w)
ax1.plot(cord[w-1:],YY1,'-b',lw=1.5,label='$\delta^c_{1,2} $')
ax1.plot(cord[0],YY1[0],'-r',lw=1.5,label='r$_G$') #dummy
plt.ylabel('$\delta^c_{1,2} $ (Å)',size=16)
ax1.yaxis.label.set_color('blue')  
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax1.set_yticks(np.arange(-1.5,1.5,0.5))
ax1.set_xticks(np.arange(0,28,4))
ax1.set_xlabel(r'Time (ps)',size=16)
ax1.set_ylim(-0.8,0.8)
ax1.set_xlim(0,20)
ax1.tick_params(axis='x', labelsize= 16,colors='black',length=8,width=1.5)
ax1.tick_params(axis='y', labelsize= 16,colors='blue',length=8,width=1.5)
ax1.legend(loc=1,prop={'size': 10})


ax2 = ax1.twinx()
Y2=dog1[:,3]
YY2=moving_average(Y2, w)
ax2.plot(cord[w-1:],YY2,'-r',lw=1.5,label='r$_G$')

fig.tight_layout()
plt.ylabel(r'r$_G$ (Å)',size=16)
ax2.yaxis.label.set_color('red')
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

ax2.tick_params(axis='y', labelsize= 16,colors='black',length=8,width=1.5)
ax2.tick_params(axis='x', labelsize= 16,colors='black',length=8,width=1.5)
ax2.set_xticks(np.arange(0,28,4))
ax2.set_yticks(np.arange(0.16,0.28,0.02))
ax2.set_ylim(0.181,0.259)
ax2.set_xlim(0,20)

ax2.tick_params(axis='y', labelsize= 16,colors='red')
#ax2.legend(loc=7,prop={'size': 10},ncol=2)



###############
###
f=open('ddel1','r')
a=f.readlines()
f.close

coord1=[]
coord2=[]
cord=[]
start=0
t=0
for j in range(e+start*40,len(a),40):
   x=a[j].split()


   coord1.append(x)
   cord.append(t/2000.0)
   t=t+1

coord1=np.array(coord1,float)
cord=np.array(cord,float)

del a
###
coord1p1=[]
coord1p2=[]
coord2p1=[]
coord2p2=[]

f=open('ddel8','r')
a=f.readlines()
f.close

dog1=[]
dog2=[]
for j in range(e+start*40,len(a),40):
   x=a[j].split()


   dog1.append(x)

dog1=np.array(dog1,float)

del a
#############

ax1 = fig.add_subplot(2,1,2)
for axis in ['top','bottom','left','right']:
     ax1.spines[axis].set_linewidth(1.5)



Y1=coord1[:,1]-coord1[:,2]
YY1=moving_average(Y1, w)
ax1.plot(cord[w-1:],YY1,'-b',lw=1.5,label='$\delta^c_{1,2}$')
plt.ylabel('$\delta^c_{1,2}$ (Å)',size=16)
ax1.yaxis.label.set_color('blue')  
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax1.set_yticks(np.arange(-1.5,1.5,0.5))
ax1.set_xticks(np.arange(0,28,4))
ax1.set_xlabel(r'Time (ps)',size=16)
ax1.set_ylim(-0.8,0.8)
ax1.set_xlim(0,20)
ax1.tick_params(axis='y', labelsize= 16,colors='blue',length=8,width=1.5)
ax1.tick_params(axis='x', labelsize= 16,colors='black',length=8,width=1.5)
#ax1.legend(loc=1,prop={'size': 10},ncol=2)


ax2 = ax1.twinx()
Y2=dog1[:,3]
YY2=moving_average(Y2, w)
ax2.plot(cord[w-1:],YY2,'-r',lw=1.5,label='r$_G$')

fig.tight_layout()
plt.ylabel(r'r$_G$ (Å)',size=16)
ax2.yaxis.label.set_color('red')
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

ax2.tick_params(axis='x', labelsize= 16,colors='red',length=8,width=1.5)
ax2.tick_params(axis='y', labelsize= 16,colors='red',length=8,width=1.5)
ax2.set_xticks(np.arange(0,28,4))
ax2.set_yticks(np.arange(0.12,0.26,0.02))
ax2.set_ylim(0.15,0.21)
ax2.set_xlim(0,20)




###############



################################################################################
plt.subplots_adjust(wspace=0.3,hspace=0.6)
plt.savefig("pimd_70_300K.jpg", dpi=500, bbox_inches = 'tight',    pad_inches = 0.1)
fig.savefig('pimd_70_300K.pdf')
#plt.show()









