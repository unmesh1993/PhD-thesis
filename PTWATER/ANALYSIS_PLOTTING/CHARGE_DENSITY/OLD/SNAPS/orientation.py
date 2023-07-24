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
from scipy.stats import gaussian_kde

import os

frames=int(sys.argv[1])
##############################################################################################

f=open('sdel1','r')
a=f.readlines()
f.close

f=open('sdel2','r')
b=f.readlines()
f.close

f=open('sddel1','r')
aa=f.readlines()
f.close

f=open('sddel2','r')
bb=f.readlines()
f.close

##########################################################
val1=np.zeros(frames,float)
val2=np.zeros(frames,float)
val3=np.zeros(frames,float)
val4=np.zeros(frames,float)
for i in range(frames):
    a1=[]
    a2=[]
    a3=[]
    a4=[]
###
    for j in range(660-30,660):
        t=a[j+i*660].split()
        a1.append(t)
###
    for j in range(660-30,660):
        t=b[j+i*660].split()
        a2.append(t)

###
    for j in range(660-30,660):
        t=aa[j+i*660].split()
        a3.append(t)
###
    for j in range(660-30,660):
        t=bb[j+i*660].split()
        a4.append(t)
###
    a1=np.array(a1,float)
    a2=np.array(a2,float)
    a3=np.array(a3,float)
    a4=np.array(a4,float)

    val1[i]=np.mean(a1)
    val2[i]=np.mean(a2)
    val3[i]=np.mean(a3)
    val4[i]=np.mean(a4)

################################################################################################

const1=13.8593*14.4030
const2=0.2081943 # Debye to eA
const5=(-1.60217663*10**(-19)*1.60217663*10**(-19)*6.2709*10**(18))/(8.854*10**(-12)*10**(-10))
vdip=1.5
cutoff=100

f=open('wfdel1','r')
a=f.readlines()
f.close
frames=int(len(a)/180)
ang=np.zeros(frames)
dip=np.zeros(frames)
wfc=np.zeros(frames)
for i in range(frames):
    coord1x=[]
    coord1y1=[]
    coord1y2=[]
    for j in range(180):
        t=j+i*180
        x=a[t].split()
        if float(x[9]) < 1.5:
           coord1x.append(float(x[0]))
           coord1y1.append(x[5])
           coord1y2.append(float(x[5])*vdip)
        elif float(x[9]) > 2.5:
           coord1x.append(float(x[0]))
           coord1y1.append(x[5])
           coord1y2.append(float(x[5])*vdip)
           coord1x.append(float(x[0]))
           coord1y1.append(x[6])
           coord1y2.append(float(x[6])*vdip)
           coord1x.append(float(x[0]))
           coord1y1.append(x[7])
           coord1y2.append(float(x[7])*vdip)
        else:
           coord1x.append(float(x[0]))
           coord1y1.append(x[5])
           coord1y2.append(float(x[5])*vdip)
           coord1x.append(float(x[0]))
           coord1y1.append(x[6])
           coord1y2.append(float(x[6])*vdip)
    del x
    x0=np.array(coord1x,float)
    y0=np.array(coord1y1,float)
    z0=np.array(coord1y2,float)

    x=x0[x0 < cutoff]
    y=y0[x0 < cutoff]
    z=z0[x0 < cutoff]

    ang[i]=np.sum(y)/len(y)
    dip[i]=np.sum(z)/len(z)
    wfc[i]=(dip[i]/const1)*const5

#    print (np.degrees(np.arccos(ang[i])),dip[i],wfc[i])
wf1=wfc

#####################################################################

f=open('wfdel2','r')
a=f.readlines()
f.close
frames=int(len(a)/180)
ang=np.zeros(frames)
cang=np.zeros(frames)
dip=np.zeros(frames)
wfc=np.zeros(frames)
for i in range(frames):
    coord1x=[]
    coord1y1=[]
    coord1y2=[]
    for j in range(180):
        t=j+i*180
        x=a[t].split()
        if float(x[9]) < 1.5:
           coord1x.append(float(x[0]))
           coord1y1.append(x[5])
           coord1y2.append(float(x[5])*vdip)
        elif float(x[9]) > 2.5:
           coord1x.append(float(x[0]))
           coord1y1.append(x[5])
           coord1y2.append(float(x[5])*vdip)
           coord1x.append(float(x[0]))
           coord1y1.append(x[6])
           coord1y2.append(float(x[6])*vdip)
           coord1x.append(float(x[0]))
           coord1y1.append(x[7])
           coord1y2.append(float(x[7])*vdip)
        else:
           coord1x.append(float(x[0]))
           coord1y1.append(x[5])
           coord1y2.append(float(x[5])*vdip)
           coord1x.append(float(x[0]))
           coord1y1.append(x[6])
           coord1y2.append(float(x[6])*vdip)
    del x
    x0=np.array(coord1x,float)
    y0=np.array(coord1y1,float)
    z0=np.array(coord1y2,float)

    x=x0[x0 < cutoff]
    y=y0[x0 < cutoff]
    z=z0[x0 < cutoff]

    

    ang[i]=np.sum(y)/len(y)
    dip[i]=np.sum(z)/len(z)
    wfc[i]=(dip[i]/const1)*const5

    
    cang[i]=np.sum(y)/len(y)

