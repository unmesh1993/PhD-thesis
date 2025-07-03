import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.colors import LogNorm
from scipy.stats import gaussian_kde


const=15000

f=open('del1','r')
a=f.readlines()
f.close
del a[0:11]

coord1x=[]
coord1y1=[]
coord1y2=[]
coord1y3=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[1])/1000)
    coord1y1.append(x[2])
    coord1y2.append(x[3])
    coord1y3.append(x[4])
del x,a

aex=np.array(coord1x,float)
a1=np.array(coord1y1,float)
a2=np.array(coord1y2,float)
a3=np.array(coord1y3,float)


f=open('del2','r')
a=f.readlines()
f.close
del a[0:11]

coord1x=[]
coord1y1=[]
coord1y2=[]
coord1y3=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[1])/1000)
    coord1y1.append(x[2])
    coord1y2.append(x[3])
    coord1y3.append(x[4])
del x,a

aaex=np.array(coord1x,float)
aa1=np.array(coord1y1,float)
aa2=np.array(coord1y2,float)
aa3=np.array(coord1y3,float)




f=open('ddel1','r')
a=f.readlines()
f.close
del a[0:11]

coord1x=[]
coord1y1=[]
coord1y2=[]
coord1y3=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[1])/1000)
    coord1y1.append(x[4])
    coord1y2.append(x[7])
    coord1y3.append(x[3])
del x,a

bex=np.array(coord1x,float)
b1=np.array(coord1y1,float)
b2=np.array(coord1y2,float)
b3=np.array(coord1y3,float)


f=open('ddel2','r')
a=f.readlines()
f.close
del a[0:11]

coord1x=[]
coord1y1=[]
coord1y2=[]
coord1y3=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[1])/1000)
    coord1y1.append(x[4])
    coord1y2.append(x[7])
    coord1y3.append(x[3])
del x,a

bbex=np.array(coord1x,float)
bb1=np.array(coord1y1,float)
bb2=np.array(coord1y2,float)
bb3=np.array(coord1y3,float)



