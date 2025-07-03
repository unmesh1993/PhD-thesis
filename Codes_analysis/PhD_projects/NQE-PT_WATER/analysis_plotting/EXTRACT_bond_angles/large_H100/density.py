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
dx=float(sys.argv[3])


os.system('rm tempo')
filename='tempo'

vec1=np.array([[19.4,0.0,0.0],[0.0,19.2,0.0],[0.0,0.0,70]],float)
atoms=1720
hyd=56

f=open(res,'r')
aa=f.readlines()
f.close

frames=int(len(aa)/(atoms+2))

coord=[]
ccoord=[]
for i in range(frames):
       cord=[]

       for j in range(1664+2-56,1664+2):
          t1=aa[j+(i)*(atoms+2)].split()
          cord.append(t1[3])

       cord=np.array(cord,float)
       mean=np.mean(cord)

       for j in range(2,1442):
          t1=aa[j+(i)*(atoms+2)].split()
          coord.append(float(t1[3])-mean)

       for j in range(atoms+2-hyd,atoms+2):
          t1=aa[j+(i)*(atoms+2)].split()
          ccoord.append(float(t1[3])-mean)

coord=np.array(coord,float)
ccoord=np.array(coord,float)



rrmax=np.amax(coord)
rrmin=np.amin(coord)
rmin=0
rmax=45
bins=int((rmax-rmin)/dx)



for ff in range(bins):
   zzmin=float(rmin+dx*ff)
   zzmax=float(zzmin+dx)
    
   mo1=np.zeros((frames), dtype=int)
   mo2=np.zeros((frames), dtype=int)
   mo3=np.zeros((frames), dtype=int)
   mo4=np.zeros((frames), dtype=int)
   for i in range(frames):
   
   #########################################################################
       for j in range(0,1440,3):
           t1=coord[j+(i)*1440]
           t2=coord[j+1+(i)*1440]
           t3=coord[j+2+(i)*1440]

           if float(t1) > zzmin and float(t1) <= zzmax:
               mo1[i]=mo1[i]+1
           if float(t2) > zzmin and float(t2) <= zzmax:
               mo2[i]=mo2[i]+1
           if float(t3) > zzmin and float(t3) <= zzmax:
               mo3[i]=mo3[i]+1


       for j in range(0,hyd):
           t1=ccoord[j+(i)*hyd]
           if float(t1) > zzmin and float(t1) <= zzmax:
               mo4[i]=mo4[i]+1

 

   f=open(filename,'a')
   f.write("%.6f  \t %.6f \n" %(zzmin+dx/2,(np.mean(mo1[:])*26.566962+np.mean(mo2[:])*1.6735575+np.mean(mo3[:])*1.6735575+np.mean(mo4[:])*1.6735575)/(vec1[0][0]*vec1[1][1]*dx)))
   f.close()
   del mo1,mo2,mo3,mo4


os.system('mv tempo %s '%filename2)
os.system('rm tempo')

