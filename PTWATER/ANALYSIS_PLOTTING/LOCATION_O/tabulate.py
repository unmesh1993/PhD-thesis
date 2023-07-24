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

    
f=open('del1','r')
a=f.readlines()
f.close

f=open('del2','r')
aa=f.readlines()
f.close

f=open('ddel1','r')
b=f.readlines()
f.close

f=open('ddel2','r')
bb=f.readlines()
f.close


z1=[]
z2=[]
z3=[]
z4=[]
for i in range(len(a)):
    t=a[i].split()
    z1.append(t)
    t=aa[i].split()
    z2.append(t)
    t=b[i].split()
    z3.append(t)
    t=bb[i].split()
    z4.append(t)

z1=np.array(z1,float)
z2=np.array(z2,float)
z3=np.array(z3,float)
z4=np.array(z4,float)

###############################################################################################################
fig=plt.figure()
ax1 = fig.add_subplot(211)

plt.plot(z1[:,0],z1[:,1], '-ob', markersize=0, lw=1  ,mfc='white',label='clean: BOMD')
plt.plot(z3[:,0],z3[:,1], '-or', markersize=0, lw=1  ,mfc='white',label='clean: BOMD+PIGLET')
plt.plot(z2[:,0],z2[:,1], '-o',color='darkorange', markersize=0, lw=1  ,mfc='white',label='0.5 ML H: BOMD')
plt.plot(z4[:,0],z4[:,1], '-og', markersize=0, lw=1  ,mfc='white',label='0.5 ML H: BOMD+PIGLET')

plt.legend(prop={'size': 6},loc=0)
plt.xticks(np.arange(0,100,1.0),size=10)
plt.yticks(size=10)
plt.xlim(0,7)
#plt.ylim(0,4.2)
plt.xlabel(r'Prob. Dens.',size=10)
plt.ylabel('Density (g/cc)',size=10)


#ax1 = fig.add_subplot(212)
#
#plt.plot(z2[:,0],z2[:,9], '-ob', markersize=2, lw=2  ,mfc='white',label='BOMD')
#plt.plot(z4[:,0],z4[:,9], '-or', markersize=2, lw=2  ,mfc='white',label='BOMD+PIGLET')
#
#plt.axhline(y=1.0, color = 'k',linewidth=1, linestyle = '--')
#plt.legend(prop={'size': 6},loc=0)
#plt.xticks(np.arange(0,100,1.0),size=10)
#plt.yticks(size=10)
#plt.xlim(0,7)
#plt.ylim(0,4.2)
#plt.xlabel(r'Distance from Pt surface (Å)',size=10)
#plt.ylabel('Density (g/cc)',size=10)




plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.savefig("photo.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)

###############################################################################################################
