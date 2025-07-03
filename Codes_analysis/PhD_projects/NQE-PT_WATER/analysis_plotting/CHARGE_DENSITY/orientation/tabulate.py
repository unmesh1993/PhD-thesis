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


def anglem(za1,zb1):
       l1=zb1-za1
       l2=np.array([0,0,1])
       dist1=np.linalg.norm(l1)
       dist2=np.linalg.norm(l2)
       cosine_angle=np.dot(l1,l2) / (dist1 * dist2)
       return cosine_angle
##########################################################
f=open('del1','r')
a=f.readlines()
f.close

f=open('ddel1','r')
aa=f.readlines()
f.close

f=open('del2','r')
b=f.readlines()
f.close

f=open('ddel2','r')
bb=f.readlines()
f.close

##########################################################

const1=13.8593*14.4030


for i in range(frames):

    a1=[]
    a2=[]
    a3=[]
    a4=[]

    c1=[]
    c2=[]
    c3=[]
    c4=[]
    
    d1=[]
    d2=[]
    d3=[]
    d4=[]

###
    for j in range(660-30,660):
        t=a[j+i*660].split()
        a1.append(t[3])
    for j in range(0,540,3):
        t=a[j+i*660].split()
        c1.append(t[1:])
        t=a[j+1+i*660].split()
        d1.append(t[1:])
        t=a[j+2+i*660].split()
        d1.append(t[1:])
    

###
    for j in range(660-30,660):
        t=b[j+i*675].split()
        a2.append(t[3])
    for j in range(0,540,3):
        t=b[j+i*675].split()
        c2.append(t[1:])
        t=b[j+1+i*675].split()
        d2.append(t[1:])
        t=b[j+2+i*675].split()
        d2.append(t)
    for j in range(660,675):
        t=b[j+i*675].split()
        d2.append(t[1:])


###
    for j in range(660-30,660):
        t=aa[j+i*660].split()
        a3.append(t[3])
    for j in range(0,540,3):
        t=aa[j+i*660].split()
        c3.append(t[1:])
        t=aa[j+1+i*660].split()
        d3.append(t[1:])
        t=aa[j+2+i*660].split()
        d3.append(t[1:])

###
    for j in range(660-30,660):
        t=bb[j+i*675].split()
        a4.append(t[3])
    for j in range(0,540,3):
        t=bb[j+i*675].split()
        c4.append(t[1:])
        t=bb[j+1+i*675].split()
        d4.append(t[1:])
        t=bb[j+2+i*675].split()
        d4.append(t)
    for j in range(660,675):
        t=bb[j+i*675].split()
        d4.append(t[1:])



###
    a1=np.array(a1,float)
    a2=np.array(a2,float)
    a3=np.array(a3,float)
    a4=np.array(a4,float)

    c1=np.array(c1,float)
    c2=np.array(c2,float)
    c3=np.array(c3,float)
    c4=np.array(c4,float)

    d1=np.array(d1,float)
    d2=np.array(d2,float)
    d3=np.array(d3,float)
    d4=np.array(d4,float)
    
    
    val1=np.mean(a1)
    val2=np.mean(a2)
    val3=np.mean(a3)
    val4=np.mean(a4)
    
##############################################################################################i
    xxx=[]
    yyy=[]
    for i in range(frames):
        for j in range(len(c1)):
           hyd=0
           sam=np.array(c1[j][0:3],float)
           a1=sam

           hhh1=np.zeros(len(d1),float)
           hhh2=np.zeros(len(d1),3,float)
           counter2=0

           for t in range(len(d1)):
               sam=np.array(d1[t],float)
               b1=sam
               nnn1=np.zeros(9,float)
               nnn4=np.zeros((9,3),float)
               counter1=0

               for k1 in range(-1,2):
                   for k2 in range(-1,2):
                      bb1=np.array(b1+k1*vec1[0,:]+k2*vec1[1,:],float)
                      h1=np.linalg.norm(bb1-a1)
                      nnn1[counter1]=h1
                      nnn4[counter1]=bb1
                      counter1=counter1+1

               hhh1[counter2]=np.min(nnn1)
               hhh2[counter2]=nnn4[np.argmin(nnn1)]
               counter2+=1  

           dipole=c1[3]*c1[1:]
           for t in range(len(d1)):
               if hhh1 < 1.32:
                  cost=anglem(a1,hhh2) 
                  
                                   
                  
 
