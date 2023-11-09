import numpy as np
import os
import math
import time
import sys

res=str(sys.argv[1])
filename2=str(sys.argv[2])
filename4=str(sys.argv[3])
filename6=str(sys.argv[4])
os.system('rm tempo')
os.system('rm tempo2')
os.system('rm tempo3')
filename='tempo'
filename3='tempo2'
filename5='tempo3'


def anglem(za1,zb1):
       l1=zb1-za1
       l2=np.array([0,0,1])
       dist1=np.linalg.norm(l1)
       dist2=np.linalg.norm(l2)
       cosine_angle=np.dot(l1,l2) / (dist1 * dist2)
       return cosine_angle


def anglem2(za1,zb1,zb2):
       l1=zb1-za1
       l2=zb2-za1
       dist1=np.linalg.norm(l1)
       dist2=np.linalg.norm(l2)
       cosine_angle=np.dot(l1,l2) / (dist1 * dist2)
       angler=np.arccos(cosine_angle)
       angler2=np.degrees(angler)
       return angler2


#index_O,cord-O_d,dist-OH,cord-H,dist-O_dO_a,cord-O_a,index-O_a
# def donor(j,a1,z1,ss1,hhh2,hhh4,index1)

def donor(j,a1,zz,sss,hhh2,hhh4,index1):
       k=np.argsort(hhh2)
       lll1=[]
       fff1=[]
       www1=[]
       www2=[]
       for i in range(1,20):
           vvv=np.linalg.norm(sss-hhh4[k[i]])

           www1.append(vvv)
           www2.append(hhh2[k[i]])

           lll1.append(hhh4[k[i]])
           fff1.append(index1[k[i]])

       www1=np.array(www1,float)
       www2=np.array(www2,float)
       lll1=np.array(lll1,float)
       fff1=np.array(fff1,int)

       dist1=zz
       dist2=np.amin(www1)
       dist3=www2[np.argmin(www1)]
       fff2=lll1[np.argmin(www1)]
       angle=anglem2(sss,a1,fff2)
       ind=fff1[np.argmin(www1)]

       
       f=open(filename3,'a')
       f.write("%.3f  \t %.3f  \t %.3f \t  %.3f \t  %.3f \t  %i \t  %i \n" %(a1[2],dist1,dist2,dist3,angle,j,ind))
       f.close()
       return

cutoff=1.32
atoms=1692
hyd=28

f=open(res,'r')
aa=f.readlines()
f.close

vec1=np.array([[19.4,0.0,0.0],[0.0,19.2,0.0],[0.0,0.0,70]],float)
ivec1=np.linalg.inv(vec1)
    
