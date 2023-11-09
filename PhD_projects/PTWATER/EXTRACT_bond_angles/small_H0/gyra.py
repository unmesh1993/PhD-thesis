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
from sklearn.neighbors.kde import KernelDensity
from scipy.stats import gaussian_kde
from scipy.stats import kurtosis, skew


import os


res=str(sys.argv[1])
filename2=str(sys.argv[2])

os.system('rm tempo')
filename='tempo'


f=open(res,'r')
aa=f.readlines()
f.close

atoms=np.int(aa[0])
frames=int(len(aa)/(atoms+2))

coord=[]
for i in range(frames):
    for j in range (2,662):
        x=aa[j+i*662].split()
        coord.append(x[1:4])
del aa
coord=np.array(coord,float)
cord=np.split(coord,6)
del coord
print (np.shape(cord))

xO_g=[]
yO_g=[]
xH_g=[]
yH_g=[]
xPt_g=[]
yPt_g=[]

xxPt_g=[]

for i in range(int(frames/6)):
 #########################################################################
    for j in range(0,540,3):
        
        b0=cord[0][j+i*660][:]
        b1=cord[1][j+i*660][:]
        b2=cord[2][j+i*660][:]
        b3=cord[3][j+i*660][:]
        b4=cord[4][j+i*660][:]
        b5=cord[5][j+i*660][:]

    
        cen=(b0+b1+b2+b3+b4+b5)/6
        rgy=((np.linalg.norm(b0-cen)**2+np.linalg.norm(b1-cen)**2+np.linalg.norm(b2-cen)**2+np.linalg.norm(b3-cen)**2+np.linalg.norm(b4-cen)**2+np.linalg.norm(b5-cen)**2)/6)**0.5
        yO_g.append(rgy)
        xO_g.append((b0[2]+b1[2]+b2[2]+b3[2]+b4[2]+b5[2])/6)


#        f=open(filename,'a')
#        f.write("%s  \t %.6f   \n" %('O',rgy))
#        f.close()     

    for j in range(1,540,3):
        
        b0=cord[0][j+i*660][:]
        b1=cord[1][j+i*660][:]
        b2=cord[2][j+i*660][:]
        b3=cord[3][j+i*660][:]
        b4=cord[4][j+i*660][:]
        b5=cord[5][j+i*660][:]

    
        cen=(b0+b1+b2+b3+b4+b5)/6
        rgy=((np.linalg.norm(b0-cen)**2+np.linalg.norm(b1-cen)**2+np.linalg.norm(b2-cen)**2+np.linalg.norm(b3-cen)**2+np.linalg.norm(b4-cen)**2+np.linalg.norm(b5-cen)**2)/6)**0.5
        yH_g.append(rgy)
        xH_g.append((b0[2]+b1[2]+b2[2]+b3[2]+b4[2]+b5[2])/6)
       


    for j in range(2,540,3):
        
        b0=cord[0][j+i*660][:]
        b1=cord[1][j+i*660][:]
        b2=cord[2][j+i*660][:]
        b3=cord[3][j+i*660][:]
        b4=cord[4][j+i*660][:]
        b5=cord[5][j+i*660][:]

    
        cen=(b0+b1+b2+b3+b4+b5)/6
        rgy=((np.linalg.norm(b0-cen)**2+np.linalg.norm(b1-cen)**2+np.linalg.norm(b2-cen)**2+np.linalg.norm(b3-cen)**2+np.linalg.norm(b4-cen)**2+np.linalg.norm(b5-cen)**2)/6)**0.5
        yH_g.append(rgy)
        xH_g.append((b0[2]+b1[2]+b2[2]+b3[2]+b4[2]+b5[2])/6)


    for j in range(540,660):

        b0=cord[0][j+i*660][:]
        b1=cord[1][j+i*660][:]
        b2=cord[2][j+i*660][:]
        b3=cord[3][j+i*660][:]
        b4=cord[4][j+i*660][:]
        b5=cord[5][j+i*660][:]


        cen=(b0+b1+b2+b3+b4+b5)/6
        rgy=((np.linalg.norm(b0-cen)**2+np.linalg.norm(b1-cen)**2+np.linalg.norm(b2-cen)**2+np.linalg.norm(b3-cen)**2+np.linalg.norm(b4-cen)**2+np.linalg.norm(b5-cen)**2)/6)**0.5
        yPt_g.append(rgy)
        xPt_g.append((b0[2]+b1[2]+b2[2]+b3[2]+b4[2]+b5[2])/6)

        if  j >= 630 :
             xxPt_g.append((b0[2]+b1[2]+b2[2]+b3[2]+b4[2]+b5[2])/6)
            
