import numpy as np
import os
import math
import time

import sys

res=str(sys.argv[1])
filename2=str(sys.argv[2])
zzmin=float(sys.argv[3])
zzmax=float(sys.argv[4])
dx=float(sys.argv[5])

os.system('rm tempo')
filename='tempo'

atoms=1720

start_time = time.time()
vec1=np.array([[19.4,0.0,0.0],[0.0,19.2,0.0],[0.0,0.0,70]],float)
ivec1=np.linalg.inv(vec1)

rmax=9.6
rmin=0.0
#dx=0.2
bins=int((rmax-rmin)/dx)
h=zzmax-zzmin

f=open(res,'r')
aa=f.readlines()
f.close

frames=int(len(aa)/(atoms+2))

    
mo=np.zeros((frames,bins), dtype=float)

for i in range(frames):
    print (i)
    cord=[]
    for j in range(1664+2-56,1664+2):
       t1=aa[j+(i)*(atoms+2)].split()
       cord.append(t1[3])

    cord=np.array(cord,float)
    mean=np.mean(cord)
   
    del cord
 
#########################################################################
    coord1=[]
    coord2=[]
    for j in range(2,1442,3):
       t1=aa[j+(i)*(atoms+2)].split()
       t2=np.array(t1[1:],float)
       t2[2]=t2[2]-mean

       t1=aa[j+1+(i)*(atoms+2)].split()
       t3=np.array(t1[1:],float)
       t3[2]=t3[2]-mean
       t1=aa[j+2+(i)*(atoms+2)].split()
       t4=np.array(t1[1:],float)
       t4[2]=t4[2]-mean
       
       if (float(t2[2])) > zzmin and (float(t2[2])) <= zzmax :
           coord1.append(t2)
       if (float(t3[2])) > zzmin and (float(t3[2])) <= zzmax :
           coord2.append(t3)
       if (float(t4[2])) > zzmin and (float(t4[2])) <= zzmax:
           coord2.append(t4)

    for j in range(2+1664,atoms+2,1):
       t1=aa[j+(i)*(atoms+2)].split()
       t2=np.array(t1[1:],float)
       t2[2]=t2[2]-mean

       if (float(t2[2])) > zzmin and (float(t2[2])) <= zzmax :
           coord2.append(t2)



    sam1=np.array(coord1,float)
    sam2=np.array(coord2,float)

#########################################################################
    for j in range(len(sam1)):
        a=np.array(sam1[j],float)
        for k in range(0,len(sam2)):
               b=np.array(sam2[k],float)

               hh1=[]
               for k1 in range(-1,2):
                   for k2 in range(-1,2):

                      bb=np.array(b+k1*vec1[0,:]+k2*vec1[1,:],float)
                      h1=np.linalg.norm(bb-a)
                      hh1.append(h1)
   
               hh1=np.array(hh1,float)
               rrmin=np.amin(hh1)

               for x in range(bins):
                    if rrmin >= float(rmin+x*dx) and rrmin <  float(rmin+(x+1)*dx):
       
                        inside=rmin+ x*dx 
                        outside=rmin + (x+1) * dx
       
                        if float(a[2] - outside) >= float(zzmin) and float(a[2] + outside) <= float(zzmax):
                           vol=(4/3)*math.pi*(outside**3-inside**3)
       
                        elif float(a[2] - outside) >= float(zzmin) and float(a[2] + outside) > float(zzmax):
                           p=a[2]+outside-zzmax
                           volt=(4/3)*math.pi*(outside**3-inside**3)
                           volo=((1/3)*math.pi*p**2*(3*outside-p))
                           p=a[2]+inside-zzmax
                           voli=((1/3)*math.pi*p**2*(3*inside-p))
                           vol=volt-(volo-voli)
                           del volt,voli,volo
       
                        elif float(a[2] - outside) < float(zzmin) and float(a[2] + outside) <= float(zzmax):
                           p=(-a[2]+outside)+zzmin
                           volt=(4/3)*math.pi*(outside**3-inside**3)
                           volo=((1/3)*math.pi*p**2*(3*outside-p))
                           p=(-a[2]+inside)+zzmin
                           voli=((1/3)*math.pi*p**2*(3*inside-p))
                           vol=volt-(volo-voli)
                           del volt,voli,volo
       
                        elif float(a[2] - outside) < float(zzmin) and float(a[2] + outside) > float(zzmax):
                           vol=math.pi*h*(outside**2-inside**2)

                                                 
                        mo[i,x]=mo[i,x] + (1.0/(dx*vol))
                        del vol
        del a
    mo[i,:]=mo[i,:]*((vec1[0][0]*vec1[1][1]*h)/(len(sam1)*(len(sam2))))


    

for x in range(bins):
        f=open(filename,'a')
        f.write("%.3f  \t %.3f \n" %(rmin+(x+1)*dx-dx/2,np.mean(np.array(mo[:,x]*dx))))
        f.close()


os.system('mv tempo %s '%filename2)
os.system('rm tempo')
print("--- %s seconds ---" % (time.time() - start_time))

