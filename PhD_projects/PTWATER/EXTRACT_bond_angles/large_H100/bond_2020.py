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


res=str(sys.argv[1])
filename2=str(sys.argv[2])

os.system('rm tempo')
filename='tempo'

vec1=np.array([[19.4,0.0,0.0],[0.0,19.2,0.0],[0.0,0.0,70]],float)
ivec1=np.linalg.inv(vec1)

    
f=open(res,'r')
aa=f.readlines()
f.close


atoms=1720

frames=int(len(aa)/(atoms+2))
wowx=[]
wowy=[]

wowxx=[]

for i in range(frames):
       print (i)
       cord=[]

       for j in range(1664+2-56,1664+2):
          t1=aa[j+(i)*(atoms+2)].split()
          cord.append(t1[3])

       cord=np.array(cord,float)
       mean=np.mean(cord)

       coord=[]
       for j in range(2,1442):
          t1=aa[j+(i)*(atoms+2)].split()
          t2=np.array(t1[1:],float)
          t2[2]=t2[2]-mean
          coord.append(t2)

       coord=np.array(coord,float)

       for t in range(0,1440,3):

           sam=np.array(coord[t][:],float)
           a1=sam

           sam=np.array(coord[t+1][:],float)
           b1=sam

           sam=np.array(coord[t+2][:],float)
           b2=sam

           d1=np.linalg.norm(b1-a1)      
           d2=np.linalg.norm(b2-a1)

           wowx.append(d1) 
           wowy.append(a1[2]) 
           wowxx.append(b1[2]) 
           wowx.append(d2) 
           wowy.append(a1[2]) 
           wowxx.append(b2[2]) 
     

x=np.array(wowy)
y=np.array(wowx)
z=np.array(wowxx)


f=open(filename,'a')
for i in range(len(x)):
    f.write("%.3f  \t %.3f \t %.3f \n" %(x[i],y[i],z[i]))
f.close()

os.system('mv tempo %s '%filename2)
os.system('rm tempo')


fig=plt.figure()
ax = fig.add_subplot(211)
ex=np.amin(y)
ey=np.amax(y)
gg,xedges,yedges=np.histogram2d(x, y, bins=(500,100),range=[[0.0, 40], [ex, ey]])
gg= gg.T ###transpose (please find reason)
#gg[gg == 0] = 0.0001

plt.ylabel('OH bond length [Å]',size=12)
plt.xlabel('z coordinate of O [Å]',size=12)
plt.yticks(size=10)
plt.xticks(size=10)
my_cmap = plt.cm.jet
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)
plt.scatter(X, Y, c=gg, s=2,cmap=my_cmap,norm = LogNorm())
plt.colorbar(label='population')
fig.savefig('photo.pdf')
plt.savefig("photo.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)


