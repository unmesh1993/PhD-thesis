# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:41:36 2018

@author: unmesh
"""
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

#from sklearn.neighbors.kde import KernelDensity
#from scipy.stats import gaussian_kde
#from scipy.stats import kurtosis, skew


import os

os.system('rm log_1.dat')
###################################################################################
tot=np.int(sys.argv[1])
fold=np.int(sys.argv[2])
beads=np.array(str(sys.argv[3]).split(','),int)
sec=str(sys.argv[4]).split(',')
temp=np.array(str(sys.argv[5]).split(','),int)
dim=np.int(sys.argv[6])
###################################################################################


def files(res2):
        f=open(res2,'r')
        a=f.readlines()
        f.close
        
        coord=[]
        for i in range(0,len(a)):
            x=a[i].split()
            coord.append(x)
        coord=np.array(coord,float)
        return (coord)

def cut(xx0,fol,bead,count):
        dd=np.split(xx0,bead)
        s=[]
        for i in range (len(dd[0])):
            for j in range (bead):
               s.append(dd[j][i])
        s=np.array(s,float)
        del dd
        return (s)



#############1.histogram########################################## 
new_colour = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf']

h=np.array(temp)
hh=np.array([0])
sec2=np.concatenate((hh,h))


fig = plt.figure()

mean01=np.zeros((tot),float)
std01=np.zeros((tot),float)
emean01=np.zeros((tot),float)
estd01=np.zeros((tot),float)

for i in range(1,tot+1):
    res2="del{}".format(i)
    coord=files(res2)

    fold=1
    xxx0=coord[:,3]
    x0=np.split(xxx0,fold)

    xxx0=coord[:,4]
    ex0=np.split(xxx0,fold)

    mean=0
    std=0
    emean=0
    estd=0
    for j in range(fold):
        mean=mean+np.mean(x0[j])/fold
        std=std+np.std(x0[j])/fold
        emean=emean+np.mean(ex0[j])/fold
        estd=estd+np.std(ex0[j])/fold

    mean01[i-1]=mean
    std01[i-1]=std
    emean01[i-1]=emean
    estd01[i-1]=estd


    del x0

####################################################################################################################################
mean02=np.zeros((tot),float)
std02=np.zeros((tot),float)
emean02=np.zeros((tot),float)
estd02=np.zeros((tot),float)

for i in range(1,tot+1):
    res2="ddel{}".format(i)
    coord=files(res2)

    fold=1
    xxx0=coord[:,3]
    xx0=cut(xxx0,fold,beads[i-1],i)
    x0=np.split(xx0,fold)

    xxx0=coord[:,4]
    xx0=cut(xxx0,fold,beads[i-1],i)
    ex0=np.split(xx0,fold)


    mean=0
    std=0
    emean=0
    estd=0
    for j in range(fold):
        mean=mean+np.mean(x0[j])/fold
        std=std+np.std(x0[j])/fold
        emean=emean+np.mean(ex0[j])/fold
        estd=estd+np.std(ex0[j])/fold
 

    mean02[i-1]=mean
    std02[i-1]=std
    emean02[i-1]=emean
    estd02[i-1]=estd
    del x0

################################################################################################
mean03=np.zeros((1),float)
std03=np.zeros((1),float)
emean03=np.zeros((1),float)
estd03=np.zeros((1),float)

for i in range(1,2):
    res2="dddel{}".format(i)
    coord=files(res2)

    fold=1
    xxx0=coord[:,3]
    x0=np.split(xxx0,fold)

    xxx0=coord[:,4]
    ex0=np.split(xxx0,fold)

    mean=0
    std=0
    emean=0
    estd=0
    for j in range(fold):
        mean=mean+np.mean(x0[j])/fold
        std=std+np.std(x0[j])/fold
        emean=emean+np.mean(ex0[j])/fold
        estd=estd+np.std(ex0[j])/fold

    mean03[i-1]=mean
    std03[i-1]=std
    emean03[i-1]=emean
    estd03[i-1]=estd


    del x0


################################################################################################
ax1 = fig.add_subplot(211)
plt.errorbar(temp,mean01,yerr=std01,markersize=4, capsize=4,lw=0.5,fmt='--ob',mfc='white',label='BOMD')


for i, txt in enumerate(mean01.round(decimals=2)):
    if i ==0:
        x, y = temp[i]-50, mean01[i]+std01[i]
    else:
        x, y = temp[i], mean01[i]+std01[i]

    text = ' μ={:.2f}\n σ={:.2f}'.format(mean01[i], std01[i])
    ax1.annotate(text, xy=(x,y),size=7,weight='bold',color='blue')


plt.errorbar(temp,mean02,yerr=std02,markersize=4, capsize=4,lw=0.5,fmt='--or',mfc='white',label='PIGLET')


for i, txt in enumerate(mean02.round(decimals=2)):
    if i ==0:
        x, y = temp[i]-50, mean02[i]-std02[i]
    else:
        x, y = temp[i], mean02[i]-std02[i]

    text = ' μ={:.2f}\n σ={:.2f}'.format(mean02[i], std02[i])
    ax1.annotate(text, xy=(x,y),size=7,weight='bold',color='red')

######
plt.errorbar(temp[0],mean03,yerr=std03,markersize=4, capsize=4,lw=0.5,fmt='--oy',mfc='white',label='PIGLET-D')
for i, txt in enumerate(mean03.round(decimals=2)):
    x, y = temp[0]-70, 2.57
    text = 'μ={:.2f}\nσ={:.2f}'.format(mean03[i], std03[i])
    ax1.annotate(text, xy=(x,y),size=7,weight='bold',color='olive')



######

plt.scatter(300,2.608, s=20 , marker = 'x',  c ="green",label='exp[1][2]')
sx, sy = 300-5, 2.608
text = ' ={:.2f}'.format(2.608)
ax1.annotate(text, xy=(sx,sy),size=7,weight='bold',color='green')

plt.scatter(400,2.625, s=20 , marker = 'x',  c ="green")
sx, sy = 400-5, 2.625
text = ' ={:.2f}'.format(2.625)
ax1.annotate(text, xy=(sx,sy),size=7,weight='bold',color='green')




plt.scatter(0,2.626, s=12, c="black",label='0K')
sx, sy = -10, 2.626+0.02
text = ' ={:.2f}'.format(2.626)
ax1.annotate(text, xy=(sx,sy),size=7,weight='bold',color='black')
plt.legend(prop={'size': 6})
#######



################################################################################################
plt.xticks(sec2,sec2,size=10)
plt.yticks(np.arange(0,10,0.1),size=10)
plt.xlim(-35,650)
plt.ylim(2.5,2.85)
plt.legend(prop={'size': 6},loc=7)
plt.ylabel(r'$d_{O{\cdots}O}$(Å)',size=10)
plt.xlabel('Temperature (K)',size=10)





ax1 = fig.add_subplot(212)
plt.errorbar(temp,emean01,yerr=estd01,markersize=4, capsize=4,lw=0.5,fmt='--ob',mfc='white',label='BOMD')


for i, txt in enumerate(emean01.round(decimals=2)):
    if i ==0:
        x, y = temp[i]-50, emean01[i]+estd01[i]
    else:
        x, y = temp[i], emean01[i]+estd01[i]

    text = ' μ={:.2f}\n σ={:.2f}'.format(emean01[i], estd01[i])
    ax1.annotate(text, xy=(x,y),size=7,weight='bold',color='blue')


plt.errorbar(temp,emean02,yerr=estd02,markersize=4, capsize=4,lw=0.5,fmt='--or',mfc='white',label='PIGLET')


for i, txt in enumerate(emean02.round(decimals=2)):
    if i ==0:
        x, y = temp[i]-50, emean02[i]-estd02[i]
    else:
        x, y = temp[i], emean02[i]-estd02[i]

    text = ' μ={:.2f}\n σ={:.2f}'.format(emean02[i], estd02[i])
    ax1.annotate(text, xy=(x,y),size=7,weight='bold',color='red')


########
plt.errorbar(temp[0],emean03,yerr=estd03,markersize=4, capsize=4,lw=0.5,fmt='--oy',mfc='white',label='PIGLET-D')
for i, txt in enumerate(emean03.round(decimals=2)):
    x, y = -10, emean03[i]
    text = 'μ={:.2f}\n σ={:.2f}'.format(emean03[i], estd03[i])
    ax1.annotate(text, xy=(x,y),size=7,weight='bold',color='olive')
#########



plt.scatter(0,176.215085, s=12, c ="black",label='0K')
sx, sy = -10, 174
text = ' ={:.2f}'.format(176.215085)
ax1.annotate(text, xy=(sx,sy),size=7,weight='bold',color='black')



plt.xticks(sec2,sec2,size=10)
plt.yticks(np.arange(0,200,5),size=10)
plt.xlim(-35,650)
plt.ylim(155,182)
plt.legend(prop={'size': 6},loc=7)
plt.ylabel(r'$\langle OHO$ ($^{\circ}$)',size=10)
plt.xlabel('Temperature (K)',size=10)




################################################################################################




plt.subplots_adjust(wspace=0.4,hspace=0.5)
plt.savefig("fig_temp_1_1.jpg", dpi=500, bbox_inches = 'tight',    pad_inches = 0.1)
fig.savefig('fig_temp_1_1.pdf')
#plt.show()







