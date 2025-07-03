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

     def anglem(a1,b1,b2,cord,i):
            dist1=np.linalg.norm(a1-b1)
            dist2=np.linalg.norm(a1-b2)
            dist3=np.linalg.norm(b1-b2)
            b1a1=b1-a1
            b2a1=b2-a1
            cosine_angle=np.dot(b1a1,b2a1) / (dist1 * dist2)
            angle=np.arccos(cosine_angle)
            del b1a1,b2a1,cosine_angle
            f=open(filename,'a')
            f.write("%.6f  \t %.6f   \t  %.6f   \t  %.6f \t %.6f \n" %(i,dist2,dist1,dist3,np.degrees(angle)))
            f.close()
#            print(i,dist1,dist2,dist3,np.degrees(angle),file=open("output2.txt", "a"))
            return ()

     def anglem2(a1,b1,b2,cord,i):
            dist1=np.linalg.norm(a1-b1)
            dist2=np.linalg.norm(a1-b2)
            dist3=np.linalg.norm(b1-b2)
            b1a1=b1-a1
            b2a1=b2-a1
            cosine_angle=np.dot(b1a1,b2a1) / (dist1 * dist2)
            angle=np.arccos(cosine_angle)
            del b1a1,b2a1,cosine_angle
            f=open(filename2,'a')
            f.write("%.6f  \t %.6f   \t  %.6f   \t  %.6f \t %.6f \n" %(i,dist2,dist1,dist3,np.degrees(angle)))
            f.close()
#            print(i,dist1,dist2,dist3,np.degrees(angle),file=open("output2.txt", "a"))
            return ()


     os.system('rm output.txt')
     os.system('rm output2.txt')
     filename="output.txt"
     filename2="output2.txt" 
#     print('#frame_number','Covalent_OH','H-bond_OH','C-C bond','<HOH>',file=open("output.txt", "a"))
#     print('#frame_number','Covalent_OH','H-bond_OH','C-C bond','<HOH>',file=open("output2.txt", "a"))
                     
     response=1
     
     
     for i in range(frames):
         cord=[]
         for j in range(2,362):
             t=a[j+(i)*362].split()
             cord.append(t)
             del t
      
         bd1=[] #C-H
         bd2=[] #H-O
         bd3=[] #C-O
         bd4=[] #OHC
         

         it1=0
         it2=0
         it3=0
         it4=0
         it5=0
         it6=0
         it7=0
         it8=0
         for k in range(0,180,18):
             if k < 72:
                a1=np.array(cord[122+it1*18][1:],float)
                b1=np.array(cord[k+7][1:],float)
                b2=np.array(cord[119+it1*18][1:],float)
                b2=np.subtract(b2,vec2)
                a1=np.subtract(a1,vec2)
                anglem(a1,b1,b2,cord,i)
                it1=it1+1
             elif k == 72:
                a1=np.array(cord[104][1:],float)
                b1=np.array(cord[k+7][1:],float)
                b2=np.array(cord[101][1:],float)
                b2=np.subtract(b2,vec2)
                b2=np.add(b2,vec3)
                a1=np.subtract(a1,vec2)
                a1=np.add(a1,vec3)
                anglem(a1,b1,b2,cord,i)
             elif k > 72 and k < 162:
                a1=np.array(cord[32+it2*18][1:],float)
                b1=np.array(cord[k+7][1:],float)
                b2=np.array(cord[29+it2*18][1:],float)
                anglem(a1,b1,b2,cord,i)
                it2=it2+1
             elif k == 162:
                a1=np.array(cord[14][1:],float)
                b1=np.array(cord[k+7][1:],float)
                b2=np.array(cord[11][1:],float)
                b2=np.add(b2,vec3)
                a1=np.add(a1,vec3)
                anglem(a1,b1,b2,cord,i)
  
     
             
############################################################### 
             if k == 0:
                a1=np.array(cord[355][1:],float)
                b1=np.array(cord[k+8][1:],float)
                b2=np.array(cord[352][1:],float)
                b2=np.subtract(b2,vec3)
                a1=np.subtract(a1,vec3)
                anglem2(a1,b1,b2,cord,i)
             elif k > 0 and k < 90:
                a1=np.array(cord[283+it3*18][1:],float)
                b1=np.array(cord[k+8][1:],float)
                b2=np.array(cord[280+it3*18][1:],float)
                anglem2(a1,b1,b2,cord,i)
                it3=it3+1
             elif k == 90:
                a1=np.array(cord[265][1:],float)
                b1=np.array(cord[k+8][1:],float)
                b2=np.array(cord[262][1:],float)
                b2=np.subtract(b2,vec3)
                b2=np.add(b2,vec2)
                a1=np.subtract(a1,vec3)
                a1=np.add(a1,vec2)
                anglem2(a1,b1,b2,cord,i)
             elif k > 90 and k < 180:
                a1=np.array(cord[193+it4*18][1:],float)
                b1=np.array(cord[k+8][1:],float)
                b2=np.array(cord[190+it4*18][1:],float)
                b2=np.add(b2,vec2)
                a1=np.add(a1,vec2)
                anglem2(a1,b1,b2,cord,i)
                it4=it4+1
     
