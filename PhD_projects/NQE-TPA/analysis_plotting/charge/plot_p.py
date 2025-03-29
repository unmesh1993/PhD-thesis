import numpy as np
import matplotlib 
#matplotlib.use('Agg')
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D # This import has side effects required for the kwarg projection='3d' in the call to fig.add_subplot
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.colors import LogNorm
import numpy as np
import os,math
import sys

res1='DDEC6_even_tempered_net_atomic_charges.xyz'

res2=str(sys.argv[1])
res3=str(sys.argv[2])
os.system('rm del1.xyz')

def anglem(a1,b1,b2,cord,dist1,dist2):
       b1a1=b1-a1
       b2a1=b2-a1
       cosine_angle=np.dot(b1a1,b2a1) / (dist1 * dist2)
       angler=np.arccos(cosine_angle)
       del b1a1,b2a1,cosine_angle
       return angler



index=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63']


x=[]
y=[]
z=[]
z1=[]
z2=[]
for i in range(16):
    for j in range(20):

        try:
           res=res2+str(index[i])+"/dir_"+str(j+1)+'/'+res1
           f=open(res,'r')
           a=f.readlines()
           f.close
        except OSError:
            print ('wow')
            continue
        

        cord=[]
        for j in range (2,362):
            xx=a[j].split()
            cord.append(xx)
        del a
        for k in range(0,180,18):
            a1=np.array(cord[k+6][1:4],float)
            b1=np.array(cord[k+7][1:4],float)
            b2=np.array(cord[k+197][1:4],float)
            dist1=np.linalg.norm(a1-b1)
            dist2=np.linalg.norm(a1-b2)
            dist3=np.linalg.norm(b1-b2)

            x.append(dist2-dist1)           
            y.append(dist3)           
            z.append(cord[k+6][4])           
            z1.append(cord[k+7][4])           
            z2.append(cord[k+197][4])           
    
            a1=np.array(cord[k+15][1:4],float)
            b1=np.array(cord[k+16][1:4],float)
            b2=np.array(cord[k+188][1:4],float)
            dist1=np.linalg.norm(a1-b1)
            dist2=np.linalg.norm(a1-b2)
            dist3=np.linalg.norm(b1-b2)

            x.append(dist2-dist1)
            y.append(dist3)           
            z.append(cord[k+15][4])
            z1.append(cord[k+16][4])           
            z2.append(cord[k+188][4])           
    
        for k in range(180,360,18):
            a1=np.array(cord[k+15][1:4],float)
            b1=np.array(cord[k+16][1:4],float)
            b2=np.array(cord[k-180+8][1:4],float)
            dist1=np.linalg.norm(a1-b1)
            dist2=np.linalg.norm(a1-b2)
            dist3=np.linalg.norm(b1-b2)
    
            x.append(dist2-dist1)
            y.append(dist3)           
            z.append(cord[k+15][4])      
            z1.append(cord[k+16][4])           
            z2.append(cord[k-180+8][4])           
    
            a1=np.array(cord[k+6][1:4],float)
            b1=np.array(cord[k+7][1:4],float)
            b2=np.array(cord[k-180+17][1:4],float)
            dist1=np.linalg.norm(a1-b1)
            dist2=np.linalg.norm(a1-b2)
            dist3=np.linalg.norm(b1-b2)

            x.append(dist2-dist1)
            y.append(dist3)           
            z.append(cord[k+6][4])              
            z1.append(cord[k+7][4])           
            z2.append(cord[k-180+17][4])           
    



x=np.array(x,float)
x=-x
y=np.array(y,float)
z=np.array(z,float)
z1=np.array(z1,float)
z2=np.array(z2,float)

print (np.amin(z),np.amax(z))
print (np.amin(z1),np.amax(z1))
print (np.amin(z2),np.amax(z2))
fig=plt.figure()


fig=plt.figure()
ax = fig.add_subplot(221)
plt.scatter(x,z, s=1);
plt.xlabel(r'$\delta_o $ (Å)',size=12)
plt.ylabel(r'DDEC charge on H',size=12)
plt.xticks(np.arange(-2.0,2.0,0.5),size=12)
plt.yticks(np.arange(0.20,0.50,0.05),size=12)
plt.ylim(0.26,0.46)
plt.xlim(-1.4,1.4)

plt.grid()
'''
ax = fig.add_subplot(223)
plt.scatter(x,z1,color='green', s=1,label='O(M1)')
plt.scatter(x,z2,color='brown', s=1,label='O(M2)')
plt.xlabel(r'$\delta_o $ (Å)',size=12)
plt.ylabel('DDEC charge on O',size=12)
plt.xticks(np.arange(-2.0,2.0,0.5),size=12)
plt.yticks(size=12)
plt.xlim(-1.4,1.4)
plt.ylim(-0.35,-0.65)
#plt.legend(prop={'size': 6},loc=9, bbox_to_anchor=(0.6,0.7))
plt.legend(prop={'size': 6},loc=0)
#ax.yaxis.set_ticklabels(np.arange(-0.30,-0.70,0.05))
plt.grid()
'''
plt.subplots_adjust(hspace=0.0,wspace=0.0)
plt.savefig(res3, dpi=500, bbox_inches = 'tight',    pad_inches = 0.1)
plt.savefig('photo.pdf')
