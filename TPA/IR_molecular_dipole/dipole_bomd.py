import numpy as np
import os,math,sys

ind=np.array(['C' ,'C' ,'C' ,'C' ,'H' ,'H' ,'H' ,'O' ,'O' ,'C' ,'C' ,'C' ,'C' ,'H' ,'H' ,'H' ,'O' ,'O'],str)
index=np.array([4,4,4,4,1,1,1,6,6,4,4,4,4,1,1,1,6,6],float)

vec=np.array([[19.249512304830585,0.0000000000000000,0.0000000000000000],[-11.556225312311822,9.8917278299989544,0.0000000000000000],[-4.7100804271264112,2.2710568232788395,17.344417844316347]],float)

res1=str(sys.argv[1])
res2=str(sys.argv[2])
#res3=str(sys.argv[3])
#res4=str(sys.argv[4])

f=open(res1,'r')
a=f.readlines()
f.close
#f=open(res3,'r')
#a2=f.readlines()
#f.close
#f=open(res4,'r')
#a3=f.readlines()
#f.close


frames=int(len(a)/982)

for i in range (frames):
        f=open(res2,'a')
        f.write("%i \n" %(20))
        f.write("%s  \t %i  \n" %('f=',i))
        f.close()
#        f.write("%s  \t %.6f  \t %.6f  \t %.6f  \n" %('X',np.float(a2[9+i*10].split()[1]),np.float(a2[9+i*10].split()[3]),np.float(a2[9+i*10].split()[5])))
#        f.write("%s  \t %.6f  \t %.6f  \t %.6f  \n" %('X',np.float(a3[0+i*1].split()[4]),np.float(a3[0+i*1].split()[5]),np.float(a3[0+i*1].split()[6])))

        cord=np.zeros((980,3),float)
        for j in range (2,982):
            t=j+i*982
            x=a[t].split()
            x=np.array(x[1:4],float)
            cord[j-2][:]=x[:]

        del t


###molecule in thesystem

        for j in range(0,360,18):
#        for j in range(180,196,18):


            mol=np.zeros((18+31,3),float)
            mol[0]=np.array(cord[j][:],float)


            for l in range(1,18):
                t=j+l

                a2=np.zeros((27,3),float)
                h=np.zeros((27),float)
                tt=0


                for k1 in range(-1,2):
                    for k2 in range(-1,2):
                        for k3 in range(-1,2):

                            a2[tt]=np.array(cord[t][:]+k1*vec[0][:]+k2*vec[1][:]+k3*vec[2][:],float)
                            h[tt]=np.linalg.norm(a2[tt]-mol[0])
                            tt=tt+1

                mol[l]=a2[np.argmin(h)]
####H involved in tunneling
#
#            for l in [6,15]:
#
#                if j < 180:
#                   t=j+l+180
#                elif j >=180:
#                   t=j+l-180
#
#                a2=np.zeros((27,3),float)
#                h=np.zeros((27),float)
#                tt=0
#
#
#                for k1 in range(-1,2):
#                    for k2 in range(-1,2):
#                        for k3 in range(-1,2):
#
#                            a2[tt]=np.array(cord[t][:]+k1*vec[0][:]+k2*vec[1][:]+k3*vec[2][:],float)
#                            h[tt]=np.linalg.norm(a2[tt]-mol[0])
#                            tt=tt+1
#
#
#                if l==6 and np.linalg.norm(mol[15]-mol[16]) > np.linalg.norm(a2[np.argmin(h)]-mol[17]):
#                      mol[15]=a2[np.argmin(h)]
#                if l==15 and np.linalg.norm(mol[6]-mol[7])  > np.linalg.norm(a2[np.argmin(h)]-mol[8]):
#                      mol[6]=a2[np.argmin(h)]
#
#

