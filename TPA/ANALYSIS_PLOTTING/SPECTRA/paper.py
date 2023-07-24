import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D # This import has side effects required for the kwarg projection='3d' in the call to fig.add_subplot
import matplotlib.pyplot as plt
import random
import sys
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.colors import LogNorm


import os
x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
x6=[]
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
y6=[]

res='del1'
f=open(res,'r')
a=f.readlines()
f.close
cord=[]
for j in range(len(a)):
   xx=a[j].split()
   x1.append(xx[0])
   y1.append(xx[1])

res='del2'
f=open(res,'r')
a=f.readlines()
f.close
cord=[]
for j in range(len(a)):
   xx=a[j].split()
   x2.append(xx[0])
   y2.append(xx[1])

res='del3'
f=open(res,'r')
a=f.readlines()
f.close
cord=[]
for j in range(len(a)):
   xx=a[j].split()
   x3.append(xx[0])
   y3.append(xx[1])

res='del4'
f=open(res,'r')
a=f.readlines()
f.close
cord=[]
for j in range(len(a)):
   xx=a[j].split()
   x4.append(xx[0])
   y4.append(xx[1])

res='del5'
f=open(res,'r')
a=f.readlines()
f.close
cord=[]
for j in range(len(a)):
   xx=a[j].split()
   x5.append(xx[0])
   y5.append(xx[1])

res='del6'
f=open(res,'r')
a=f.readlines()
f.close
cord=[]
for j in range(len(a)):
   xx=a[j].split()
   x6.append(xx[0])
   y6.append(xx[1])


x1=np.array(x1,float)
x2=np.array(x2,float)
x3=np.array(x3,float)
x4=np.array(x4,float)
x5=np.array(x5,float)
x6=np.array(x6,float)
y1=np.array(y1,float)
y2=np.array(y2,float)
y3=np.array(y3,float)
y4=np.array(y4,float)
y5=np.array(y5,float)
y6=np.array(y6,float)


fig=plt.figure()
ax = fig.add_subplot(211)
plt.plot(x5,y5*20,'-ok', markersize=4, lw=2,mfc='white',label='70K-monomer (x20)')
plt.plot(x1,y1,'-Xb', markersize=4, lw=2, mfc='white',label='70 K')
plt.plot(x2,y2,'-sr', markersize=4, lw=2,mfc='white',label='300 K')
plt.xlabel('$\omega$ (cm$^{-1}$)',size=12)
plt.ylabel('IR abs. (arb. units)',size=10)
plt.xticks(np.arange(200,4200,400),size=10)
plt.xlim(2000,3800)
#plt.ylim(0,4)
plt.ylim(0,np.amax(y2[x2 > 1800])+np.amax(y2[(x2 > 1800)])*0.4)
ax.set_yticks([])
plt.legend(prop={'size': 8},loc=2,ncol=3)

ax = fig.add_subplot(212)
plt.plot(x5,y5*20,'-ok', markersize=4, lw=2,mfc='white',label='70K-monomer (x20)')
plt.plot(x3,y3,'-Xb', markersize=4, lw=2,mfc='white',label='70 K')
plt.plot(x4,y4,'-sr', markersize=4, lw=2,mfc='white',label='300 K')
plt.xlabel('$\omega$ (cm$^{-1}$)',size=12)
plt.ylabel('IR abs. (arb. units)',size=10)
plt.xticks(np.arange(200,4200,400),size=10)
plt.xlim(2000,3800)
plt.ylim(0,np.amax(y4[x4 > 1800])+np.amax(y4[(x4 > 1800)])*0.4)
ax.set_yticks([])
plt.legend(prop={'size': 8},loc=2,ncol=3)

plt.subplots_adjust(wspace=0.00,hspace=0.5)
fig.savefig('photo.pdf')
plt.savefig("photo.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)

