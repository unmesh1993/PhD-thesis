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




ax1 = fig.add_subplot(212)
plt.plot(z1[:,0],z1[:,2], '--ob', markersize=0, lw=1  ,mfc='white',label='BOMD: H$_2$O-H clean')
plt.plot(z3[:,0],z3[:,2], '--or', markersize=0, lw=1  ,mfc='white',label='BOMD+PIGLET: H$_2$O-H clean')

plt.plot(z2[:,0],z2[:,2], '--o',color='darkorange', markersize=0, lw=1  ,mfc='white',label='BOMD: H$_2$O-H')
plt.plot(z4[:,0],z4[:,2], '--og', markersize=0, lw=1  ,mfc='white',label='BOMD+PIGLET: H$_2$O-H')

plt.legend(prop={'size': 6},loc=0)
plt.xticks(np.arange(0,100,0.5),size=10)
plt.yticks(size=10)
#plt.xlim(0,4.5)
plt.ylim(0,0.14)
plt.xlabel(r'Distance from Pt surface (Å)',size=10)
plt.ylabel('prob. density',size=10)

ax2 = ax1.twinx()
ax2.plot(z2[:,0],z2[:,3], '-o',color='darkorange', markersize=0, lw=1  ,mfc='white',label='BOMD: H$_{ads}$')
ax2.plot(z4[:,0],z4[:,3], '-og', markersize=0, lw=1  ,mfc='white',label='BOMD+PIGLET: H$_{ads}$')
fig.tight_layout()

ax2.set_xlim(0,4.5)
ax2.set_ylim(0,2.0)
plt.ylabel('prob. density',size=10)
ax2.yaxis.label.set_color('black')
plt.legend(prop={'size': 6},loc=9)


plt.subplots_adjust(wspace=0.3,hspace=0.5)
plt.savefig("photo.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)

##################################################################################################################
res=str(sys.argv[1])

vec1=np.array([[13.8593,0.0,0.0],[0.0,14.4030,0.0],[0.0,0.0,65]],float)
ivec1=np.linalg.inv(vec1)

    
f=open(res,'r')
aa=f.readlines()
f.close

fig=plt.figure()

atoms=675
hyd=28

frames=int(len(aa)/(atoms+2))
wowx=[]
wowy=[]

lay1=np.zeros((56,2),float)
lay2=np.zeros((56,2),float)
lay3=np.zeros((56,2),float)

for i in range(frames):
       cord=[]
       count=0
       for j in range(660+2-30,660+2):
          t1=aa[j+(i)*(atoms+2)].split()
          cord.append(t1[3])
          
          t2=np.array(t1[1:3],float)
          lay1[count][0]=lay1[count][0]+t2[0]
          lay1[count][1]=lay1[count][1]+t2[1]

          t1=aa[j-30+(i)*(atoms+2)].split()
          t2=np.array(t1[1:3],float)
          lay2[count][0]=lay2[count][0]+t2[0]
          lay2[count][1]=lay2[count][1]+t2[1]

          t1=aa[j-30-30+(i)*(atoms+2)].split()
          t2=np.array(t1[1:3],float)
          lay3[count][0]=lay3[count][0]+t2[0]
          lay3[count][1]=lay3[count][1]+t2[1]

          count=count+1

       cord=np.array(cord,float)
       mean=np.mean(cord)

    

       coord=[]

       for j in range(atoms+2-hyd,atoms+2):
          t1=aa[j+(i)*(atoms+2)].split()
          t2=np.array(t1[1:],float)
          t2[2]=t2[2]-mean
          if t2[2] < 1.9:
              coord.append(t2)

       coord=np.array(coord,float)

       for t in range(0,len(coord)):

           xx=np.array(coord[t][0],float)
           yy=np.array(coord[t][1],float)

           wowx.append(xx) 
           wowy.append(yy) 


lay1=lay1/frames
lay2=lay2/frames
lay3=lay3/frames


############################
ax = fig.add_subplot(221)

plt.scatter (lay1[:,0],lay1[:,1],s=50,c='tan',alpha=1.0,label='top')
plt.scatter (lay2[:,0],lay2[:,1],s=20,c='grey',marker='x',alpha=1.0,label='hcp')
plt.scatter (lay3[:,0],lay3[:,1],s=20,c='magenta',marker='*',alpha=0.5,label='fcc')

x=np.array(wowy)
y=np.array(wowx)
gg,xedges,yedges=np.histogram2d(x, y, bins=(139,144),range=[[0.000,13.9 ], [0.000,14.41]],normed=True)
gg= gg.T ###transpose (please find reason)
#gg[gg == 0] = 0.0001

plt.ylabel('y [Å]',size=12)
plt.xlabel('x [Å]',size=12)
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)

