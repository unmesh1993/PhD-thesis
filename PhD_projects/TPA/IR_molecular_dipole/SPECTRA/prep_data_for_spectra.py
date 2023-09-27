import numpy as np

import os,math
import sys
import time
start_time = time.time()


res1=str(sys.argv[1])

os.system('rm del1.xyz')
os.system('rm del2.xyz')

f=open(res1,'r')
a=f.readlines()
f.close


frames=int(len(a)/983)


 

for i in range (0,frames,5):

            t1=981+i*983
            t2=982+i*983
            x=a[t1].split()
            x=0.2081943*(1/1.8897261)*np.array(x[:3],float)
            y=a[t2].split()
            y=0.2081943*(1/1.8897261)*np.array(y[:3],float)

            f=open('del1.xyz','a')
            f.write("%i  \n" %(1))
            f.write("%s  \t  %i \n" %('Frame=',i))
            f.write("%s  \t %.6f   \t  %.6f   \t  %.6f \n" %('X',x[0],x[1],x[2]))
            f.close()
            f=open('del2.xyz','a')
            f.write("%i  \n" %(1))
            f.write("%s  \t  %i \n" %('Frame=',i))
            f.write("%s  \t %.6f   \t  %.6f   \t  %.6f \n" %('X',y[0],y[1],y[2]))
            f.close()