###Wannier center


            aa1=(mol[0]+mol[1]+mol[2]+mol[9]+mol[10]+mol[11])/6
            aa3=np.zeros((620,3),float)
            ahh=np.zeros((620),float)

            ba1=(mol[7])
            ba3=np.zeros((620,3),float)
            bhh=np.zeros((620),float)
            ca1=(mol[8])
            ca3=np.zeros((620,3),float)
            chh=np.zeros((620),float)
            da1=(mol[16])
            da3=np.zeros((620,3),float)
            dhh=np.zeros((620),float)
            ea1=(mol[17])
            ea3=np.zeros((620,3),float)
            ehh=np.zeros((620),float)
            for l in range(360,980):

                t=l

                aa2=np.zeros((27,3),float)
                ah=np.zeros((27),float)
                att=0

                ba2=np.zeros((27,3),float)
                bh=np.zeros((27),float)
                btt=0

                ca2=np.zeros((27,3),float)
                ch=np.zeros((27),float)
                ctt=0


                da2=np.zeros((27,3),float)
                dh=np.zeros((27),float)
                dtt=0

                ea2=np.zeros((27,3),float)
                eh=np.zeros((27),float)
                ett=0


                for k1 in range(-1,2):
                    for k2 in range(-1,2):
                        for k3 in range(-1,2):

                            aa2[att]=np.array(cord[t][:]+k1*vec[0][:]+k2*vec[1][:]+k3*vec[2][:],float)
                            ah[att]=np.linalg.norm(aa2[att]-aa1)
                            att=att+1
                            ba2[btt]=np.array(cord[t][:]+k1*vec[0][:]+k2*vec[1][:]+k3*vec[2][:],float)
                            bh[btt]=np.linalg.norm(ba2[btt]-ba1)
                            btt=btt+1
                            ca2[ctt]=np.array(cord[t][:]+k1*vec[0][:]+k2*vec[1][:]+k3*vec[2][:],float)
                            ch[ctt]=np.linalg.norm(ca2[ctt]-ca1)
                            ctt=ctt+1
                            da2[dtt]=np.array(cord[t][:]+k1*vec[0][:]+k2*vec[1][:]+k3*vec[2][:],float)
                            dh[dtt]=np.linalg.norm(da2[dtt]-da1)
                            dtt=dtt+1
                            ea2[ett]=np.array(cord[t][:]+k1*vec[0][:]+k2*vec[1][:]+k3*vec[2][:],float)
                            eh[ett]=np.linalg.norm(ea2[ett]-ea1)
                            ett=ett+1

                aa3[l-360]=aa2[np.argmin(ah)]
                ahh[l-360]=np.linalg.norm(aa3[l-360]-aa1)
                ba3[l-360]=ba2[np.argmin(bh)]
                bhh[l-360]=np.linalg.norm(ba3[l-360]-ba1)
                ca3[l-360]=ca2[np.argmin(ch)]
                chh[l-360]=np.linalg.norm(ca3[l-360]-ca1)
                da3[l-360]=da2[np.argmin(dh)]
                dhh[l-360]=np.linalg.norm(da3[l-360]-da1)
                ea3[l-360]=ea2[np.argmin(eh)]
                ehh[l-360]=np.linalg.norm(ea3[l-360]-ea1)

            for l in range(15):
                mol[l+18]=aa3[np.argmin(ahh)]
                ahh[np.argmin(ahh)]=100
            for l in range(4):
                mol[l+18+15]=ba3[np.argmin(bhh)]
                bhh[np.argmin(bhh)]=100
            for l in range(4):
                mol[l+18+19]=ca3[np.argmin(chh)]
                chh[np.argmin(chh)]=100
            for l in range(4):
                mol[l+18+23]=da3[np.argmin(dhh)]
                dhh[np.argmin(dhh)]=100
            for l in range(4):
                mol[l+18+27]=ea3[np.argmin(ehh)]
                ehh[np.argmin(ehh)]=100

######################################################################
##DIPOLE in atomic_unit

            dipole=np.array([0,0,0],float)

            for l in range(18):
                dipole=dipole+index[l]*mol[l]*(0.3934303/0.2081943)

            for l in range(31):
                dipole=dipole-2*mol[18+l]*(0.3934303/0.2081943)

            f=open(res2,'a')
            f.write("%s  \t %.6f  \t %.6f  \t %.6f  \n" %('X',dipole[0],dipole[1],dipole[2]))
            f.close()
#########################################################################

#print("--- %s seconds ---" % (time.time() - start_time))