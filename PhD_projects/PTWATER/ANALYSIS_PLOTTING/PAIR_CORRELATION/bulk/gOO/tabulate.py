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

coord1x=[]
coord1y1=[]
coord1y2=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[0]))
    coord1y1.append(x[1])
del x,a
d1x=np.array(coord1x,float)
d1y1=np.array(coord1y1,float)

coord2x=[]
coord2y1=[]
for i in range(len(aa)):
    x=aa[i].split()
    coord2x.append(float(x[0]))
    coord2y1.append(x[1])
del x,aa
d2x=np.array(coord2x,float)
d2y1=np.array(coord2y1,float)

##########################################
f=open('ddel1','r')
a=f.readlines()
f.close

f=open('ddel2','r')
aa=f.readlines()
f.close

coord1x=[]
coord1y1=[]
coord1y2=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[0]))
    coord1y1.append(x[1])
del x,a
dd1x=np.array(coord1x,float)
dd1y1=np.array(coord1y1,float)

coord2x=[]
coord2y1=[]
for i in range(len(aa)):
    x=aa[i].split()
    coord2x.append(float(x[0]))
    coord2y1.append(x[1])
del x,aa
dd2x=np.array(coord2x,float)
dd2y1=np.array(coord2y1,float)

#######################



###############################################################################################################
fig=plt.figure()
ax1 = fig.add_subplot(211)

plt.plot(d1x,d1y1, '-ob', markersize=0, lw=1  ,mfc='white',label='clean: BOMD')
plt.plot(dd1x,dd1y1, '-or', markersize=0, lw=1  ,mfc='white',label='clean: BOMD+PIGLET')
plt.plot(d2x,d2y1, '-o',color='darkorange', markersize=0, lw=1  ,mfc='white',label='0.5 ML H: BOMD')
plt.plot(dd2x,dd2y1, '-og', markersize=0, lw=1  ,mfc='white',label='0.5 ML H: BOMD+PIGLET')

plt.axhline(y=1.0, color = 'k',linewidth=1, linestyle = '--')
plt.legend(prop={'size': 6},loc=0)
plt.xticks(np.arange(0,100,1.0),size=10)
plt.yticks(size=10)
plt.xlim(1,6)
plt.ylim(0,5)
plt.xlabel(r'r (Å)',size=10)
plt.ylabel('g$_{O)}$ (r)',size=10)


#ax1 = fig.add_subplot(212)
#
#plt.plot(z2[:,0],z2[:,1], '-ob', markersize=2, lw=2  ,mfc='white',label='BOMD')
#plt.plot(z4[:,0],z4[:,1], '-or', markersize=2, lw=2  ,mfc='white',label='BOMD+PIGLET')
#
#plt.axhline(y=1.0, color = 'k',linewidth=1, linestyle = '--')
#plt.legend(prop={'size': 6},loc=0)
#plt.xticks(np.arange(0,100,1.0),size=10)
#plt.yticks(size=10)
#plt.xlim(0,6)
#plt.ylim(0,3)
#plt.xlabel(r'r (Å)',size=10)
#plt.ylabel('g$_{OH}$ (r)',size=10)




plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.savefig("photo.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)

###############################################################################################################
