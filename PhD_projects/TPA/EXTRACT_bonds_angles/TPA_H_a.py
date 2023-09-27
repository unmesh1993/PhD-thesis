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
      
         bd1=[] #O-H
         bd2=[] #H-O
         bd3=[] #O-O
         bd4=[] #OHO
     
         for k in range(0,180,18):
             a1=np.array(cord[k+6][1:],float)
             b1=np.array(cord[k+7][1:],float)
             b2=np.array(cord[k+197][1:],float)
             dist1=np.linalg.norm(a1-b1)
             dist2=np.linalg.norm(a1-b2)
             dist3=np.linalg.norm(b1-b2)
             angle=anglem(a1,b1,b2,cord,dist1,dist2)
     
             f=open(filename,'a')
             f.write("%.6f  \t %.6f   \t  %.6f   \t  %.6f \t %.6f \n" %(i,dist1,dist2,dist3,np.degrees(angle)))
             f.close()              
#             print(i,dist1,dist2,dist3,np.degrees(angle),file=open("output.txt", "a"))
     
             a1=np.array(cord[k+15][1:],float)
             b1=np.array(cord[k+16][1:],float)
             b2=np.array(cord[k+188][1:],float)
             b2=np.subtract(b2,vec1)
             dist1=np.linalg.norm(a1-b1)
             dist2=np.linalg.norm(a1-b2)
             dist3=np.linalg.norm(b1-b2)
             angle=anglem(a1,b1,b2,cord,dist1,dist2)
     
     
             f=open(filename,'a')
             f.write("%.6f  \t %.6f   \t  %.6f   \t  %.6f \t %.6f \n" %(i,dist1,dist2,dist3,np.degrees(angle)))
             f.close()              
#             print(i,dist1,dist2,dist3,np.degrees(angle),file=open("output.txt", "a"))
     
     
         for k in range(180,360,18):
             a1=np.array(cord[k+15][1:],float)
             b1=np.array(cord[k+16][1:],float)
             b2=np.array(cord[k-180+8][1:],float)
             dist1=np.linalg.norm(a1-b1)
             dist2=np.linalg.norm(a1-b2)
             dist3=np.linalg.norm(b1-b2)
             angle=anglem(a1,b1,b2,cord,dist1,dist2)
     
     
             f=open(filename,'a')
             f.write("%.6f  \t %.6f   \t  %.6f   \t  %.6f \t %.6f \n" %(i,dist1,dist2,dist3,np.degrees(angle)))
             f.close()              
#             print(i,dist1,dist2,dist3,np.degrees(angle),file=open("output.txt", "a"))
     
             a1=np.array(cord[k+6][1:],float)
             b1=np.array(cord[k+7][1:],float)
             b2=np.array(cord[k-180+17][1:],float)
             b2=np.add(b2,vec1)
             dist1=np.linalg.norm(a1-b1)
             dist2=np.linalg.norm(a1-b2)
             dist3=np.linalg.norm(b1-b2)
             angle=anglem(a1,b1,b2,cord,dist1,dist2)
     
     
             f=open(filename,'a')
             f.write("%.6f  \t %.6f   \t  %.6f   \t  %.6f \t %.6f \n" %(i,dist1,dist2,dist3,np.degrees(angle)))
             f.close()              
#             print(i,dist1,dist2,dist3,np.degrees(angle),file=open("output.txt", "a"))
     
     
         del a1,b1,b2,dist1,dist2,dist3,angle
     
         
         del bd1,bd2,bd3,bd4 
         del cord
     del i,j,k,a,natoms,vec1,vec2,vec3,response,frames,printf
     
     
     os.system('mv output.txt properties_1.dat')
     return()     