plt.contourf(Y, X, gg, [0.00001,0.0001,0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('Blues'),norm = LogNorm())
cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
cbar.ax.tick_params(labelsize=8)

#plt.legend(prop={'size': 8},loc=9, bbox_to_anchor=(1.30,1.0))
plt.xticks(np.arange(0,13.9,2.7714),size=9,rotation=45)
plt.yticks(np.arange(0,14.41+2.40,2.40),size=9)
plt.xlim(0,13.9)
plt.ylim(0,14.41)

#############################################################################
dx=xcenters[1]-xcenters[0]
dy=ycenters[1]-ycenters[0]
summ=0
for i in range(144):
    for j in range(139):
        if gg[i,j] > 0:
             summ=summ+1

area1=summ*dx*dy/(13.8593*14.4030) 
##################################################################################################################
res=str(sys.argv[2])

    
f=open(res,'r')
aa=f.readlines()
f.close


atoms=675
hyd=15

frames=int(len(aa)/(atoms+2))
wowx=[]
wowy=[]

lay1=np.zeros((30,2),float)
lay2=np.zeros((30,2),float)
lay3=np.zeros((30,2),float)

for i in range(frames):
       cord=[]
       count=0
       for j in range(660+2-30,660+2):
          t1=aa[j+(i)*(atoms+2)].split()
          cord.append(t1[3])
          
          t2=np.array(t1[1:3],float)
          lay1[count][0]=lay1[count][0]+t2[0]
          lay1[count][1]=lay1[count][1]+t2[1]

          t1=aa[j-30+(i)*(atoms+2)].split()
          t2=np.array(t1[1:3],float)
          lay2[count][0]=lay2[count][0]+t2[0]
          lay2[count][1]=lay2[count][1]+t2[1]

          t1=aa[j-30-30+(i)*(atoms+2)].split()
          t2=np.array(t1[1:3],float)
          lay3[count][0]=lay3[count][0]+t2[0]
          lay3[count][1]=lay3[count][1]+t2[1]

          count=count+1

       cord=np.array(cord,float)
       mean=np.mean(cord)

    

       coord=[]

       for j in range(atoms+2-hyd,atoms+2):
          t1=aa[j+(i)*(atoms+2)].split()
          t2=np.array(t1[1:],float)
          t2[2]=t2[2]-mean
          if t2[2] < 2.2:
              coord.append(t2)

       coord=np.array(coord,float)

       for t in range(0,len(coord)):

           xx=np.array(coord[t][0],float)
           yy=np.array(coord[t][1],float)

           wowx.append(xx) 
           wowy.append(yy) 


lay1=lay1/frames
lay2=lay2/frames
lay3=lay3/frames


############################
ax = fig.add_subplot(222)

plt.scatter (lay1[:,0],lay1[:,1],s=50,c='tan',alpha=1.0,label='top')
plt.scatter (lay2[:,0],lay2[:,1],s=20,c='grey',marker='x',alpha=1.0,label='hcp')
plt.scatter (lay3[:,0],lay3[:,1],s=20,c='magenta',marker='*',alpha=0.5,label='fcc')

x=np.array(wowy)
y=np.array(wowx)
gg,xedges,yedges=np.histogram2d(x, y, bins=(139,144),range=[[0.000,13.9 ], [0.000,14.41]],normed=True)
gg= gg.T ###transpose (please find reason)
#gg[gg == 0] = 0.0001

#plt.ylabel('y [Å]',size=12)
plt.xlabel('x [Å]',size=12)
plt.yticks(size=10)
plt.xticks(size=10)
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)

plt.contourf(Y, X, gg, [0.00001,0.0001,0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('Blues'),norm = LogNorm())
cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
cbar.ax.tick_params(labelsize=8)
cbar.set_label(r'prob. density', size=8)

plt.legend(prop={'size': 8},loc=9, bbox_to_anchor=(1.80,1.0))
plt.xticks(np.arange(0,13.9,2.7714),size=9,rotation=45)
plt.yticks(np.arange(0,14.41+2.40,2.40),size=9)
plt.xlim(0,13.9)
plt.ylim(0,14.41)

#############################################################################
dx=xcenters[1]-xcenters[0]
dy=ycenters[1]-ycenters[0]
summ=0
for i in range(144):
    for j in range(139):
        if gg[i,j] > 0:
             summ=summ+1

area2=summ*dx*dy/(13.8593*14.4030)
##################################################################################################################

print ('Area=',area1,area2)

plt.subplots_adjust(wspace=0.3,hspace=0.5)
plt.savefig("photo_2d.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)


###############################################################################################################
