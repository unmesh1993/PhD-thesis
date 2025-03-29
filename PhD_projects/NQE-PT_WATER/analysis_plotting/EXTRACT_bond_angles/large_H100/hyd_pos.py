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
hyd=56

frames=int(len(aa)/(atoms+2))
wowx=[]
wowy=[]

lay1=np.zeros((56,2),float)
lay2=np.zeros((56,2),float)
lay3=np.zeros((56,2),float)

for i in range(frames):
       print (i)
       cord=[]
       count=0
       for j in range(1664+2-56,1664+2):
          t1=aa[j+(i)*(atoms+2)].split()
          cord.append(t1[3])
          
          t2=np.array(t1[1:3],float)
          lay1[count][0]=lay1[count][0]+t2[0]
          lay1[count][1]=lay1[count][1]+t2[1]

          t1=aa[j-56+(i)*(atoms+2)].split()
          t2=np.array(t1[1:3],float)
          lay2[count][0]=lay2[count][0]+t2[0]
          lay2[count][1]=lay2[count][1]+t2[1]

          t1=aa[j-56-56+(i)*(atoms+2)].split()
          t2=np.array(t1[1:3],float)
          lay3[count][0]=lay3[count][0]+t2[0]
          lay3[count][1]=lay3[count][1]+t2[1]

          count=count+1

       cord=np.array(cord,float)
       mean=np.mean(cord)

    

       coord=[]
#       for j in range(2,1442,3):
#          t1=aa[j+1+(i)*(atoms+2)].split()
#          t2=np.array(t1[1:],float)
#          t2[2]=t2[2]-mean
#          if t2[2] < 1.7:
#              coord.append(t2)
#
#          t1=aa[j+2+(i)*(atoms+2)].split()
#          t2=np.array(t1[1:],float)
#          t2[2]=t2[2]-mean
#          if t2[2] < 1.7:
#              coord.append(t2)

       for j in range(atoms+2-hyd,atoms+2):
          t1=aa[j+(i)*(atoms+2)].split()
          t2=np.array(t1[1:],float)
          t2[2]=t2[2]-mean
          if t2[2] < 1.7:
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


fig=plt.figure()
############################
ax = fig.add_subplot(111)

#plt.scatter (lay1[:,0],lay1[:,1],s=200,c='tan',alpha=0.5,label='top')
#plt.scatter (lay2[:,0],lay2[:,1],s=200,c='grey',alpha=0.2,label='hcp')
#plt.scatter (lay3[:,0],lay3[:,1],s=200,c='magenta',alpha=0.1,label='fcc')

plt.scatter (lay1[:,0],lay1[:,1],s=200,c='tan',alpha=1.0,label='top')
plt.scatter (lay2[:,0],lay2[:,1],s=50,c='grey',marker='x',alpha=1.0,label='hcp')
plt.scatter (lay3[:,0],lay3[:,1],s=50,c='magenta',marker='*',alpha=0.5,label='fcc')

x=np.array(wowy)
y=np.array(wowx)
gg,xedges,yedges=np.histogram2d(x, y, bins=(400,400),range=[[0.0,38.8 ], [0, 38.4]],normed=True)
gg= gg.T ###transpose (please find reason)
#gg[gg == 0] = 0.0001

plt.ylabel('b [Å]',size=12)
plt.xlabel('a [Å]',size=12)
plt.yticks(size=10)
plt.xticks(size=10)
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)

print (np.shape(X), np.shape(Y),np.shape(gg))
print (X)
print (Y)
print (gg)
#plt.scatter(X, Y, c=gg, s=2,cmap=my_cmap,norm = LogNorm())

plt.contourf(Y, X, gg, [0.00001,0.0001,0.001,0.01,0.1,1,10],cmap=plt.cm.get_cmap('Blues'),norm = LogNorm())
plt.colorbar(label='population')

###############################

plt.legend(prop={'size': 8},loc=9, bbox_to_anchor=(1.30,1.0))
plt.xticks(np.arange(0,19.40,2.7714),size=10)
plt.yticks(np.arange(0,19.20+2.40,2.40),size=10)
plt.xlim(0,19.4)
plt.ylim(0,19.2)
#plt.grid()
#plt.title('1 ML')
fig.savefig('photo.pdf')
plt.savefig("photo.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)