frames=int(len(aa)/(atoms+2))
for i in range(frames):
       print (i)
       cord=[]

       for j in range(1664+2-56,1664+2):
          t1=aa[j+(i)*(atoms+2)].split()
          cord.append(t1[3])

       cord=np.array(cord,float)
       mean=np.mean(cord)
       del cord

       coord=[]
       for j in range(2,1442):
          t1=aa[j+(i)*(atoms+2)].split()
          t2=np.array(t1[1:],float)
          t2[2]=t2[2]-mean
          coord.append(t2)

       cord=np.array(coord,float)

       coord=[] 
       for j in range(atoms+2-hyd,atoms+2):
          t1=aa[j+(i)*(atoms+2)].split()
          t2=np.array(t1[1:],float)
          t2[2]=t2[2]-mean
          coord.append(t2)

       ccord=np.array(coord,float)
       


       for j in range(0,1440,3):

           sam=np.array(cord[j],float)
           a1=sam

           hhh1=np.zeros(480*2+hyd,float) 
           hhh2=np.zeros(480,float) 
           hhh3=np.zeros(((480*2+hyd),3),float)
           hhh4=np.zeros((480,3),float)
           index1=np.zeros(480,int)
           counter2=0
           counter3=0

           for t in range(0,1440,3):
               sam=np.array(cord[t+1],float)
               b1=sam

               sam=np.array(cord[t+2],float)
               b2=sam

               sam=np.array(cord[t],float)
               c1=sam


               nnn1=np.zeros(9,float)
               nnn2=np.zeros(9,float)
               nnn3=np.zeros(9,float)
               nnn4=np.zeros((9,3),float)
               nnn5=np.zeros((9,3),float)
               nnn6=np.zeros((9,3),float)
               counter1=0

               for k1 in range(-1,2):
                   for k2 in range(-1,2):

                      bb1=np.array(b1+k1*vec1[0,:]+k2*vec1[1,:],float)
                      h1=np.linalg.norm(bb1-a1)

                      nnn1[counter1]=h1
                      nnn4[counter1]=bb1

                      bb2=np.array(b2+k1*vec1[0,:]+k2*vec1[1,:],float)
                      h2=np.linalg.norm(bb2-a1)

                      nnn2[counter1]=h2
                      nnn5[counter1]=bb2

                      bb3=np.array(c1+k1*vec1[0,:]+k2*vec1[1,:],float)
                      h3=np.linalg.norm(bb3-a1)

                      nnn3[counter1]=h3
                      nnn6[counter1]=bb3

                      counter1=counter1+1

               kkk1=np.amin(nnn1)
               kkk2=np.amin(nnn2)
               kkk3=np.amin(nnn3)

               kkk4=nnn4[np.argmin(nnn1)] 
               kkk5=nnn5[np.argmin(nnn2)] 
               kkk6=nnn6[np.argmin(nnn3)]

               
               hhh1[counter2]=kkk1
               hhh3[counter2]=kkk4
               counter2=counter2+1
               hhh1[counter2]=kkk2
               hhh3[counter2]=kkk5
               counter2=counter2+1
 
               hhh2[counter3]=kkk3
               hhh4[counter3]=kkk6
               index1[counter3]=t
               counter3=counter3+1



           for t in range(0,hyd):
               sam=np.array(ccord[t],float)
               b1=sam

               nnn1=np.zeros(9,float)
               nnn4=np.zeros((9,3),float)
               counter1=0

               for k1 in range(-1,2):
                   for k2 in range(-1,2):

                      bb1=np.array(b1+k1*vec1[0,:]+k2*vec1[1,:],float)
                      h1=np.linalg.norm(bb1-a1)

                      nnn1[counter1]=h1
                      nnn4[counter1]=bb1

                      counter1=counter1+1

               kkk1=np.amin(nnn1)
               kkk4=nnn4[np.argmin(nnn1)] 

               
               hhh1[counter2]=kkk1
               hhh3[counter2]=kkk4
               counter2=counter2+1
 

           add=0
           for t in range(480*2+hyd):
               num = 1 - (hhh1[t]/cutoff)**16
               den = 1 - (hhh1[t]/cutoff)**56
               add = add + num/den

           cnn=add

           z1=np.amin(hhh1)
           ss1=hhh3[np.argmin(hhh1)]
           hhh1[hhh1 == np.amin(hhh1)]=50000

           angle1=anglem(a1,ss1)

           z2=np.amin(hhh1)
           ss2=hhh3[np.argmin(hhh1)]
           hhh1[hhh1 == np.amin(hhh1)]=50000

           angle2=anglem(a1,ss2)

           z3=np.amin(hhh1)
           ss3=hhh3[np.argmin(hhh1)]
           hhh1[hhh1 == np.amin(hhh1)]=50000

           angle3=anglem(a1,ss3)

           z4=np.amin(hhh1)
           ss4=hhh3[np.argmin(hhh1)]
           hhh1[hhh1 == np.amin(hhh1)]=50000

           angle4=anglem(a1,ss4)


#           aangle1=anglem2(a1,ss1,ss2)
#           aangle2=anglem2(a1,ss1,ss3)
#           aangle3=anglem2(a1,ss1,ss4)
#           aangle4=anglem2(a1,ss2,ss3)
#           aangle5=anglem2(a1,ss2,ss4)
#           aangle6=anglem2(a1,ss3,ss4)


           f=open(filename,'a')
           f.write("%.3f  \t %.3f  \t %.3f \t  %.3f \t  %.3f \t  %.3f \t  %.3f \t  %.3f \t  %.3f  \t %.3f \n" %(a1[2],z1,z2,z3,z4,angle1,angle2,angle3,angle4,cnn))
           f.close()

#           f=open(filename5,'a')
#           f.write("%.3f  \t %.3f  \t %.3f \t  %.3f \t  %.3f \t  %.3f \t  %.3f  \n" %(a1[2],aangle1,aangle2,aangle3,aangle4,aangle5,aangle6))
#           f.close()

           #index_O,cord-O_d,dist-OH,cord-H,dist-O_dO_a,cord-O_a,index-O_a
#           donor(j,a1,z1,ss1,hhh2,hhh4,index1)
#           donor(j,a1,z2,ss2,hhh2,hhh4,index1)
#           donor(j,a1,z3,ss3,hhh2,hhh4,index1)
#           donor(j,a1,z4,ss4,hhh2,hhh4,index1)

os.system('mv tempo %s '%filename2)
os.system('rm tempo')
os.system('mv tempo2 %s '%filename4)
os.system('rm tempo2')
os.system('mv tempo3 %s '%filename6)
os.system('rm tempo3')
