import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.colors import LogNorm

const1=19.4*19.2
const2=0.2081943 # Debye to eA
const5=(-1.60217663*10**(-19)*1.60217663*10**(-19)*6.2709*10**(18))/(8.854*10**(-12)*10**(-10)) 
vdip=1.5
cutoff=4.5
cutoff=100
cutoff=7

f=open('del1','r')
a=f.readlines()
f.close
frames=int(len(a)/480)
ang=np.zeros(frames)
dip=np.zeros(frames)
wfc=np.zeros(frames)
for i in range(frames):
    coord1x=[]
    coord1y1=[]
    coord1y2=[]
    for j in range(480):
        t=j+i*480 
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

print (np.degrees(np.arccos(np.mean(ang))),np.mean(dip),np.mean(wfc))
print ('not-needed',np.std(dip),np.std(wfc))
#####################################################################

f=open('del2','r')
a=f.readlines()
f.close
frames=int(len(a)/480)
ang=np.zeros(frames)
dip=np.zeros(frames)
wfc=np.zeros(frames)
for i in range(frames):
    coord1x=[]
    coord1y1=[]
    coord1y2=[]
    for j in range(480):
        t=j+i*480 
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
wf2=wfc

print (np.degrees(np.arccos(np.mean(ang))),np.mean(dip),np.mean(wfc))
print ('not-needed',np.std(dip),np.std(wfc))

######################################################

f=open('ddel1','r')
a=f.readlines()
f.close
frames=int(len(a)/480)
ang=np.zeros(frames)
dip=np.zeros(frames)
wfc=np.zeros(frames)
for i in range(frames):
    coord1x=[]
    coord1y1=[]
    coord1y2=[]
    for j in range(480):
        t=j+i*480 
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

print (np.degrees(np.arccos(np.mean(ang))),np.mean(dip),np.mean(wfc))
print ('not-needed',np.std(dip),np.std(wfc))

################################################

f=open('ddel2','r')
a=f.readlines()
f.close
frames=int(len(a)/480)
ang=np.zeros(frames)
dip=np.zeros(frames)
wfc=np.zeros(frames)
for i in range(frames):
    coord1x=[]
    coord1y1=[]
    coord1y2=[]
    for j in range(480):
        t=j+i*480 
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
print (np.degrees(np.arccos(np.mean(ang))),np.mean(dip),np.mean(wfc))
print ('not-needed',np.std(dip),np.std(wfc))

fig=plt.figure()
ax1 = fig.add_subplot(211)
#
e1=wf1 
gg1,xedges=np.histogram(e1, bins=10,range=[-0.5,0.5],density=True)
xcenters = (xedges[:-1] + xedges[1:]) / 2 
plt.plot(xcenters,gg1,'-o', color='blue',label='clean: QMMM')
#
e1=wf3 
gg1,xedges=np.histogram(e1, bins=10,range=[-0.5,0.5],density=True)
xcenters = (xedges[:-1] + xedges[1:]) / 2 
plt.plot(xcenters,gg1,'-o', color='red',label='clean: QMMM+PIGLET')
#
e1=wf2 
gg1,xedges=np.histogram(e1, bins=10,range=[-0.5,0.5],density=True)
xcenters = (xedges[:-1] + xedges[1:]) / 2 
plt.plot(xcenters,gg1,'-o', color='darkorange',label='0.5 ML: QMMM')
#
e1=wf4 
gg1,xedges=np.histogram(e1, bins=10,range=[-0.5,0.5],density=True)
xcenters = (xedges[:-1] + xedges[1:]) / 2 
plt.plot(xcenters,gg1,'-o', color='green',label='0.5 ML: QMMM+PIGLET')

plt.axvline(x=0.0, color = 'k',linewidth=1, linestyle = '--')
plt.legend(prop={'size': 6},loc=0)
plt.xticks(np.arange(-0.2,0.5,0.1),size=10)
plt.yticks(size=10)
plt.xlim(-0.3,0.3)
plt.xlabel(r'$\Delta$ WF$_{ori}$ (eV)',size=10)
plt.ylabel('probability density',size=10)
plt.subplots_adjust(wspace=0.4,hspace=0.4) 
plt.savefig("photo_2.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