del cord

O_g=np.array(yO_g)
H_g=np.array(yH_g)
Pt_g=np.array(yPt_g)
print ('O',np.mean(O_g),np.std(O_g),np.amax(O_g),np.amin(O_g))
print ('H',np.mean(H_g),np.std(H_g),np.amax(H_g),np.amin(H_g))
print ('Pt',np.mean(Pt_g),np.std(Pt_g),np.amax(Pt_g),np.amin(Pt_g))

minus=np.mean(np.array(xxPt_g))

fig = plt.figure()


ax = fig.add_subplot(311)
y=np.array(yO_g)
x=np.array(xO_g-minus)


gg,xedges,yedges=np.histogram2d(x, y, bins=(500,100),range=[[0, 20], [0.0, np.amax(y)]])
gg= gg.T ###transpose (please find reason)

legend='O'
#plt.title(legend,size=12)
plt.ylabel('g(O) [Å]',size=12)
plt.xlabel('z coordinate of O [Å]',size=12)
plt.yticks(size=10)
plt.xticks(size=10)
my_cmap = plt.cm.Blues
my_cmap = plt.cm.jet
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)
plt.scatter(X, Y, c=gg, label=legend,s=2,cmap=my_cmap,norm = LogNorm())
plt.colorbar(label='population')
plt.legend()

ax = fig.add_subplot(312)
y=np.array(yH_g)
x=np.array(xH_g-minus)

for i in range(len(x)):
   f=open(filename,'a')
   f.write("%.3f  \t %.3f  \n" %(np.array(x[i],float),np.array(y[i],float)))
   f.close()
os.system('mv tempo %s '%filename2)
os.system('rm tempo')


gg,xedges,yedges=np.histogram2d(x, y, bins=(500,100),range=[[0, 20], [0.0, np.amax(y)]])
gg= gg.T ###transpose (please find reason)

legend='H'
#plt.title(legend,size=12)
plt.ylabel('g(H) [Å]',size=12)
plt.xlabel('z coordinate of H [Å]',size=12)
plt.yticks(size=10)
plt.xticks(size=10)
my_cmap = plt.cm.Blues
my_cmap = plt.cm.jet
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)
plt.scatter(X, Y, c=gg, label=legend, s=2,cmap=my_cmap,norm = LogNorm())
plt.colorbar(label='population')
plt.legend()


ax = fig.add_subplot(313)
y=np.array(yPt_g)
x=np.array(xPt_g-minus)
gg,xedges,yedges=np.histogram2d(x, y, bins=(500,100),range=[[-10, 2], [0.0, np.amax(y)]])
gg= gg.T ###transpose (please find reason)

legend='Pt'
#plt.title(legend,size=12)
plt.ylabel('g(Pt) [Å]',size=12)
plt.xlabel('z coordinate of Pt [Å]',size=12)
plt.yticks(size=10)
plt.xticks(size=10)
my_cmap = plt.cm.Blues
my_cmap = plt.cm.jet
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)
plt.scatter(X, Y, c=gg, label=legend,s=2,cmap=my_cmap,norm = LogNorm())
plt.xlim(-8,1)
plt.colorbar(label='population')
plt.legend()









plt.subplots_adjust(wspace=0.3,hspace=0.6)
fig.savefig('photo.pdf')





