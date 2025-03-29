#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 23:22:17 2018

@author: unmesh
"""

import numpy as np
import os
import math
import time
###################################################

def TPA(natoms,frames,a):

     vec1=np.array([19.249512304830585,0.0000000000000000,0.0000000000000000])
     vec2=np.array([-11.556225312311822,9.8917278299989544,0.0000000000000000])
     vec3=np.array([-4.7100804271264112,2.2710568232788395,17.344417844316347])

     def anglem(a1,b1,b2,cord,dist1,dist2):
            b1a1=b1-a1
            b2a1=b2-a1
            cosine_angle=np.dot(b1a1,b2a1) / (dist1 * dist2)
            angler=np.arccos(cosine_angle)
            del b1a1,b2a1,cosine_angle
            return angler

     os.system('rm output.txt')
#     print('#frame_number','Covalent_OH','H-bond_OH','C-C bond','<HOH>', file = open("output.txt", "a"))
     filename="output.txt"
#     f=open(filename,'a')
#     f.write("%i \n" %("#frame_number  Covalent_OH H-bond_OH  C-C bond <HOH>"))
#     f.close()
                
     response=1
     printf=1
     
     
     for i in range(frames):
         cord=[]
         for j in range(2,362):
             t=a[j+(i)*362].split()
             cord.append(t)
             del t
      
         for k in range(0,360,18):
             a0=np.array(cord[k+0][1:],float)
             a1=np.array(cord[k+1][1:],float)
             a2=np.array(cord[k+2][1:],float)
             a3=np.array(cord[k+3][1:],float)
             a7=np.array(cord[k+7][1:],float)
             a8=np.array(cord[k+8][1:],float)
             a9=np.array(cord[k+9][1:],float)
             a10=np.array(cord[k+10][1:],float)
             a11=np.array(cord[k+11][1:],float)
             a12=np.array(cord[k+12][1:],float)
             a16=np.array(cord[k+16][1:],float)
             a17=np.array(cord[k+17][1:],float)

             dist1=np.linalg.norm(a3-a7)
             dist2=np.linalg.norm(a3-a8)
             dist3=np.linalg.norm(a12-a16)
             dist4=np.linalg.norm(a12-a17)
             dist5=np.linalg.norm(a0-a3)
             dist6=np.linalg.norm(a9-a12)
             dist7=np.linalg.norm(a0-a1)
             dist8=np.linalg.norm(a9-a11)
             dist9=np.linalg.norm(a2-a10)
             dist10=np.linalg.norm(a0-a2)
             dist11=np.linalg.norm(a9-a10)
             dist12=np.linalg.norm(a1-a11)
     
             f=open(filename,'a')
             f.write("%.6f  \t %.6f   \t  %.6f   \t  %.6f \t %.6f  \t %.6f  \t %.6f   \t  %.6f   \t  %.6f \t %.6f  \t %.6f   \t  %.6f  \t  %.6f \n" %(i,dist1,dist2,dist3,dist4,dist5,dist6,dist7,dist8,dist9,dist10,dist11,dist12))
             f.close()              
#             print(i,dist1,dist2,dist3,np.degrees(angle),file=open("output.txt", "a"))
     
     
     
     
     
     
         
         del cord
     del i,j,k,a,natoms,vec1,vec2,vec3,response,frames,printf
     
     
     os.system('mv output.txt properties_5.dat')
     return()     




