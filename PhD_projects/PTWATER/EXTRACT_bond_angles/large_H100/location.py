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

wowyy=[]

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
          coord.append(float(t1[3])-mean)

       coord=np.array(coord,float)

       ccoord=[]
       for j in range(atoms+2-hyd,atoms+2):
          t1=aa[j+(i)*(atoms+2)].split()
          ccoord.append(float(t1[3])-mean)

       ccoord=np.array(ccoord,float)



       for j in range(0,1440,3):
   
           sam=np.array(coord[j],float)
           wowx.append(sam)
   
           sam=np.array(coord[j+1],float)
           wowy.append(sam)
   
           sam=np.array(coord[j+2],float)
           wowy.append(sam)

 
       for j in range(0,hyd):
   
           sam=np.array(ccoord[j],float)
           wowyy.append(sam)
   

        
e1=np.array(wowx,float)
e1x=np.amin(e1)
e1y=np.amax(e1)
gg1,xedges=np.histogram(e1, bins=400,range=[0,80],density=True)
xcenters = (xedges[:-1] + xedges[1:]) / 2

e2=np.array(wowy,float)
e2x=np.amin(e2)
e2y=np.amax(e2)
gg2,xedges=np.histogram(e2, bins=400,range=[0,80],density=True)

e3=np.array(wowyy,float)
e3x=np.amin(e3)
e3y=np.amax(e3)
gg3,xedges=np.histogram(e3, bins=400,range=[0,80],density=True)


e4=np.concatenate((wowy,wowyy))
e4x=np.amin(e4)
e4y=np.amax(e4)
gg4,xedges=np.histogram(e4, bins=400,range=[0,80],density=True)


ggg1=np.cumsum(gg1)*(xedges[1]-xedges[0])*480
ggg2=np.cumsum(gg2)*(xedges[1]-xedges[0])*480*2
ggg3=np.cumsum(gg3)*(xedges[1]-xedges[0])*hyd
ggg4=np.cumsum(gg4)*(xedges[1]-xedges[0])*(hyd+480)




f=open(filename,'a')
for i in range(len(gg1)):
    f.write("%.3f  \t %.3f  \t %.3f \t %.3f  \t %.3f \t %.3f  \t %.3f \t %.3f  \t %.3f \n" %(xcenters[i],gg1[i],gg2[i],gg3[i],gg4[i],ggg1[i],ggg2[i],ggg3[i],ggg4[i]))
f.close()

os.system('mv tempo %s '%filename2)




