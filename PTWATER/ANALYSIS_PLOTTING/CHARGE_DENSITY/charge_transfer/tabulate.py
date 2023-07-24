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
f=open('del1','r')
pa=f.readlines()
f.close

f=open('ddel1','r')
paa=f.readlines()
f.close

f=open('del2','r')
pb=f.readlines()
f.close

f=open('ddel2','r')
pbb=f.readlines()
f.close

##########################################################
cutoff=-5
cutoff2=50
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

const2=4.80320*const1 #(eA to Debye)
const3=6.241506363094*10**(18)*3.33304*10**(-30)*-1.60217663*10**(-19)/(10.8*8.854*10**(-12)*10**(-20))

const4=1.60217663*10**(-19)*10**(6)/(10**(-16))

const5=(-1.60217663*10**(-19)*1.60217663*10**(-19)*6.241509*10**(18))/(8.854*10**(-12)*10**(-10))
const6=4.80320*const1

dz=0.341201*0.529177

wf1=[]
wwf1=[]
dip1=[]
ddip1=[]
cds1=[]
scds1=[]

wf2=[]
wwf2=[]
dip2=[]
ddip2=[]
cds2=[]
scds2=[]

wf3=[]
wwf3=[]
dip3=[]
ddip3=[]
cds3=[]
scds3=[]

wf4=[]
wwf4=[]
dip4=[]
ddip4=[]
cds4=[]
scds4=[]

for i in range(frames):

    a1=[]
    a2=[]
    a3=[]
    a4=[]
    b1=[]
    b2=[]
    b3=[]
    b4=[]
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    
    k2=[]
    k4=[]


###
    for j in range(660-30,660):
        t=a[j+i*660].split()
        a1.append(t)
    for j in range(660-120,660-120+30):
        t=a[j+i*660].split()
        b1.append(t)
    d1=[]
    for j in range(0,540):
        t=a[j+i*660].split()
        d1.append(t)
    
    d1=np.array(d1,float)
    c1.append(np.amax(d1))


###
    for j in range(660-30,660):
        t=b[j+i*660].split()
        a2.append(t)
    for j in range(660-120,660-120+30):
        t=b[j+i*660].split()
        b2.append(t)
    d2=[]
    for j in range(0,540):
        t=b[j+i*660].split()
        d2.append(t)

    d2=np.array(d2,float)
    c2.append(np.amax(d2))

###
    for j in range(660-30,660):
        t=aa[j+i*660].split()
        a3.append(t)
    for j in range(660-120,660-120+30):
        t=aa[j+i*660].split()
        b3.append(t)
    d3=[]
    for j in range(0,540):
        t=aa[j+i*660].split()
        d3.append(t)

    d3=np.array(d3,float)
    c3.append(np.amax(d3))

###
    for j in range(660-30,660):
        t=bb[j+i*660].split()
        a4.append(t)
    for j in range(660-120,660-120+30):
        t=bb[j+i*660].split()
        b4.append(t)
    d4=[]
    for j in range(0,540):
        t=bb[j+i*660].split()
        d4.append(t)

    d4=np.array(d4,float)
    c4.append(np.amax(d4))


###
    a1=np.array(a1,float)
    a2=np.array(a2,float)
    a3=np.array(a3,float)
    a4=np.array(a4,float)
    b1=np.array(b1,float)
    b2=np.array(b2,float)
    b3=np.array(b3,float)
    b4=np.array(b4,float)
    c1=np.array(c1,float)
    c2=np.array(c2,float)
    c3=np.array(c3,float)
    c4=np.array(c4,float)
    
    k2=np.array(k2,float)
    k4=np.array(k4,float)
    
    val1=np.mean(a1)
    val2=np.mean(a2)
    val3=np.mean(a3)
    val4=np.mean(a4)
    vval1=np.mean(b1)
    vval2=np.mean(b2)
    vval3=np.mean(b3)
    vval4=np.mean(b4)
    
    
    mid1=(vval1 - val1)*0.5
    mid2=(vval2 - val2)*0.5
    mid3=(vval3 - val3)*0.5
    mid4=(vval4 - val4)*0.5
    
    mmid1=(65 + np.mean(c1))*0.5 - val1
    mmid2=(65 + np.mean(c2))*0.5 - val2
    mmid3=(65 + np.mean(c3))*0.5 - val3
    mmid4=(65 + np.mean(c4))*0.5 - val4
    
    
    k2=k2-val2
    k4=k4-val4
    
    kmean2=np.mean(k2[k2 < 2.0])
    kmean4=np.mean(k4[k4 < 2.0])

##############################################################################################
    
    z1=[]
    z2=[]
    z3=[]
    z4=[]
    for j in range(fftz):
        t=pa[j+i*fftz].split()
        z1.append(t)
    
        t=pb[j+i*fftz].split()
        z2.append(t)
    
        t=paa[j+i*fftz].split()
        z3.append(t)
    
        t=pbb[j+i*fftz].split()
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


plt.errorbar(zx1,zy1, ey1, color='blue',label='clean: QMMM')
plt.errorbar(zx3,zy3, ey3, color='red' , label='clean: QMMM+PIGLET')

plt.axhline(y=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.axvline(x=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.legend(prop={'size': 6},loc=0)
plt.xticks(np.arange(-100,100,2.0),size=10)
plt.yticks(size=10)
plt.xlim(-10,10)
#plt.ylim(0,4.2)
plt.xlabel(r'Distance from Pt surface (Å)',size=10)
plt.ylabel('$\Delta ρ $(z) (e/Å$^3$)',size=10)


ax1 = fig.add_subplot(212)

plt.errorbar(zx2,zy2,ey2, color='darkorange' ,label='0.5 ML: QMMM')
plt.errorbar(zx4,zy4,ey4, color='green', label='0.5ML: QMMM+PIGLET')

plt.axhline(y=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.axvline(x=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.legend(prop={'size': 6},loc=0)
plt.xticks(np.arange(-100,100,2.0),size=10)
plt.yticks(size=10)
plt.xlim(-10,10)
#plt.ylim(0,4.2)
plt.xlabel(r'Distance from Pt surface (Å)',size=10)
plt.ylabel('$\Delta ρ $(z) (e/Å$^3$)',size=10)

plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.savefig("photo_1.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
plt.savefig('photo_1.pdf')
###############################################################################################################

