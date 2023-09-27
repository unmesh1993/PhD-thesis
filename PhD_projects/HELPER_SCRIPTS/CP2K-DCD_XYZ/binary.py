#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:22:23 2019

@author: unmesh
"""


import numpy as np
import os

os.system('rm bead_*.txt')

nbeads=input ('number of beads: ')
natoms=360
nstep=input('number of steps: ')
natoms=int(natoms)
nstep=int(nstep)
nbeads=int(nbeads)
#fn='lol.dcd'
#fn='TPA-position_aligned.dcd-pos-1-1.dcd'

for l in range(1,nbeads+1):
     fn='TPA-position-pos-{}-1.dcd'.format(i)
     fd = open(fn,'rb')
     dtype = \
             np.dtype(([('blk0-0',  'i4',1  ),# 84 (start of first block, size=84 bytes) 
                        ('x1', 'f8', (6,)),#lattice parameter a,gamma,b,beta,alpha,c
                        ('blk0-1',  'i4',1  ),#84
                        ('blk1-0',  'i4',1  ),#164
                        ('x2', 'f4', (natoms,)),#xcordinate
                        ('blk1-1',  'i4',1  ),#84
                        ('blk2-0',  'i4',1  ),#164
                        ('x3', 'f4', (natoms,)),#ycordinate
                        ('blk2-1',  'i4',1  ),#84
                        ('blk3-0',  'i4',1  ),#164
                        ('x4', 'f4', (natoms,)),#zcordinate
                        ('blk3-1',  'i4',1)]))#94
     #E                   (nstep,)))
     
     arr = np.fromfile(fd, dtype, nstep)
     fd.close
     
     #helpa=(arr['x2'][:,0])
     
     cryst_const = np.empty((nstep,6), dtype=np.float64)
     cryst_const[:,0] = arr['x1'][:,0]
     cryst_const[:,1] = arr['x1'][:,2]
     cryst_const[:,2] = arr['x1'][:,5]
     cryst_const[:,3] = arr['x1'][:,4]
     cryst_const[:,4] = arr['x1'][:,3]
     cryst_const[:,5] = arr['x1'][:,1]
     
     coords = np.empty((nstep,natoms,3), dtype=np.float32)
     coords[:,:,0] = arr['x2'][:,:]
     coords[:,:,1] = arr['x3'][:,:]
     coords[:,:,2] = arr['x4'][:,:]
     
     label=[]
     #fn=input('template xyz file: ')
     fn="cord.xyz"
     fd = open(fn,'r')
     a=fd.readlines()
     fd.close
     
     del a[1],a[0]
     for o in range(natoms):
         x=a[o].split()[0]
         label.append(x)
         
     
     filename="bead_" + l + "txt"
     f=open(filename,'a')
     for i in range(nstep):
#         f.write("%.0d \n" %(natoms))
         f.write("%i \n" %(natoms))
         f.write("%.6f  \t %.6f   \t  %.6f   \t  %.6f \t %.6f \t %.6f \n" %(cryst_const[i,0],cryst_const[i,1],cryst_const[i,2],cryst_const[i,3],cryst_const[i,4],cryst_const[i,5]))
         for k in range(natoms):
             f.write("%s  \t %.6f   \t  %.6f   \t  %.6f \n" %(label[k],coords[i,k,0],coords[i,k,1],coords[i,k,2]))

     f.close()

#os.system('mv output.txt position_dcd.xyz')

del a,arr,natoms,nstep,fn,i,k,x



