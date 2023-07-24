import numpy as np
import os,math,sys


vec=np.array([[19.249512304830585,0.0000000000000000,0.0000000000000000],[-11.556225312311822,9.8917278299989544,0.0000000000000000],[-4.7100804271264112,2.2710568232788395,17.344417844316347]],float)

#print (vec[0])
#print (vec[1])
#print (vec[2])

res1=str(sys.argv[1])

f=open(res1,'r')
a=f.readlines()
f.close

def proj(a,b):
    k=(np.dot(b,a)*b)/(np.linalg.norm(b))**2
    return k
    
    


frames=int(len(a)/983)
 
elxx=np.zeros(frames,float)
elxy=np.zeros(frames,float)
elxz=np.zeros(frames,float)
elyx=np.zeros(frames,float)
elyy=np.zeros(frames,float)
elyz=np.zeros(frames,float)
elzx=np.zeros(frames,float)
elzy=np.zeros(frames,float)
elzz=np.zeros(frames,float)

elx=np.zeros((frames,3),float)
ely=np.zeros((frames,3),float)
elz=np.zeros((frames,3),float)

for i in range (frames):

        t=982+i*983  #berry
#        t=981+i*983  #wann
        x=a[t].split()
        x=np.array(x[:3],float)
        x=x*3.33564095*10**(-30)

        vx=proj(x,vec[0])
        vy=proj(x,vec[1])
        vz=proj(x,vec[2])
         
        elxx[i]=np.dot(vx,vx)          
        elxy[i]=np.dot(vx,vy)          
        elxz[i]=np.dot(vx,vz)          
        elyx[i]=np.dot(vy,vx)          
        elyy[i]=np.dot(vy,vy)          
        elyz[i]=np.dot(vy,vz)          
        elzx[i]=np.dot(vz,vx)          
        elzy[i]=np.dot(vz,vy)          
        elzz[i]=np.dot(vz,vz)          

        elx[i]=vx
        ely[i]=vy
        elz[i]=vz

temp=70
vol=3302.567*10**(-30)
conv=1
conv1=(8.85418782*10**(-12))

dxx=(1 + (np.mean(elxx)-np.dot(np.mean(elx,axis=0),np.mean(elx,axis=0)))*(4*math.pi)*(1/(3*vol*1.38064852*10**(-23)*temp)))
dxy=(1 + (np.mean(elxy)-np.dot(np.mean(elx,axis=0),np.mean(ely,axis=0)))*(4*math.pi)*(1/(3*vol*1.38064852*10**(-23)*temp)))
dxz=(1 + (np.mean(elxz)-np.dot(np.mean(elx,axis=0),np.mean(elz,axis=0)))*(4*math.pi)*(1/(3*vol*1.38064852*10**(-23)*temp)))
dyx=(1 + (np.mean(elyx)-np.dot(np.mean(ely,axis=0),np.mean(elx,axis=0)))*(4*math.pi)*(1/(3*vol*1.38064852*10**(-23)*temp)))
dyy=(1 + (np.mean(elyy)-np.dot(np.mean(ely,axis=0),np.mean(ely,axis=0)))*(4*math.pi)*(1/(3*vol*1.38064852*10**(-23)*temp)))
dyz=(1 + (np.mean(elyz)-np.dot(np.mean(ely,axis=0),np.mean(elz,axis=0)))*(4*math.pi)*(1/(3*vol*1.38064852*10**(-23)*temp)))
dzx=(1 + (np.mean(elzx)-np.dot(np.mean(elz,axis=0),np.mean(elx,axis=0)))*(4*math.pi)*(1/(3*vol*1.38064852*10**(-23)*temp)))
dzy=(1 + (np.mean(elzy)-np.dot(np.mean(elz,axis=0),np.mean(ely,axis=0)))*(4*math.pi)*(1/(3*vol*1.38064852*10**(-23)*temp)))
dzz=(1 + (np.mean(elzz)-np.dot(np.mean(elz,axis=0),np.mean(elz,axis=0)))*(4*math.pi)*(1/(3*vol*1.38064852*10**(-23)*temp)))

DP=np.zeros((3,3),float)
DP[0,0],DP[0,1],DP[0,2],DP[1,0],DP[1,1],DP[1,2],DP[2,0],DP[2,1],DP[2,2]=dxx,dxy,dxz,dyx,dyy,dyz,dzx,dzy,dzz

print ((np.trace(DP)))

print (dxx,dxy,dxz)
print (dyx,dyy,dyz)
print (dzx,dzy,dzz)
