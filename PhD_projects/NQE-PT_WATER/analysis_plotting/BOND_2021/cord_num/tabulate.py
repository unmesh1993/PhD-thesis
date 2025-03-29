import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.colors import LogNorm


f=open('del1','r')
a=f.readlines()
f.close

coord1x=[]
coord1y1=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[0]))
    coord1y1.append(x[9])
del x,a
d1x=np.array(coord1x,float)
d1y1=np.array(coord1y1,float)


f=open('del2','r')
a=f.readlines()
f.close

coord1x=[]
coord1y1=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[0]))
    coord1y1.append(x[9])
del x,a
d2x=np.array(coord1x,float)
d2y1=np.array(coord1y1,float)


f=open('ddel1','r')
a=f.readlines()
f.close

coord1x=[]
coord1y1=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[0]))
    coord1y1.append(x[9])
del x,a
dd1x=np.array(coord1x,float)
dd1y1=np.array(coord1y1,float)

f=open('ddel2','r')
a=f.readlines()
f.close

coord1x=[]
coord1y1=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[0]))
    coord1y1.append(x[9])
del x,a
dd2x=np.array(coord1x,float)
dd2y1=np.array(coord1y1,float)


##################################################################################
fig = plt.figure()

ax = fig.add_subplot(2,2,1)
x=d1x
y=d1y1
ex=np.amin(d1y1)
ey=np.amax(d1y1)
gg,xedges,yedges=np.histogram2d(x, y, bins=(400,100),range=[[0.0, 20], [0.5, 3.5]], normed=True)
gg= gg.T 

plt.yticks(np.arange(0,50,1.0),size=10)
plt.xticks(np.arange(0,14,2),size=10)
plt.xlim(0,7)
plt.ylim(0.5,3.5)
plt.xlabel(r'z coordinate of O (Å)',size=10)
plt.ylabel(r'CN$_O$',size=12)
my_cmap = plt.cm.jet
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)

plt.contourf(X, Y, gg, [0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
cbar.ax.tick_params(labelsize=8)
cbar.set_label(r'prob. dens.', size=8)


ax = fig.add_subplot(2,2,3)
x=d2x
y=d2y1
ex=np.amin(d2y1)
ey=np.amax(d2y1)
gg,xedges,yedges=np.histogram2d(x, y, bins=(400,100),range=[[0.0, 20], [0.5, 3.5]], normed=True)
gg= gg.T 

plt.yticks(np.arange(0,50,1.0),size=10)
plt.xticks(np.arange(0,14,2),size=10)
plt.xlim(0,7)
plt.ylim(0.5,3.5)
plt.xlabel(r'z coordinate of O (Å)',size=10)
plt.ylabel(r'CN$_O$',size=12)
my_cmap = plt.cm.jet
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)

plt.contourf(X, Y, gg, [0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
cbar.ax.tick_params(labelsize=8)
cbar.set_label(r'prob. dens.', size=8)



ax = fig.add_subplot(2,2,2)
x=dd1x
y=dd1y1
ex=np.amin(dd1y1)
ey=np.amax(dd1y1)
gg,xedges,yedges=np.histogram2d(x, y, bins=(400,100),range=[[0.0, 20], [0.5, 3.5]], normed=True)
gg= gg.T

plt.yticks(np.arange(0,50,1.0),size=10)
plt.xticks(np.arange(0,14,2),size=10)
plt.xlim(0,7)
plt.ylim(0.5,3.5)
plt.xlabel(r'z coordinate of O (Å)',size=10)
plt.ylabel(r'CN$_O$',size=12)
my_cmap = plt.cm.jet
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)

plt.contourf(X, Y, gg, [0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
cbar.ax.tick_params(labelsize=8)
cbar.set_label(r'prob. dens.', size=8)


###
fff1=[]
fff2=[]
for j in range (100):
    for i in range (400):
        if ycenters[j] < 1.3:
           fff1.append(gg[j,i])
           fff2.append(xcenters[i])
fff1=np.array(fff1)
fff2=np.array(fff2)

print (fff2[np.argmax(fff1)])
##

ax = fig.add_subplot(2,2,4)
x=dd2x
y=dd2y1
ex=np.amin(dd2y1)
ey=np.amax(dd2y1)
gg,xedges,yedges=np.histogram2d(x, y, bins=(400,100),range=[[0.0, 20], [0.5, 3.5]], normed=True)
gg= gg.T

plt.yticks(np.arange(0,50,1.0),size=10)
plt.xticks(np.arange(0,14,2),size=10)
plt.xlim(0,7)
plt.ylim(0.5,3.5)
plt.xlabel(r'z coordinate of O (Å)',size=10)
plt.ylabel(r'CN$_O$',size=12)
my_cmap = plt.cm.jet
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)

plt.contourf(X, Y, gg, [0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
cbar.ax.tick_params(labelsize=8)
cbar.set_label(r'prob. dens.', size=8)



plt.subplots_adjust(wspace=0.5,hspace=0.5)
plt.savefig("photo.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
plt.savefig('photo.pdf')