##############################################################################################

    zx1=z1[:,0]-val1
    zx2=z2[:,0]-val2
    zx3=z3[:,0]-val3
    zx4=z4[:,0]-val4

    zy1=z1[:,1]/(0.529177249*0.529177249*0.529177249) 
    zy2=z2[:,1]/(0.529177249*0.529177249*0.529177249) 
    zy3=z3[:,1]/(0.529177249*0.529177249*0.529177249)
    zy4=z4[:,1]/(0.529177249*0.529177249*0.529177249)
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
    
    
    ssum1,ssum2,ssum3,ssum4=0.00, 0.00, 0.00, 0.00
    sssum1,sssum2,sssum3,sssum4=0.00, 0.00, 0.00, 0.00

    cutoff,cutoff2=mid1,mmid1     
    for j in range(len(zx1)):

        kk=zx1[(zx1 > 0.5) & (zy1 < 0)]
        if zx1[j] >= kk[0]:
            ssum1=ssum1+zy1[j]*dz
    
        if zx1[j] >= cutoff and zx1[j] < cutoff2:
            sssum1=sssum1-zx1[j]*zy1[j]*dz
 
    
    cutoff,cutoff2=mid2,mmid2     
    for j in range(len(zx2)):

        kk=zx2[(zx2 > 0.5) & (zy2 < 0)]
        if zx2[j] >= kk[0]:
            ssum2=ssum2+zy2[j]*dz

        if zx2[j] >= cutoff and zx2[j] < cutoff2:
            sssum2=sssum2-zx2[j]*zy2[j]*dz
    
    cutoff,cutoff2=mid3,mmid3     
    for j in range(len(zx3)):

        kk=zx3[(zx3 > 0.5) & (zy3 < 0)]
        if zx3[j] >= kk[0]:
            ssum3=ssum3+zy3[j]*dz

        if zx3[j] >= cutoff and zx3[j] < cutoff2:
            sssum3=sssum3-zx3[j]*zy3[j]*dz
    
    cutoff,cutoff2=mid4,mmid4     
    for j in range(len(zx4)):

        kk=zx4[(zx4 > 0.5) & (zy4 < 0)]
        if zx4[j] >= kk[0]:
            ssum4=ssum4+zy4[j]*dz
    
        if zx4[j] >= cutoff and zx4[j] < cutoff2:
            sssum4=sssum4-zx4[j]*zy4[j]*dz
    

    cds1.append(ssum1*const1) #charge
    cds2.append(ssum2*const1)
    cds3.append(ssum3*const1)
    cds4.append(ssum4*const1)

    ddip1.append(const6*sssum1/const1)#dipole 
    ddip2.append(const6*sssum2/const1) 
    ddip3.append(const6*sssum3/const1)
    ddip4.append(const6*sssum4/const1)
    
    wwf1.append(const5*(sssum1)) #wavefunction 
    wwf2.append(const5*(sssum2))
    wwf3.append(const5*(sssum3))
    wwf4.append(const5*(sssum4))


cds1=np.array(cds1,float)
ddip1=np.array(ddip1,float)
wwf1=np.array(wwf1,float)

cds2=np.array(cds2,float)
ddip2=np.array(ddip2,float)
wwf2=np.array(wwf2,float)

cds3=np.array(cds3,float)
ddip3=np.array(ddip3,float)
wwf3=np.array(wwf3,float)

cds4=np.array(cds4,float)
ddip4=np.array(ddip4,float)
wwf4=np.array(wwf4,float)

print ('#############################################################################')
print ('Method2:Charge transferred')
print ('mean=',np.mean(cds1),np.mean(cds3),'---',np.mean(cds2),np.mean(cds4))
print ('std=',np.std(cds1),np.std(cds3),'---',np.std(cds2),np.std(cds4))


print ('#############################################################################')
print ('Method2:dipole')
print ('mean=',np.mean(ddip1),np.mean(ddip3),'---',np.mean(ddip2),np.mean(ddip4))
print ('std=',np.std(ddip1),np.std(ddip3),'---',np.std(ddip2),np.std(ddip4))

print ('#############################################################################')
print ('Method2:wf')
print ('mean=',np.mean(wwf1),np.mean(wwf3),'---',np.mean(wwf2),np.mean(wwf4))
print ('std=',np.std(wwf1),np.std(wwf3),'---',np.std(wwf2),np.std(wwf4))

###########################################################################
zx1,zy1,ey1=np.mean(kx1,axis=1),np.mean(ky1*const1,axis=1),np.std(ky1*const1,axis=1)
zx2,zy2,ey2=np.mean(kx2,axis=1),np.mean(ky2*const1,axis=1),np.std(ky2*const1,axis=1)
zx3,zy3,ey3=np.mean(kx3,axis=1),np.mean(ky3*const1,axis=1),np.std(ky3*const1,axis=1)
zx4,zy4,ey4=np.mean(kx4,axis=1),np.mean(ky4*const1,axis=1),np.std(ky4*const1,axis=1)



###########################################################################
###########################################################################
fig=plt.figure()
ax1 = fig.add_subplot(211)


plt.errorbar(zx1,zy1, ey1, color='blue',label='clean: BOMD')
plt.errorbar(zx3,zy3, ey3, color='red' , label='clean: BOMD+PIGLET')

plt.axhline(y=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.axvline(x=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.legend(prop={'size': 6},loc=0)
plt.xticks(np.arange(-100,100,2.0),size=10)
plt.yticks(size=10)
plt.xlim(-10,10)
plt.ylim(-1.5,1.5)
plt.xlabel(r'Distance from Pt surface (Å)',size=10)
plt.ylabel('$\Delta ρ $(z) (e/Å$^3$)',size=10)


ax1 = fig.add_subplot(212)

plt.errorbar(zx2,zy2,ey2, color='darkorange' ,label='0.5 ML: BOMD')
plt.errorbar(zx4,zy4,ey4, color='green', label='0.5ML: BOMD+PIGLET')

plt.axhline(y=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.axvline(x=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.legend(prop={'size': 6},loc=0)
plt.xticks(np.arange(-100,100,2.0),size=10)
plt.yticks(size=10)
plt.xlim(-10,10)
plt.ylim(-1.5,1.5)
plt.xlabel(r'Distance from Pt surface (Å)',size=10)
plt.ylabel('$\Delta ρ $(z) (e/Å$^3$)',size=10)

plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.savefig("photo_1.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
plt.savefig('photo_1.pdf')
###############################################################################################################

