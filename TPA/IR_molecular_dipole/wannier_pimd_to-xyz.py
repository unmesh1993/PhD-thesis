import numpy as np
from scipy import special
from scipy.stats import entropy, linregress
from matplotlib import pyplot as plt

import os,math

#vec1=np.array([19.249512304830585,0.0000000000000000,0.0000000000000000],float)
#vec2=np.array([-11.556225312311822,9.8917278299989544,0.0000000000000000],float)
#vec3=np.array([-4.7100804271264112,2.2710568232788395,17.344417844316347],float)

#ivec1=np.array([0.05194937,0.0000000,0.0000000],float)
#ivec2=np.array([0.06069097,0.10109457,0.000000],float)
#ivec3=np.array([0.00616066,-0.0132372,0.05765544],float)



index=np.array(['C' ,'C' ,'C' ,'C' ,'H' ,'H' ,'H' ,'O' ,'O' ,'C' ,'C' ,'C' ,'C' ,'H' ,'H' ,'H' ,'O' ,'O'],str)
vec=np.array([[19.249512304830585,0.0000000000000000,0.0000000000000000],[-11.556225312311822,9.8917278299989544,0.0000000000000000],[-4.7100804271264112,2.2710568232788395,17.344417844316347]],float)


#ivec=np.linalg.inv(vec)
#vect=(np.transpose(vec))
#ivect=(np.transpose(ivec))
#print (np.linalg.norm(vec[0][:]))
#print (np.linalg.norm(vec[1][:]))
#print (np.linalg.norm(vec[2][:]))



res1='IR.dat'


f=open(res1,'r')
a=f.readlines()
f.close

os.system('rm del.xyz') 
f=open('del.xyz','a')

frames=int(len(a)/983)


 

for i in range (frames):
        cord=np.zeros((980,3),float)
        f.write("%i  \n" %(980))
        f.write("%s \t %i  \n" %('Frame=',i))
        tt=-1
        for j in range (1,361):
            t=j+i*983
            x=a[t].split()
            x=np.array(x[:3],float)
            x[:]=x[:]+vec[0][:]*0.5
            x[:]=x[:]+vec[1][:]*0.5
            x[:]=x[:]+vec[2][:]*0.5
            cord[j-1][:]=x[:]
            
            del t
            tt=tt+1
            f.write("%s  \t %.6f   \t  %.6f   \t  %.6f \n" %(index[tt],x[0],x[1],x[2]))
            if tt == 17 :
                tt=-1 

        for j in range (361,981):
            t=j+i*983
            x=a[t].split()
            x=np.array(x[:3],float)
            x[:]=x[:]+vec[0][:]*0.5
            x[:]=x[:]+vec[1][:]*0.5
            x[:]=x[:]+vec[2][:]*0.5
            cord[j-1][:]=x[:]
            del t
            f.write("%s  \t %.6f   \t  %.6f   \t  %.6f \n" %('X',x[0],x[1],x[2]))
   

#os.system('vmd del.xyz')

      

     

    
    
        