####################################################################################################
for i in range(3):

    if i==0:
        fig = plt.figure()
        

        ax = fig.add_subplot(2,2,1)
        a1=a1[len(a1)-const:len(a1)]
        e1=a1
        sstd=np.std(e1)
        smean=np.mean(e1)
        gg1,xedges=np.histogram(e1, bins=50,range=[smean-6*sstd,smean+6*sstd],density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2  
        plt.plot(xcenters,gg1,'--or',markersize=2)

        density = gaussian_kde(e1)
        xs = np.linspace(smean-6*sstd,smean+6*sstd,1000)
        density.covariance_factor = lambda : 0.25
        density._compute_covariance()
        plt.plot(xs,density(xs))
        plt.axvline(x=xs[np.argmax(density(xs))], color = 'k',linewidth=1, linestyle = '--')

        plt.xlabel(r'$E_{KE}$ (Ha)',size=10)
        plt.ylabel(r'prob. density',size=10)
        plt.xlim(smean-3*sstd,smean+3*sstd)

        ax = fig.add_subplot(2,2,3)
        aa1=aa1[len(aa1)-const:len(aa1)]
        e1=aa1
        sstd=np.std(e1)
        smean=np.mean(e1)
        gg1,xedges=np.histogram(e1, bins=50,range=[smean-6*sstd,smean+6*sstd],density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,gg1,'--or',markersize=2)

        density = gaussian_kde(e1)
        xs = np.linspace(smean-6*sstd,smean+6*sstd,1000)
        density.covariance_factor = lambda : 0.25
        density._compute_covariance()
        plt.plot(xs,density(xs))
        plt.axvline(x=xs[np.argmax(density(xs))], color = 'k',linewidth=1, linestyle = '--')

        plt.xlabel(r'$E_{KE}$ (Ha)',size=10)
        plt.ylabel(r'prob. density',size=10)
        plt.xlim(smean-3*sstd,smean+3*sstd)




        ax = fig.add_subplot(2,2,2)
        b1=b1[len(b1)-const:len(b1)]
        e1=b1
        sstd=np.std(e1)
        smean=np.mean(e1)
        gg1,xedges=np.histogram(e1, bins=50,range=[smean-6*sstd,smean+6*sstd],density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,gg1,'--or',markersize=2)

        density = gaussian_kde(e1)
        xs = np.linspace(smean-6*sstd,smean+6*sstd,1000)
        density.covariance_factor = lambda : 0.25
        density._compute_covariance()
        plt.plot(xs,density(xs))
        plt.axvline(x=xs[np.argmax(density(xs))], color = 'k',linewidth=1, linestyle = '--')
         
        plt.xlabel(r'$E_{QKE}$ (Ha)',size=10)
        plt.ylabel(r'prob. density',size=10)
        plt.xlim(smean-3*sstd,smean+3*sstd)



        ax = fig.add_subplot(2,2,4)
        bb1=bb1[len(bb1)-const:len(bb1)]
        e1=bb1
        sstd=np.std(e1)
        smean=np.mean(e1)
        gg1,xedges=np.histogram(e1, bins=50,range=[smean-6*sstd,smean+6*sstd],density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,gg1,'--or',markersize=2)

        density = gaussian_kde(e1)
        xs = np.linspace(smean-6*sstd,smean+6*sstd,1000)
        density.covariance_factor = lambda : 0.25
        density._compute_covariance()
        plt.plot(xs,density(xs))
        plt.axvline(x=xs[np.argmax(density(xs))], color = 'k',linewidth=1, linestyle = '--')

        plt.xlabel(r'$E_{QKE}$ (Ha)',size=10)
        plt.ylabel(r'prob. density',size=10)
        plt.xlim(smean-3*sstd,smean+3*sstd)


        #######


        plt.subplots_adjust(wspace=0.5,hspace=0.5)
        plt.savefig("KE.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
        plt.savefig('KE.pdf')

    if i==1:

        fig = plt.figure()
        

        ax = fig.add_subplot(2,2,1)
        a2=a2[len(a2)-const:len(a2)]
        e1=a2
        sstd=np.std(e1)
        smean=np.mean(e1)
        gg1,xedges=np.histogram(e1, bins=50,range=[smean-6*sstd,smean+6*sstd],density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2  
        plt.plot(xcenters,gg1,'--or',markersize=2)

        density = gaussian_kde(e1)
        xs = np.linspace(smean-6*sstd,smean+6*sstd,1000)
        density.covariance_factor = lambda : 0.25
        density._compute_covariance()
        plt.plot(xs,density(xs))
        plt.axvline(x=xs[np.argmax(density(xs))], color = 'k',linewidth=1, linestyle = '--')

        plt.xlabel(r'Temp (K)',size=10)
        plt.ylabel(r'prob. density',size=10)
        plt.xlim(smean-3*sstd,smean+3*sstd)

        ax = fig.add_subplot(2,2,3)
        aa2=aa2[len(aa2)-const:len(aa2)]
        e1=aa2
        sstd=np.std(e1)
        smean=np.mean(e1)
        gg1,xedges=np.histogram(e1, bins=50,range=[smean-6*sstd,smean+6*sstd],density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,gg1,'--or',markersize=2)

        density = gaussian_kde(e1)
        xs = np.linspace(smean-6*sstd,smean+6*sstd,1000)
        density.covariance_factor = lambda : 0.25
        density._compute_covariance()
        plt.plot(xs,density(xs))
        plt.axvline(x=xs[np.argmax(density(xs))], color = 'k',linewidth=1, linestyle = '--')

        plt.xlabel(r'Temp (K)',size=10)
        plt.ylabel(r'prob. density',size=10)
        plt.xlim(smean-3*sstd,smean+3*sstd)




        ax = fig.add_subplot(2,2,2)
        b2=b2[len(b2)-const:len(b2)]
        e1=b2
        sstd=np.std(e1)
        smean=np.mean(e1)
        gg1,xedges=np.histogram(e1, bins=50,range=[smean-6*sstd,smean+6*sstd],density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,gg1,'--or',markersize=2)

        density = gaussian_kde(e1)
        xs = np.linspace(smean-6*sstd,smean+6*sstd,1000)
        density.covariance_factor = lambda : 0.08
        density._compute_covariance()
        plt.plot(xs,density(xs))
        plt.axvline(x=xs[np.argmax(density(xs))], color = 'k',linewidth=1, linestyle = '--')
         
        plt.xlabel(r'Temp (K)',size=10)
        plt.ylabel(r'prob. density',size=10)
        plt.xlim(smean-3*sstd,smean+3*sstd)



        ax = fig.add_subplot(2,2,4)
        bb2=bb2[len(bb2)-const:len(bb2)]
        e1=bb2
        sstd=np.std(e1)
        smean=np.mean(e1)
        gg1,xedges=np.histogram(e1, bins=50,range=[smean-6*sstd,smean+6*sstd],density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,gg1,'--or',markersize=2)

        density = gaussian_kde(e1)
        xs = np.linspace(smean-6*sstd,smean+6*sstd,1000)
        density.covariance_factor = lambda : 0.08
        density._compute_covariance()
        plt.plot(xs,density(xs))
        plt.axvline(x=xs[np.argmax(density(xs))], color = 'k',linewidth=1, linestyle = '--')

        plt.xlabel(r'Temp (K)',size=10)
        plt.ylabel(r'prob. density',size=10)
        plt.xlim(smean-3*sstd,smean+3*sstd)


        #######


        plt.subplots_adjust(wspace=0.5,hspace=0.5)
        plt.savefig("Temp.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
        plt.savefig('Temp.pdf')

    if i == 2:
        fig = plt.figure()

        ax = fig.add_subplot(2,2,1)
        a3=a3[len(a3)-const:len(a3)]
        e1=a3
        sstd=np.std(e1)
        smean=np.mean(e1)
        gg1,xedges=np.histogram(e1, bins=50,range=[smean-6*sstd,smean+6*sstd],density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,gg1,'--or',markersize=2)

        density = gaussian_kde(e1)
        xs = np.linspace(smean-6*sstd,smean+6*sstd,1000)
        density.covariance_factor = lambda : 0.25
        density._compute_covariance()
        plt.plot(xs,density(xs))
        plt.axvline(x=xs[np.argmax(density(xs))], color = 'k',linewidth=1, linestyle = '--')

        plt.xlabel(r'$E_{PE}$ (Ha)',size=10)
        plt.ylabel(r'prob. density',size=10)
        plt.xlim(smean-3*sstd,smean+3*sstd)

        ax = fig.add_subplot(2,2,3)
        aa3=aa3[len(aa3)-const:len(aa3)]
        e1=aa3
        sstd=np.std(e1)
        smean=np.mean(e1)
        gg1,xedges=np.histogram(e1, bins=50,range=[smean-6*sstd,smean+6*sstd],density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,gg1,'--or',markersize=2)

        density = gaussian_kde(e1)
        xs = np.linspace(smean-6*sstd,smean+6*sstd,1000)
        density.covariance_factor = lambda : 0.25
        density._compute_covariance()
        plt.plot(xs,density(xs))
        plt.axvline(x=xs[np.argmax(density(xs))], color = 'k',linewidth=1, linestyle = '--')

        plt.xlabel(r'$E_{PE}$ (Ha)',size=10)
        plt.ylabel(r'prob. density',size=10)
        plt.xlim(smean-3*sstd,smean+3*sstd)




        ax = fig.add_subplot(2,2,2)
        b3=b3[len(b3)-const:len(b3)]
        e1=b3
        sstd=np.std(e1)
        smean=np.mean(e1)
        gg1,xedges=np.histogram(e1, bins=50,range=[smean-6*sstd,smean+6*sstd],density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,gg1,'--or',markersize=2)

        density = gaussian_kde(e1)
        xs = np.linspace(smean-6*sstd,smean+6*sstd,1000)
        density.covariance_factor = lambda : 0.25
        density._compute_covariance()
        plt.plot(xs,density(xs))
        plt.axvline(x=xs[np.argmax(density(xs))], color = 'k',linewidth=1, linestyle = '--')

        plt.xlabel(r'$E_{PE}$ (Ha)',size=10)
        plt.ylabel(r'prob. density',size=10)
        plt.xlim(smean-3*sstd,smean+3*sstd)



        ax = fig.add_subplot(2,2,4)
        bb3=bb3[len(bb3)-const:len(bb3)]
        e1=bb3
        sstd=np.std(e1)
        smean=np.mean(e1)
        gg1,xedges=np.histogram(e1, bins=50,range=[smean-6*sstd,smean+6*sstd],density=True)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        plt.plot(xcenters,gg1,'--or',markersize=2)

        density = gaussian_kde(e1)
        xs = np.linspace(smean-6*sstd,smean+6*sstd,1000)
        density.covariance_factor = lambda : 0.25
        density._compute_covariance()
        plt.plot(xs,density(xs))
        plt.axvline(x=xs[np.argmax(density(xs))], color = 'k',linewidth=1, linestyle = '--')

        plt.xlabel(r'$E_{PE}$ (Ha)',size=10)
        plt.ylabel(r'prob. density',size=10)
        plt.xlim(smean-3*sstd,smean+3*sstd)


        #######


        plt.subplots_adjust(wspace=0.5,hspace=0.5)
        plt.savefig("PE.jpg", dpi=300, bbox_inches = 'tight',    pad_inches = 0.1)
        plt.savefig('PE.pdf')