#    print (np.degrees(np.arccos(ang[i])),dip[i],wfc[i])
wf2=wfc

######################################################

f=open('wfddel1','r')
a=f.readlines()
f.close
frames=int(len(a)/180)
ang=np.zeros(frames)
dip=np.zeros(frames)
wfc=np.zeros(frames)
for i in range(frames):
    coord1x=[]
    coord1y1=[]
    coord1y2=[]
    for j in range(180):
        t=j+i*180
        x=a[t].split()
        if float(x[9]) < 1.5:
           coord1x.append(float(x[0]))
           coord1y1.append(x[5])
           coord1y2.append(float(x[5])*vdip)
        elif float(x[9]) > 2.5:
           coord1x.append(float(x[0]))
           coord1y1.append(x[5])
           coord1y2.append(float(x[5])*vdip)
           coord1x.append(float(x[0]))
           coord1y1.append(x[6])
           coord1y2.append(float(x[6])*vdip)
           coord1x.append(float(x[0]))
           coord1y1.append(x[7])
           coord1y2.append(float(x[7])*vdip)
        else:
           coord1x.append(float(x[0]))
           coord1y1.append(x[5])
           coord1y2.append(float(x[5])*vdip)
           coord1x.append(float(x[0]))
           coord1y1.append(x[6])
           coord1y2.append(float(x[6])*vdip)
    del x
    x0=np.array(coord1x,float)
    y0=np.array(coord1y1,float)
    z0=np.array(coord1y2,float)

    x=x0[x0 < cutoff]
    y=y0[x0 < cutoff]
    z=z0[x0 < cutoff]

    ang[i]=np.sum(y)/len(y)
    dip[i]=np.sum(z)/len(z)
    wfc[i]=(dip[i]/const1)*const5

#    print (np.degrees(np.arccos(ang[i])),dip[i],wfc[i])
wf3=wfc

################################################

f=open('wfddel2','r')
a=f.readlines()
f.close
frames=int(len(a)/180)
ang=np.zeros(frames)
dip=np.zeros(frames)
wfc=np.zeros(frames)
for i in range(frames):
    coord1x=[]
    coord1y1=[]
    coord1y2=[]
    for j in range(180):
        t=j+i*180
        x=a[t].split()
        if float(x[9]) < 1.5:
           coord1x.append(float(x[0]))
           coord1y1.append(x[5])
           coord1y2.append(float(x[5])*vdip)
        elif float(x[9]) > 2.5:
           coord1x.append(float(x[0]))
           coord1y1.append(x[5])
           coord1y2.append(float(x[5])*vdip)
           coord1x.append(float(x[0]))
           coord1y1.append(x[6])
           coord1y2.append(float(x[6])*vdip)
           coord1x.append(float(x[0]))
           coord1y1.append(x[7])
           coord1y2.append(float(x[7])*vdip)
        else:
           coord1x.append(float(x[0]))
           coord1y1.append(x[5])
           coord1y2.append(float(x[5])*vdip)
           coord1x.append(float(x[0]))
           coord1y1.append(x[6])
           coord1y2.append(float(x[6])*vdip)
    del x
    x0=np.array(coord1x,float)
    y0=np.array(coord1y1,float)
    z0=np.array(coord1y2,float)

    x=x0[x0 < cutoff]
    y=y0[x0 < cutoff]
    z=z0[x0 < cutoff]

    ang[i]=np.sum(y)/len(y)
    dip[i]=np.sum(z)/len(z)
    wfc[i]=(dip[i]/const1)*const5

#    print (np.degrees(np.arccos(ang[i])),dip[i],wfc[i])
wf4=wfc

###################################################################################################
fig=plt.figure()

ax1 = fig.add_subplot(211)

ey1=np.zeros(len(zx1))
ey3=np.zeros(len(zx3))
plt.errorbar(zx3,zy3, ey3, color='red' , label='clean: BOMD+PIGLET')
plt.errorbar(zx1,zy1, ey1, color='blue',label='clean: BOMD')

plt.axhline(y=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.axvline(x=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.legend(prop={'size': 6},loc=0)
plt.xticks(np.arange(-100,100,10),size=10)
plt.yticks(size=10)
plt.xlim(-10,45)
plt.ylim(-20,20)
plt.xlabel(r'Distance from Pt surface (Å)',size=10)
plt.ylabel('$ e * ele. pot.$ (z) (eV/Å$^3$)',size=10)

###############################################################################################################


plt.subplots_adjust(wspace=0.4,hspace=0.6)
plt.savefig("photo_22.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
plt.savefig('photo_22.pdf')
###############################################################################################################
