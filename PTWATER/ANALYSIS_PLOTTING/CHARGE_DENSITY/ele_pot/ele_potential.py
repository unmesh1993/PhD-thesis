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

frames=int(sys.argv[1])
##############################################################################################

f=open('fdel1','r')
fa=f.readlines()
f.close

f=open('fddel1','r')
faa=f.readlines()
f.close

f=open('fdel2','r')
fb=f.readlines()
f.close

f=open('fddel2','r')
fbb=f.readlines()
f.close

###############################################################################################################

f=open('hdel1','r')
ha=f.readlines()
f.close

f=open('hddel1','r')
haa=f.readlines()
f.close

f=open('hdel2','r')
hb=f.readlines()
f.close

f=open('hddel2','r')
hbb=f.readlines()
                                                                                                            
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

fftz=360

kx1=np.zeros((fftz,frames))
kx2=np.zeros((fftz,frames))
kx3=np.zeros((fftz,frames))
kx4=np.zeros((fftz,frames))
ky1=np.zeros((fftz,frames))
ky2=np.zeros((fftz,frames))
ky3=np.zeros((fftz,frames))
ky4=np.zeros((fftz,frames))

const1=13.8593*14.4030 

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
        t=b[j+i*675].split()
        a2.append(t)

###
    for j in range(660-30,660):
        t=aa[j+i*660].split()
        a3.append(t)
###
    for j in range(660-30,660):
        t=bb[j+i*675].split()
        a4.append(t)
###
    a1=np.array(a1,float)
    a2=np.array(a2,float)
    a3=np.array(a3,float)
    a4=np.array(a4,float)
    
    val1=np.mean(a1)
    val2=np.mean(a2)
    val3=np.mean(a3)
    val4=np.mean(a4)

    h1=float(ha[i].split()[0])
    h2=float(hb[i].split()[0])
    h3=float(haa[i].split()[0])
    h4=float(hbb[i].split()[0])

##############################################################################################
    
    z1=[]
    z2=[]
    z3=[]
    z4=[]
    for j in range(fftz):
        t=fa[j+i*fftz].split()
        z1.append(t)
    
        t=fb[j+i*fftz].split()
        z2.append(t)
    
        t=faa[j+i*fftz].split()
        z3.append(t)
    
        t=fbb[j+i*fftz].split()
        z4.append(t)
    
    z1=np.array(z1,float)
    z2=np.array(z2,float)
    z3=np.array(z3,float)
    z4=np.array(z4,float)
    
    ###############################################################################################################

    zx1=z1[:,0]-val1
    zx2=z2[:,0]-val2
    zx3=z3[:,0]-val3
    zx4=z4[:,0]-val4

    zy1=z1[:,1]*(27.211399) - h1
    zy2=z2[:,1]*(27.211399) - h2
    zy3=z3[:,1]*(27.211399) - h3
    zy4=z4[:,1]*(27.211399) - h4
    ###############################################################################################################
    kx1[:,i]=zx1
    kx2[:,i]=zx2
    kx3[:,i]=zx3
    kx4[:,i]=zx4

    ky1[:,i]=zy1
    ky2[:,i]=zy2
    ky3[:,i]=zy3
    ky4[:,i]=zy4
    
 
    ###############################################################################################################
    
    
zx1,zy1,ey1=np.mean(kx1,axis=1),np.mean(ky1,axis=1),np.std(ky1,axis=1)
zx2,zy2,ey2=np.mean(kx2,axis=1),np.mean(ky2,axis=1),np.std(ky2,axis=1)
zx3,zy3,ey3=np.mean(kx3,axis=1),np.mean(ky3,axis=1),np.std(ky3,axis=1)
zx4,zy4,ey4=np.mean(kx4,axis=1),np.mean(ky4,axis=1),np.std(ky4,axis=1)

print ('WF_change')
print (-(zy1[350]-zy1[280]),'---',-(zy3[350]-zy3[280]))
print ('WF_change')
print (-(zy2[350]-zy2[280]),'---',-(zy4[350]-zy4[280]))

###########################################################################
fig=plt.figure()
ax1 = fig.add_subplot(211)

#ey1=np.zeros(len(zx1))
#ey3=np.zeros(len(zx3))
plt.errorbar(zx1,zy1, ey1, color='blue',label='clean: BOMD')
plt.errorbar(zx3,zy3, ey3, color='red' , label='clean: BOMD+PIGLET')

plt.axhline(y=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.axvline(x=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.legend(prop={'size': 6},loc=0)
plt.xticks(np.arange(-100,100,10),size=10)
plt.yticks(size=10)
plt.xlim(-10,55)
plt.ylim(-5,10)
plt.xlabel(r'Distance from Pt surface (Å)',size=10)
plt.ylabel('$ e * ele. pot.$ (z) (eV/Å$^3$)',size=10)

ax1 = fig.add_subplot(212)

#ey2=np.zeros(len(zx2))
#ey4=np.zeros(len(zx4))
plt.errorbar(zx2,zy2,ey2, color='darkorange' ,label='0.5 ML: BOMD')
plt.errorbar(zx4,zy4,ey4, color='green', label='0.5ML: BOMD+PIGLET')

plt.axhline(y=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.axvline(x=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.legend(prop={'size': 6},loc=0)
plt.xticks(np.arange(-100,100,10),size=10)
plt.yticks(size=10)
plt.xlim(-10,55)
plt.ylim(-5,10)
plt.xlabel(r'Distance from Pt surface (Å)',size=10)
plt.ylabel('$ e * ele. pot.$ (z) (eV/Å$^3$)',size=10)

plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.savefig("photo_33.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
plt.savefig('photo_33.pdf')
###############################################################################################################
