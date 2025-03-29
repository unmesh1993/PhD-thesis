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
    coord1y1.append(float(x[1])-float(x[2]))
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
    coord1y1.append(float(x[1])-float(x[2]))
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
    coord1y1.append(float(x[1])-float(x[2]))
del x,a
d3x=np.array(coord1x,float)
d3y1=np.array(coord1y1,float)

f=open('ddel2','r')
a=f.readlines()
f.close

coord1x=[]
coord1y1=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[0]))
    coord1y1.append(float(x[1])-float(x[2]))
del x,a
d4x=np.array(coord1x,float)
d4y1=np.array(coord1y1,float)


####################################################################################################
fig = plt.figure()

ax = fig.add_subplot(2,2,1)
x=d1x
y=d1y1
ex=-2
ey=1
gg,xedges,yedges=np.histogram2d(x, y, bins=(500,120),range=[[0.0, 20], [ex, ey]], normed=True)
gg= gg.T ###transpose (please find reason)
#gg[gg == 0] = 0.0001

plt.yticks(np.arange(-50,50,0.2),size=10)
plt.xticks(np.arange(0,16,2),size=10)
plt.xlim(0,7)
plt.ylim(-1.1,0)
plt.xlabel(r'z coordinate of O (Å)',size=12)
plt.ylabel(r'$d_{OH1}-d_{OH2}$ (Å)',size=12)
#plt.title('(a) clean',size=6)
my_cmap = plt.cm.jet
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)

plt.contourf(X, Y, gg, [0.0001,0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
#S=ax.contour(X, Y, gg,[0.0001,0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
cbar.ax.tick_params(labelsize=6)
cbar.set_label(r'prob. dens.', size=6)

ax = fig.add_subplot(2,2,2)
x=d3x
y=d3y1
gg,xedges,yedges=np.histogram2d(x, y, bins=(500,120),range=[[0.0, 20], [ex, ey]], normed=True)
gg= gg.T ###transpose (please find reason)
#gg[gg == 0] = 0.0001

plt.yticks(np.arange(-50,50,0.2),size=10)
plt.xticks(np.arange(0,16,2),size=10)
plt.xlim(0,7)
plt.ylim(-1.1,0)
plt.xlabel(r'z coordinate of O (Å)',size=12)
plt.ylabel(r'$d_{OH1}-d_{OH2}$ (Å)',size=12)
#plt.title('(a) clean',size=6)
my_cmap = plt.cm.jet
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)

plt.contourf(X, Y, gg, [0.0001,0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
#S=ax.contour(X, Y, gg,[0.0001,0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
cbar.ax.tick_params(labelsize=6)
cbar.set_label(r'prob. dens.', size=6)

ax = fig.add_subplot(2,2,3)
x=d2x
y=d2y1
gg,xedges,yedges=np.histogram2d(x, y, bins=(500,120),range=[[0.0, 20], [ex, ey]], normed=True)
gg= gg.T ###transpose (please find reason)
#gg[gg == 0] = 0.0001

plt.yticks(np.arange(-50,50,0.2),size=10)
plt.xticks(np.arange(0,16,2),size=10)
plt.xlim(0,7)
plt.ylim(-1.1,0)
plt.xlabel(r'z coordinate of O (Å)',size=12)
plt.ylabel(r'$d_{OH1}-d_{OH2}$ (Å)',size=12)
#plt.title('(a) clean',size=6)
my_cmap = plt.cm.jet
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)

plt.contourf(X, Y, gg, [0.0001,0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
#S=ax.contour(X, Y, gg,[0.0001,0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
cbar.ax.tick_params(labelsize=6)
cbar.set_label(r'prob. dens.', size=6)


ax = fig.add_subplot(2,2,4)
x=d4x
y=d4y1
gg,xedges,yedges=np.histogram2d(x, y, bins=(500,120),range=[[0.0, 20], [ex, ey]], normed=True)
gg= gg.T ###transpose (please find reason)
#gg[gg == 0] = 0.0001

plt.yticks(np.arange(-50,50,0.2),size=10)
plt.xticks(np.arange(0,16,2),size=10)
plt.xlim(0,7)
plt.ylim(-1.1,0)
plt.xlabel(r'z coordinate of O (Å)',size=12)
plt.ylabel(r'$d_{OH1}-d_{OH2}$ (Å)',size=12)
#plt.title('(a) clean',size=6)
my_cmap = plt.cm.jet
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)

plt.contourf(X, Y, gg, [0.0001,0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
#S=ax.contour(X, Y, gg,[0.0001,0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('jet'),norm = LogNorm())
cbar = plt.colorbar(ticks=None,shrink=1.0,pad=0.0 )
cbar.ax.tick_params(labelsize=6)
cbar.set_label(r'prob. dens.', size=6)




plt.subplots_adjust(wspace=0.5,hspace=0.5)
plt.savefig("photo.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
plt.savefig('photo.pdf')

#plt.show()