#####################################################################################################     
             if k == 0:
                a1=np.array(cord[167][1:],float)
                b1=np.array(cord[k+16][1:],float)
                b2=np.array(cord[164][1:],float)
                b2=np.subtract(b2,vec3)
                a1=np.subtract(a1,vec3)
                anglem(a1,b1,b2,cord,i)
             elif k > 0 and k < 90:
                a1=np.array(cord[95+it5*18][1:],float)
                b1=np.array(cord[k+16][1:],float)
                b2=np.array(cord[92+it5*18][1:],float)
                anglem(a1,b1,b2,cord,i)
                it5=it5+1
             elif k == 90:
                a1=np.array(cord[77][1:],float)
                b1=np.array(cord[k+16][1:],float)
                b2=np.array(cord[74][1:],float)
                b2=np.subtract(b2,vec3)
                b2=np.add(b2,vec2)
                a1=np.subtract(a1,vec3)
                a1=np.add(a1,vec2)
                anglem(a1,b1,b2,cord,i)
             elif k > 90 and k < 180:
                a1=np.array(cord[5+it6*18][1:],float)
                b1=np.array(cord[k+16][1:],float)
                b2=np.array(cord[2+it6*18][1:],float)
                b2=np.add(b2,vec2)
                a1=np.add(a1,vec2)
                anglem(a1,b1,b2,cord,i)
                it6=it6+1

#########################################################################
             if k < 72:
                a1=np.array(cord[292+it7*18][1:],float)
                b1=np.array(cord[k+17][1:],float)
                b2=np.array(cord[289+it7*18][1:],float)
                b2=np.subtract(b2,vec2)
                b2=np.subtract(b2,vec1)
                a1=np.subtract(a1,vec2)
                a1=np.subtract(a1,vec1)
                anglem2(a1,b1,b2,cord,i)
                it7=it7+1
             elif k == 72:
                a1=np.array(cord[274][1:],float)
                b1=np.array(cord[k+17][1:],float)
                b2=np.array(cord[271][1:],float)
                b2=np.subtract(b2,vec2)
                b2=np.subtract(b2,vec1)
                b2=np.add(b2,vec3)
                a1=np.subtract(a1,vec2)
                a1=np.subtract(a1,vec1)
                a1=np.add(a1,vec3)
                anglem2(a1,b1,b2,cord,i)
             elif k > 72 and k < 162:
                a1=np.array(cord[202+it8*18][1:],float)
                b1=np.array(cord[k+17][1:],float)
                b2=np.array(cord[199+it8*18][1:],float)
                b2=np.subtract(b2,vec1)
                a1=np.subtract(a1,vec1)
                anglem2(a1,b1,b2,cord,i)
                it8=it8+1
             elif k == 162:
                a1=np.array(cord[184][1:],float)
                b1=np.array(cord[k+17][1:],float)
                b2=np.array(cord[181][1:],float)
                b2=np.subtract(b2,vec1)
                b2=np.add(b2,vec3)
                a1=np.subtract(a1,vec1)
                a1=np.add(a1,vec3)
                anglem2(a1,b1,b2,cord,i)
#####################################################################################################
         it1=0 
         it2=0 
         it3=0 
         it4=0 
         it5=0 
         it6=0 
         it7=0 
         it8=0 
         for k in range(180,360,18):

             if k == 180:
                a1=np.array(cord[347][1:],float)
                b1=np.array(cord[k+16][1:],float)
                b2=np.array(cord[344][1:],float)
                b2=np.subtract(b2,vec3)
                a1=np.subtract(a1,vec3)
                anglem(a1,b1,b2,cord,i)
             elif k > 180 and k < 270:
                a1=np.array(cord[275+it1*18][1:],float)
                b1=np.array(cord[k+16][1:],float)
                b2=np.array(cord[272+it1*18][1:],float)
                anglem(a1,b1,b2,cord,i)
                it1=it1+1
             elif k == 270:
                a1=np.array(cord[257][1:],float)
                b1=np.array(cord[k+16][1:],float)
                b2=np.array(cord[254][1:],float)
                b2=np.subtract(b2,vec3)
                b2=np.add(b2,vec2)
                a1=np.subtract(a1,vec3)
                a1=np.add(a1,vec2)
                anglem(a1,b1,b2,cord,i)
             elif k > 270 and k < 360:
                a1=np.array(cord[185+it2*18][1:],float)
                b1=np.array(cord[k+16][1:],float)
                b2=np.array(cord[182+it2*18][1:],float)
                b2=np.add(b2,vec2)
                a1=np.add(a1,vec2)
                anglem(a1,b1,b2,cord,i)
                it2=it2+1
     
