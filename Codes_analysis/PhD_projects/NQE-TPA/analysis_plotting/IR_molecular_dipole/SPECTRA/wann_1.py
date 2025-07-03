import numpy as np
import os,math,sys
import time

os.system('rm del1')
#filename="output.txt"

vec=np.array([[19.249512304830585,0.0000000000000000,0.0000000000000000],[-11.556225312311822,9.8917278299989544,0.0000000000000000],[-4.7100804271264112,2.2710568232788395,17.344417844316347]],float)
start_time = time.time()
res1=str(sys.argv[1])
res2=str(sys.argv[2])

f=open(res1,'r')
a=f.readlines()
f.close


frames=int(len(a)/982)
 
for i in range (frames):


        cord=np.zeros((980,3),float)
        for j in range (2,982):
            t=j+i*982
            x=a[t].split()
            x=np.array(x[1:4],float)
            cord[j-2][:]=x[:]
        
        del t


        cord=np.array(cord,float)
        mo1=np.zeros((40),float)
        mo2=np.zeros((40),float)
        mo3=np.zeros((40),float)
        iii=0

        for k in range(0,180,18):
            a1=np.array(cord[k+6][:],float)
            b1=np.array(cord[k+7][:],float)
            b2=np.array(cord[k+197][:],float)
            dis1=np.linalg.norm(a1-b1)
            dis2=np.linalg.norm(a1-b2)

    
            aa1=np.array(cord[k+15][:],float)
            bb1=np.array(cord[k+16][:],float)
            bb2=np.array(cord[k+188][:],float)
            ddis1=np.linalg.norm(aa1-bb1)
            ddis2=np.linalg.norm(aa1-bb2)

              
            dist1=[]
            dist2=[]
            dist3=[]
            dist4=[]

            for ds in range(360,980): 
               x=np.array(cord[ds][:],float)

               dog1=np.linalg.norm(b1-x)
               dist1.append(dog1)
               dog1=np.linalg.norm(b2-x)
               dist2.append(dog1)

               dog1=np.linalg.norm(bb1-x)
               dist3.append(dog1)
               dog1=np.linalg.norm(bb2-x)
               dist4.append(dog1)

           
            dist1=np.array(dist1,float)
            dist2=np.array(dist2,float)
            dist3=np.array(dist3,float)
            dist4=np.array(dist4,float)

            
            mo2[iii]=dis2-dis1         
            mo2[iii+1]=ddis2-ddis1         

    
            kik1=[]
            kik2=[]
            kik3=[]
            kik4=[]
            for ds in range(4):
                q=np.argmin(dist1)+360
                kik1.append(q)
                dist1[np.argmin(dist1)]=50
                q=np.argmin(dist2)+360
                kik2.append(q)
                dist2[np.argmin(dist2)]=50

                q=np.argmin(dist3)+360
                kik3.append(q)
                dist3[np.argmin(dist3)]=50
                q=np.argmin(dist4)+360
                kik4.append(q)
                dist4[np.argmin(dist4)]=50

            kik1=np.array(kik1,int)
            kik2=np.array(kik2,int)
            kik3=np.array(kik3,int)
            kik4=np.array(kik4,int)

            dist5=[]
            dist6=[]
            dist7=[]
            dist8=[]

            dist1=[]
            dist2=[]
            dist3=[]
            dist4=[]
            for ds in range(4):
                bull=np.array(cord[kik1[ds]][:],float)
                dog1=np.linalg.norm(a1-bull)
                dog2=np.linalg.norm(b1-bull)
                dist5.append(dog1)
                dist1.append(dog2)

                bull=np.array(cord[kik2[ds]][:],float)
                dog1=np.linalg.norm(a1-bull)
                dog2=np.linalg.norm(b2-bull)
                dist6.append(dog1)
                dist2.append(dog2)

                bull=np.array(cord[kik3[ds]][:],float)
                dog1=np.linalg.norm(aa1-bull)
                dog2=np.linalg.norm(bb1-bull)
                dist7.append(dog1)
                dist3.append(dog2)

                bull=np.array(cord[kik4[ds]][:],float)
                dog1=np.linalg.norm(aa1-bull)
                dog2=np.linalg.norm(bb2-bull)
                dist8.append(dog1)
                dist4.append(dog2)

            mo1[iii]=dist1[np.argmin(dist5)] 
            mo1[iii+1]=dist3[np.argmin(dist7)]
 
            mo3[iii]=dist2[np.argmin(dist6)]
            mo3[iii+1]=dist4[np.argmin(dist8)] 
            iii=iii+2

        for k in range(180,360,18):
            a1=np.array(cord[k+15][:],float)
            b1=np.array(cord[k+16][:],float)
            b2=np.array(cord[k-180+8][:],float)
            dis1=np.linalg.norm(a1-b1)
            dis2=np.linalg.norm(a1-b2)

    
            aa1=np.array(cord[k+6][:],float)
            bb1=np.array(cord[k+7][:],float)
            bb2=np.array(cord[k-180+17][:],float)
            ddis1=np.linalg.norm(aa1-bb1)
            ddis2=np.linalg.norm(aa1-bb2)

            dist1=[]
            dist2=[]
            dist3=[]
            dist4=[]

            for ds in range(360,980): 
               x=np.array(cord[ds][:],float)

               dog1=np.linalg.norm(b1-x)
               dist1.append(dog1)
               dog1=np.linalg.norm(b2-x)
               dist2.append(dog1)

               dog1=np.linalg.norm(bb1-x)
               dist3.append(dog1)
               dog1=np.linalg.norm(bb2-x)
               dist4.append(dog1)

           
            dist1=np.array(dist1,float)
            dist2=np.array(dist2,float)
            dist3=np.array(dist3,float)
            dist4=np.array(dist4,float)

            
            mo2[iii]=dis2-dis1         
            mo2[iii+1]=ddis2-ddis1         

    
            kik1=[]
            kik2=[]
            kik3=[]
            kik4=[]
            for ds in range(4):
                q=np.argmin(dist1)+360
                kik1.append(q)
                dist1[np.argmin(dist1)]=50
                q=np.argmin(dist2)+360
                kik2.append(q)
                dist2[np.argmin(dist2)]=50

                q=np.argmin(dist3)+360
                kik3.append(q)
                dist3[np.argmin(dist3)]=50
                q=np.argmin(dist4)+360
                kik4.append(q)
                dist4[np.argmin(dist4)]=50

            kik1=np.array(kik1,int)
            kik2=np.array(kik2,int)
            kik3=np.array(kik3,int)
            kik4=np.array(kik4,int)

            dist5=[]
            dist6=[]
            dist7=[]
            dist8=[]

            dist1=[]
            dist2=[]
            dist3=[]
            dist4=[]
            for ds in range(4):
                bull=np.array(cord[kik1[ds]][:],float)
                dog1=np.linalg.norm(a1-bull)
                dog2=np.linalg.norm(b1-bull)
                dist5.append(dog1)
                dist1.append(dog2)

                bull=np.array(cord[kik2[ds]][:],float)
                dog1=np.linalg.norm(a1-bull)
                dog2=np.linalg.norm(b2-bull)
                dist6.append(dog1)
                dist2.append(dog2)

                bull=np.array(cord[kik3[ds]][:],float)
                dog1=np.linalg.norm(aa1-bull)
                dog2=np.linalg.norm(bb1-bull)
                dist7.append(dog1)
                dist3.append(dog2)

                bull=np.array(cord[kik4[ds]][:],float)
                dog1=np.linalg.norm(aa1-bull)
                dog2=np.linalg.norm(bb2-bull)
                dist8.append(dog1)
                dist4.append(dog2)

            mo1[iii]=dist1[np.argmin(dist5)] 
            mo1[iii+1]=dist3[np.argmin(dist7)]
 
            mo3[iii]=dist2[np.argmin(dist6)]
            mo3[iii+1]=dist4[np.argmin(dist8)] 
            iii=iii+2
              


        for ds in range(40):
             f=open(res2,'a')
             f.write("%.6f  \t %.6f   \t  %.6f   \t  %.6f \n" %(i,mo2[ds],mo1[ds],mo3[ds]))
             f.close()
        
#             print (mo2[ds],mo1[ds],mo3[ds])


#os.system('mv output.txt prop_wan_1.dat')    
#########################################################################
                   
print("--- %s seconds ---" % (time.time() - start_time))   
