import numpy as np
import os
import math
import time
import sys

res=str(sys.argv[1])
filename2=str(sys.argv[2])
os.system('rm tempo')
filename='tempo'

vec1=np.array([[13.8593,0.0,0.0],[0.0,14.4030,0.0],[0.0,0.0,65]],float)
ivec1=np.linalg.inv(vec1)



f=open(res,'r')
aa=f.readlines()
f.close


atoms=660
frames=int(len(aa)/(atoms+2))

    
for i in range(frames):
    f=open(filename,'a')
    f.write("%d \n" %(atoms))
    f.write("%d \n" %(i))
    f.close()
#########################################################################
    for j in range(2,atoms+2):
        
        t=aa[j+(i)*(atoms+2)].split()
        sam=np.array(t[1:],float)
        sam[0]=sam[0]*ivec1[0,0]
        sam[1]=sam[1]*ivec1[1,1]

        sam[0]=sam[0] - math.floor(sam[0])
        sam[1]=sam[1] - math.floor(sam[1])

        sam[0]=sam[0]*vec1[0,0]
        sam[1]=sam[1]*vec1[1,1]


        f=open(filename,'a')
        f.write("%s  \t %.6f   \t  %.6f   \t  %.6f \n" %(t[0],sam[0],sam[1],sam[2]))
        f.close()     
        
os.system('mv tempo %s'%filename2)
os.system('rm tempo')
