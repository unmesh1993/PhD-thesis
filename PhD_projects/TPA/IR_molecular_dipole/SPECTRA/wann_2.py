import numpy as np
import os,math,sys
import time

os.system('rm del1')
#filename="output.txt"

vec1=np.array([[19.249512304830585,0.0000000000000000,0.0000000000000000],[-11.556225312311822,9.8917278299989544,0.0000000000000000],[-4.7100804271264112,2.2710568232788395,17.344417844316347]],float)
start_time = time.time()
res1=str(sys.argv[1])
res2=str(sys.argv[2])

f=open(res1,'r')
a=f.readlines()
f.close


frames=int(len(a)/982)
 
for i in range (frames):

        print (i)

        cord=np.zeros((980,3),float)
        for j in range (2,982):
            t=j+i*982
            x=a[t].split()
            x=np.array(x[1:4],float)
            cord[j-2][:]=x
        
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

               kdist1=[]
               kdist2=[]
               kdist3=[]
               kdist4=[]
    
               for k1 in range(-1,2):
                   for k2 in range(-1,2):
                      for k3 in range(-1,2):

                          xb1=np.array(b1+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog1=np.linalg.norm(xb1-x)
                          kdist1.append(dog1)

                          xb2=np.array(b2+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog2=np.linalg.norm(xb2-x)
                          kdist2.append(dog2)


                          xb3=np.array(bb1+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog3=np.linalg.norm(xb3-x)
                          kdist3.append(dog3)

                          xb4=np.array(bb2+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog4=np.linalg.norm(xb4-x)
                          kdist4.append(dog4)

               kdist1=np.array(kdist1,float)
               kdist2=np.array(kdist2,float)
               kdist3=np.array(kdist3,float)
               kdist4=np.array(kdist4,float)
               
               dist1.append(np.amin(kdist1))
               dist2.append(np.amin(kdist2))
               dist3.append(np.amin(kdist3))
               dist4.append(np.amin(kdist4))

           
            dist1=np.array(dist1,float)
            dist2=np.array(dist2,float)
            dist3=np.array(dist3,float)
            dist4=np.array(dist4,float)

            
            mo1[iii]=dis2-dis1         
            mo1[iii+1]=ddis2-ddis1         


            
            ik1=np.argsort(dist1)
            ik2=np.argsort(dist2)
            ik3=np.argsort(dist3)
            ik4=np.argsort(dist4)

             
            dist1=[]
            dist2=[]
            dist3=[]
            dist4=[]

            for ds in range(0,4):
               sop1=cord[ik1[ds]+360,:]
               sop2=cord[ik2[ds]+360,:]
               sop3=cord[ik3[ds]+360,:]
               sop4=cord[ik4[ds]+360,:]

               kdist1=[]
               kdist2=[]
               kdist3=[]
               kdist4=[]


               for k1 in range(-1,2):
                   for k2 in range(-1,2):
                      for k3 in range(-1,2):

                          xb1=np.array(sop1+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog1=np.linalg.norm(xb1-a1)
                          kdist1.append(dog1)

                          xb2=np.array(sop2+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog2=np.linalg.norm(xb2-a1)
                          kdist2.append(dog2)

                          xb3=np.array(sop3+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog3=np.linalg.norm(xb3-aa1)
                          kdist3.append(dog3)

                          xb4=np.array(sop4+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog4=np.linalg.norm(xb4-aa1)
                          kdist4.append(dog4)

               kdist1=np.array(kdist1,float)
               kdist2=np.array(kdist2,float)
               kdist3=np.array(kdist3,float)
               kdist4=np.array(kdist4,float)

               dist1.append(np.amin(kdist1))
               dist2.append(np.amin(kdist2))
               dist3.append(np.amin(kdist3))
               dist4.append(np.amin(kdist4))

            dist1=np.array(dist1,float)
            dist2=np.array(dist2,float)
            dist3=np.array(dist3,float)
            dist4=np.array(dist4,float)
            print (np.sort(dist1)[0:4])
            print (np.sort(dist2)[0:4])
            print (np.sort(dist3)[0:4])
            print (np.sort(dist4)[0:4])



            mo2[iii]=np.amin(dist1)
            mo2[iii+1]=np.amin(dist3)

            mo3[iii]=np.amin(dist2)
            mo3[iii+1]=np.amin(dist4)
 
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

               kdist1=[]
               kdist2=[]
               kdist3=[]
               kdist4=[]
    
               for k1 in range(-1,2):
                   for k2 in range(-1,2):
                      for k3 in range(-1,2):

                          xb1=np.array(b1+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog1=np.linalg.norm(xb1-x)
                          kdist1.append(dog1)

                          xb2=np.array(b2+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog2=np.linalg.norm(xb2-x)
                          kdist2.append(dog2)


                          xb3=np.array(bb1+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog3=np.linalg.norm(xb3-x)
                          kdist3.append(dog3)

                          xb4=np.array(bb2+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog4=np.linalg.norm(xb4-x)
                          kdist4.append(dog4)

               kdist1=np.array(kdist1,float)
               kdist2=np.array(kdist2,float)
               kdist3=np.array(kdist3,float)
               kdist4=np.array(kdist4,float)
               
               dist1.append(np.amin(kdist1))
               dist2.append(np.amin(kdist2))
               dist3.append(np.amin(kdist3))
               dist4.append(np.amin(kdist4))

           
            dist1=np.array(dist1,float)
            dist2=np.array(dist2,float)
            dist3=np.array(dist3,float)
            dist4=np.array(dist4,float)

            
            mo1[iii]=dis2-dis1         
            mo1[iii+1]=ddis2-ddis1         


            
            ik1=np.argsort(dist1)
            ik2=np.argsort(dist2)
            ik3=np.argsort(dist3)
            ik4=np.argsort(dist4)

             
            dist1=[]
            dist2=[]
            dist3=[]
            dist4=[]

            for ds in range(0,4):
               sop1=cord[ik1[ds]+360,:]
               sop2=cord[ik2[ds]+360,:]
               sop3=cord[ik3[ds]+360,:]
               sop4=cord[ik4[ds]+360,:]

               kdist1=[]
               kdist2=[]
               kdist3=[]
               kdist4=[]


               for k1 in range(-1,2):
                   for k2 in range(-1,2):
                      for k3 in range(-1,2):

                          xb1=np.array(sop1+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog1=np.linalg.norm(xb1-a1)
                          kdist1.append(dog1)

                          xb2=np.array(sop2+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog2=np.linalg.norm(xb2-a1)
                          kdist2.append(dog2)

                          xb3=np.array(sop3+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog3=np.linalg.norm(xb3-aa1)
                          kdist3.append(dog3)

                          xb4=np.array(sop4+k1*vec1[0,:]+k2*vec1[1,:]+k3*vec1[2,:],float)
                          dog4=np.linalg.norm(xb4-aa1)
                          kdist4.append(dog4)

               kdist1=np.array(kdist1,float)
               kdist2=np.array(kdist2,float)
               kdist3=np.array(kdist3,float)
               kdist4=np.array(kdist4,float)

               dist1.append(np.amin(kdist1))
               dist2.append(np.amin(kdist2))
               dist3.append(np.amin(kdist3))
               dist4.append(np.amin(kdist4))

            dist1=np.array(dist1,float)
            dist2=np.array(dist2,float)
            dist3=np.array(dist3,float)
            dist4=np.array(dist4,float)
            print (np.sort(dist1)[0:4])
            print (np.sort(dist2)[0:4])
            print (np.sort(dist3)[0:4])
            print (np.sort(dist4)[0:4])



            mo2[iii]=np.amin(dist1)
            mo2[iii+1]=np.amin(dist3)

            mo3[iii]=np.amin(dist2)
            mo3[iii+1]=np.amin(dist4)
 
            iii=iii+2
             


        for ds in range(40):
             f=open(res2,'a')
             f.write("%.3f  \t %.3f   \t  %.3f   \t  %.3f \n" %(i,mo1[ds],mo2[ds],mo3[ds]))
             f.close()
        
#             print (mo2[ds],mo1[ds],mo3[ds])


#os.system('mv output.txt prop_wan_1.dat')    
#########################################################################
                   
print("--- %s seconds ---" % (time.time() - start_time))   
