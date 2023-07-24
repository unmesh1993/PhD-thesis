import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D # This import has side effects required for the kwarg projection='3d' in the call to fig.add_subplot
import matplotlib.pyplot as plt
import random
import sys
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.colors import LogNorm
from scipy.stats import gaussian_kde
from scipy.optimize import curve_fit
import os

########################################################################################
#Define the Gaussian function
def Gauss(x, H, A, x0, sigma):
    return H + A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))
###################################################################

x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
x6=[]
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
y6=[]

res='del1'
f=open(res,'r')
a=f.readlines()
f.close
cord=[]
for j in range(len(a)):
   xx=a[j].split()
   x1.append(xx[0])

res='del2'
f=open(res,'r')
a=f.readlines()
f.close
cord=[]
for j in range(len(a)):
   xx=a[j].split()
   x2.append(xx[0])

res='del3'
f=open(res,'r')
a=f.readlines()
f.close
cord=[]
for j in range(len(a)):
   xx=a[j].split()
   x3.append(xx[0])

res='del4'
f=open(res,'r')
a=f.readlines()
f.close
cord=[]
for j in range(len(a)):
   xx=a[j].split()
   x4.append(xx[0])


x1=np.array(x1,float)
x2=np.array(x2,float)
x3=np.array(x3,float)
x4=np.array(x4,float)

e=x1
e1,xedges=np.histogram(e, bins=100,range=[0,4], density=True)
xcenters1 = (xedges[:-1] + xedges[1:]) / 2
e=x2
e2,xedges=np.histogram(e, bins=100,range=[0,4], density=True)
xcenters2 = (xedges[:-1] + xedges[1:]) / 2
e=x3
e3,xedges=np.histogram(e, bins=100,range=[0,4], density=True)
xcenters3 = (xedges[:-1] + xedges[1:]) / 2
e=x4
e4,xedges=np.histogram(e, bins=100,range=[0,4], density=True)
xcenters4 = (xedges[:-1] + xedges[1:]) / 2


fig=plt.figure()
ax = fig.add_subplot(211)

##############################################################################################
plt.plot(xcenters1,e1,'--ob', markersize=2, lw=0.5, mfc='white',label='70 K')

po=[1,1,np.mean(x1),np.std(x1)]
xdata=xcenters1
ydata=e1

parameters, covariance = curve_fit(Gauss, xdata, ydata,po)

fit_A = parameters[0]
fit_B = parameters[1]
fit_C = parameters[2]
fit_D = parameters[3]

fit_y = Gauss(xdata, fit_A, fit_B, fit_C, fit_D)

plt.plot(xdata,fit_y,'-b')
plt.axvline(x=fit_C, color = 'b',linewidth=1, linestyle = '--')

print (fit_A,fit_B,fit_C,fit_D)

####

plt.plot(xcenters2,e2,'--or', markersize=2, lw=0.5, mfc='white',label='300 K')

po=[1,1,np.mean(x2),np.std(x2)]
xdata=xcenters2
ydata=e2

parameters, covariance = curve_fit(Gauss, xdata, ydata,po)

fit_A = parameters[0]
fit_B = parameters[1]
fit_C = parameters[2]
fit_D = parameters[3]

fit_y = Gauss(xdata, fit_A, fit_B, fit_C, fit_D)

plt.plot(xdata,fit_y,'-r')
plt.axvline(x=fit_C, color = 'r',linewidth=1, linestyle = '--')

print (fit_A,fit_B,fit_C,fit_D)
##################################################################################################



plt.xlabel('Band Gap (eV)',size=12)
plt.ylabel('prob. density',size=10)
plt.xticks(np.arange(0,10,0.2),size=10)
plt.xlim(1.5,2.7)
#plt.ylim(0,4)
plt.legend(prop={'size': 7},loc=2)

ax = fig.add_subplot(212)

##############################################################################################
plt.plot(xcenters3,e3,'--ob', markersize=2, lw=0.5, mfc='white',label='70 K')

po=[1,1,np.mean(x3),np.std(x3)]
xdata=xcenters3
ydata=e3

parameters, covariance = curve_fit(Gauss, xdata, ydata,po)

fit_A = parameters[0]
fit_B = parameters[1]
fit_C = parameters[2]
fit_D = parameters[3]

fit_y = Gauss(xdata, fit_A, fit_B, fit_C, fit_D)

plt.plot(xdata,fit_y,'-b')
plt.axvline(x=fit_C, color = 'b',linewidth=1, linestyle = '--')

print (fit_A,fit_B,fit_C,fit_D)

####

plt.plot(xcenters4,e4,'--or', markersize=2, lw=0.5, mfc='white',label='300 K')

po=[1,1,np.mean(x4),np.std(x4)]
xdata=xcenters4
ydata=e4

parameters, covariance = curve_fit(Gauss, xdata, ydata,po)

fit_A = parameters[0]
fit_B = parameters[1]
fit_C = parameters[2]
fit_D = parameters[3]

fit_y = Gauss(xdata, fit_A, fit_B, fit_C, fit_D)

plt.plot(xdata,fit_y,'-r')
plt.axvline(x=fit_C, color = 'r',linewidth=1, linestyle = '--')

print (fit_A,fit_B,fit_C,fit_D)
##################################################################################################



plt.xlabel('Band Gap (eV)',size=12)
plt.ylabel('prob. density',size=10)
plt.xticks(np.arange(0,10,0.2),size=10)
plt.xlim(1.5,2.7)
#plt.ylim(0,4)
plt.legend(prop={'size': 7},loc=2)

plt.subplots_adjust(wspace=0.00,hspace=0.6)
fig.savefig('photo.pdf')
plt.savefig("photo.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)

