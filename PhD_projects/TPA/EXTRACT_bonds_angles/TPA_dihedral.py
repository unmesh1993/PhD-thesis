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
####################################################################

def TPA(natoms,frames,a):

         
       def dihedral(p0,p1,p2,p3):


                       b0 = -1.0*(p1 - p0)
                       b1 = p2 - p1
                       b2 = p3 - p2
                       
                   
                       # normalize b1 so that it does not influence magnitude of vector
                       # rejections that come next
                       b1 /= np.linalg.norm(b1)
                   
                       # vector rejections
                       # v = projection of b0 onto plane perpendicular to b1
                       #   = b0 minus component that aligns with b1
                       # w = projection of b2 onto plane perpendicular to b1
                       #   = b2 minus component that aligns with b1
                       v = b0 - np.dot(b0, b1)*b1
                       w = b2 - np.dot(b2, b1)*b1
                   
                       # angle between v and w in a plane is the torsion angle
                       # v and w may not be normalized but that's fine since tan is y/x
                       x = np.dot(v, w)
                       y = np.dot(np.cross(b1, v), w)
                       return np.degrees(np.arctan2(y, x))
       
       vec1=np.array([19.249512304830585,0.0000000000000000,0.0000000000000000])
       vec2=np.array([-11.556225312311822,9.8917278299989544,0.0000000000000000])
       vec3=np.array([-4.7100804271264112,2.2710568232788395,17.344417844316347])
       
       
       os.system('rm output.txt')
       filename="output.txt"
#       print('#frame_number','CCC-O','CCC=0',file=open("output.txt", "a"))
       
                       
       response=1
       printf=1
       
       for i in range(frames):
           cord=[]
           for j in range(2,362):
               t=a[j+(i)*362].split()
               cord.append(t)
               del t 
           bd5=[] #CCC-O
           bd6=[] #CCC=O
           bd7=[] #C-H
           bd8=[] #(C)H-O
           bd9=[] #C-O
           bd10=[] #CHO
       
           for k in range(0,180,18):
               p1=np.array(cord[k+2][1:],float)
               p2=np.array(cord[k+0][1:],float)
               p3=np.array(cord[k+3][1:],float)
               p4=np.array(cord[k+7][1:],float)
               r1=dihedral(p1,p2,p3,p4)
       
       
               p1=np.array(cord[k+1][1:],float)
               p2=np.array(cord[k+0][1:],float)
               p3=np.array(cord[k+3][1:],float)
               p4=np.array(cord[k+8][1:],float)
               r2=dihedral(p1,p2,p3,p4)

               p1=np.array(cord[k+0][1:],float)
               p2=np.array(cord[k+3][1:],float)
               p3=np.array(cord[k+7][1:],float)
               p4=np.array(cord[k+8][1:],float)
               r3=dihedral(p1,p2,p3,p4)

#               p1=np.array(cord[k+2][1:],float)
#               p2=np.array(cord[k+1][1:],float)
#               p3=np.array(cord[k+11][1:],float)
#               p4=np.array(cord[k+10][1:],float)
#               r4=dihedral(p1,p2,p3,p4)
                
               del p1,p2,p3,p4

               f=open(filename,'a')
               f.write("%.6f  \t %.6f   \t  %.6f \t  %.6f \n " %(i,r1,r2,r3))
               f.close()
#               print(i,r1,r2,file=open("output.txt", "a"))

               p1=np.array(cord[k+9+2][1:],float)
               p2=np.array(cord[k+9+0][1:],float)
               p3=np.array(cord[k+9+3][1:],float)
               p4=np.array(cord[k+9+7][1:],float)
               r1=dihedral(p1,p2,p3,p4) 
       
               p1=np.array(cord[k+9+1][1:],float)
               p2=np.array(cord[k+9+0][1:],float)
               p3=np.array(cord[k+9+3][1:],float)
               p4=np.array(cord[k+9+8][1:],float)
               r2=dihedral(p1,p2,p3,p4)

               p1=np.array(cord[k+9+0][1:],float)
               p2=np.array(cord[k+9+3][1:],float)
               p3=np.array(cord[k+9+7][1:],float)
               p4=np.array(cord[k+9+8][1:],float)
               r3=dihedral(p1,p2,p3,p4)

#               p1=np.array(cord[k+2][1:],float)
#               p2=np.array(cord[k+1][1:],float)
#               p3=np.array(cord[k+11][1:],float)
#               p4=np.array(cord[k+10][1:],float)
#               r4=dihedral(p1,p2,p3,p4)
               


               del p1,p2,p3,p4
#               return np.absolute(r1),np.absolute(r2)
               f=open(filename,'a')
               f.write("%.6f  \t %.6f   \t  %.6f \t  %.6f \n" %(i,r1,r2,r3))
               f.close()
#               print(i,r1,r2,file=open("output.txt", "a"))
       
           for k in range(180,360,18):
       
               p1=np.array(cord[k+9+2][1:],float)
               p2=np.array(cord[k+9+0][1:],float)
               p3=np.array(cord[k+9+3][1:],float)
               p4=np.array(cord[k+9+7][1:],float)
               r1=dihedral(p1,p2,p3,p4) 
       
               p1=np.array(cord[k+9+1][1:],float)
               p2=np.array(cord[k+9+0][1:],float)
               p3=np.array(cord[k+9+3][1:],float)
               p4=np.array(cord[k+9+8][1:],float)
               r2=dihedral(p1,p2,p3,p4)

               p1=np.array(cord[k+9+0][1:],float)
               p2=np.array(cord[k+9+3][1:],float)
               p3=np.array(cord[k+9+7][1:],float)
               p4=np.array(cord[k+9+8][1:],float)
               r3=dihedral(p1,p2,p3,p4)


               del p1,p2,p3,p4

               f=open(filename,'a')
               f.write("%.6f  \t %.6f   \t  %.6f \t  %.6f \n" %(i,r1,r2,r3))
               f.close()
#               print(i,r1,r2,file=open("output.txt", "a"))
       
               p1=np.array(cord[k+2][1:],float)
               p2=np.array(cord[k+0][1:],float)
               p3=np.array(cord[k+3][1:],float)
               p4=np.array(cord[k+7][1:],float)
               r1=dihedral(p1,p2,p3,p4) 
       
               p1=np.array(cord[k+1][1:],float)
               p2=np.array(cord[k+0][1:],float)
               p3=np.array(cord[k+3][1:],float)
               p4=np.array(cord[k+8][1:],float)
               r2=dihedral(p1,p2,p3,p4)

               p1=np.array(cord[k+0][1:],float)
               p2=np.array(cord[k+3][1:],float)
               p3=np.array(cord[k+7][1:],float)
               p4=np.array(cord[k+8][1:],float)
               r3=dihedral(p1,p2,p3,p4)

#               p1=np.array(cord[k+2][1:],float)
#               p2=np.array(cord[k+1][1:],float)
#               p3=np.array(cord[k+11][1:],float)
#               p4=np.array(cord[k+10][1:],float)
#               r4=dihedral(p1,p2,p3,p4)

               del p1,p2,p3,p4
       
               f=open(filename,'a')
               f.write("%.6f  \t %.6f   \t  %.6f \t  %.6f \n" %(i,r1,r2,r3))
               f.close()       
#               print(i,r1,r2,file=open("output.txt", "a"))
       
           del r1,r2
       
       
           del bd5,bd6 
           
           del cord
       del i,j,k,a,natoms,vec1,vec2,vec3,response,frames,printf
       
       
       os.system('mv output.txt properties_2.dat')
       return()       