###############################################################     
             if k < 252:
                a1=np.array(cord[112+it3*18][1:],float)
                b1=np.array(cord[k+17][1:],float)
                b2=np.array(cord[109+it3*18][1:],float)
                b2=np.subtract(b2,vec2)
                a1=np.subtract(a1,vec2)
                anglem2(a1,b1,b2,cord,i)
                it3=it3+1
             elif k == 252:
                a1=np.array(cord[94][1:],float)
                b1=np.array(cord[k+17][1:],float)
                b2=np.array(cord[91][1:],float)
                b2=np.subtract(b2,vec2)
                b2=np.add(b2,vec3)
                a1=np.subtract(a1,vec2)
                a1=np.add(a1,vec3)
                anglem2(a1,b1,b2,cord,i)
             elif k > 252 and k < 342:
                a1=np.array(cord[22+it4*18][1:],float)
                b1=np.array(cord[k+17][1:],float)
                b2=np.array(cord[19+it4*18][1:],float)
                anglem2(a1,b1,b2,cord,i)
                it4=it4+1
             elif k == 342:
                a1=np.array(cord[4][1:],float)
                b1=np.array(cord[k+17][1:],float)
                b2=np.array(cord[1][1:],float)
                b2=np.add(b2,vec3)
                a1=np.add(a1,vec3)
                anglem2(a1,b1,b2,cord,i)

###############################################################
             if k < 252:
                a1=np.array(cord[302+it5*18][1:],float)
                b1=np.array(cord[k+7][1:],float)
                b2=np.array(cord[299+it5*18][1:],float)
                b2=np.subtract(b2,vec2)
                a1=np.subtract(a1,vec2)
                anglem(a1,b1,b2,cord,i)
                it5=it5+1
             elif k == 252:
                a1=np.array(cord[284][1:],float)
                b1=np.array(cord[k+7][1:],float)
                b2=np.array(cord[281][1:],float)
                b2=np.subtract(b2,vec2)
                b2=np.add(b2,vec3)
                a1=np.subtract(a1,vec2)
                a1=np.add(a1,vec3)
                anglem(a1,b1,b2,cord,i)
             elif k > 252 and k < 342:
                a1=np.array(cord[212+it6*18][1:],float)
                b1=np.array(cord[k+7][1:],float)
                b2=np.array(cord[209+it6*18][1:],float)
                anglem(a1,b1,b2,cord,i)
                it6=it6+1
             elif k == 342:
                a1=np.array(cord[194][1:],float)
                b1=np.array(cord[k+7][1:],float)
                b2=np.array(cord[191][1:],float)
                b2=np.add(b2,vec3)
                a1=np.add(a1,vec3)
                anglem(a1,b1,b2,cord,i)

###############################################################
             if k == 180:
                a1=np.array(cord[175][1:],float)
                b1=np.array(cord[k+8][1:],float)
                b2=np.array(cord[172][1:],float)
                b2=np.subtract(b2,vec3)
                b2=np.add(b2,vec1)
                a1=np.subtract(a1,vec3)
                a1=np.add(a1,vec1)
                anglem2(a1,b1,b2,cord,i)
             elif k > 180 and k < 270:
                a1=np.array(cord[103+it7*18][1:],float)
                b1=np.array(cord[k+8][1:],float)
                b2=np.array(cord[100+it7*18][1:],float)
                b2=np.add(b2,vec1)
                a1=np.add(a1,vec1)
                anglem2(a1,b1,b2,cord,i)
                it7=it7+1
             elif k == 270:
                a1=np.array(cord[85][1:],float)
                b1=np.array(cord[k+8][1:],float)
                b2=np.array(cord[82][1:],float)
                b2=np.subtract(b2,vec3)
                b2=np.add(b2,vec2)
                b2=np.add(b2,vec1)
                a1=np.subtract(a1,vec3)
                a1=np.add(a1,vec2)
                a1=np.add(a1,vec1)
                anglem2(a1,b1,b2,cord,i)
             elif k > 270 and k < 360:
                a1=np.array(cord[13+it8*18][1:],float)
                b1=np.array(cord[k+8][1:],float)
                b2=np.array(cord[10+it8*18][1:],float)
                b2=np.add(b2,vec2)
                b2=np.add(b2,vec1)
                a1=np.add(a1,vec2)
                a1=np.add(a1,vec1)
                anglem2(a1,b1,b2,cord,i)
                it8=it8+1

######################################################################################################     
         del a1,b1,b2,it1,it2,it3,it4,it5,it6,it7,it8
     
         
         del cord
     del i,j,k,a,natoms,vec1,vec2,vec3,response,frames
     
     
     
     os.system('mv output.txt properties_3.dat')
     os.system('mv output2.txt properties_4.dat')
     return()     




