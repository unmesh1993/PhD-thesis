import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.colors import LogNorm
import sys
###
##
f=open('del1','r')
a=f.readlines()
f.close

coord1x=[]
coord1y1=[]
coord1y2=[]
coord1y3=[]
coord1y4=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[0]))
    coord1y1.append(x[9])
    coord1y2.append(x[1])
    coord1y3.append(x[2])
    coord1y4.append(x[3])
del x,a
d1x=np.array(coord1x,float)
d1y1=np.array(coord1y1,float)
d1y2=np.array(coord1y2,float)
d1y3=np.array(coord1y3,float)
d1y4=np.array(coord1y4,float)

f=open('del2','r')
a=f.readlines()
f.close

coord1x=[]
coord1y1=[]
coord1y2=[]
coord1y3=[]
coord1y4=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[0]))
    coord1y1.append(x[9])
    coord1y2.append(x[1])
    coord1y3.append(x[2])
    coord1y4.append(x[3])
del x,a
d2x=np.array(coord1x,float)
d2y1=np.array(coord1y1,float)
d2y2=np.array(coord1y2,float)
d2y3=np.array(coord1y3,float)
d2y4=np.array(coord1y4,float)

f=open('ddel1','r')
a=f.readlines()
f.close

coord1x=[]
coord1y1=[]
coord1y2=[]
coord1y3=[]
coord1y4=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[0]))
    coord1y1.append(x[9])
    coord1y2.append(x[1])
    coord1y3.append(x[2])
    coord1y4.append(x[3])
del x,a
d3x=np.array(coord1x,float)
d3y1=np.array(coord1y1,float)
d3y2=np.array(coord1y2,float)
d3y3=np.array(coord1y3,float)
d3y4=np.array(coord1y4,float)

f=open('ddel2','r')
a=f.readlines()
f.close

coord1x=[]
coord1y1=[]
coord1y2=[]
coord1y3=[]
coord1y4=[]
for i in range(len(a)):
    x=a[i].split()
    coord1x.append(float(x[0]))
    coord1y1.append(x[9])
    coord1y2.append(x[1])
    coord1y3.append(x[2])
    coord1y4.append(x[3])
del x,a
d4x=np.array(coord1x,float)
d4y1=np.array(coord1y1,float)
d4y2=np.array(coord1y2,float)
d4y3=np.array(coord1y3,float)
d4y4=np.array(coord1y4,float)


#################################################################################################
################### 

a=13.8593 
b=14.4030
c=23

#1
for i in range(4):
   if i == 0:
      x=d1x
      y=d1y1

      u=d1y2-d1y3
      v=d1y2+d1y3+d1y4-3*d1y2

      exh=0

   elif i == 1:
      x=d3x
      y=d3y1

      u=d3y2-d3y3
      v=d3y2+d3y3+d3y4-3*d3y2

      exh=0

   elif i == 2:
      x=d2x
      y=d2y1

      u=d2y2-d2y3
      v=d2y2+d2y3+d2y4-3*d2y2


      exh=2

   elif i == 3:
      x=d4x
      y=d4y1

      u=d4y2-d4y3
      v=d4y2+d4y3+d4y4-3*d4y2

      exh=1

   frames=len(x)/180
   die1,die2=1.5,2.5
   kill1=2.7
   
   a1=len(y[(y >= die1) & (y <= die2) & (x < c) ])/frames
   ca1=a1/(6.022*a*b*c*10**(-4))

   a2=len(y[(y > die2) & (x < c)])/frames
   ca2=a2/(6.022*a*b*c*10**(-4))
   
   a3=len(y[(y < die1) & (x < kill1)])/frames + exh
   ca3=a3/(6.022*a*b*c*10**(-4))
   
   print ('pH',-1*np.log10(ca3))

   #print ('pH2O',-1*np.log10(ca1))
   #print ('pOH',-1*np.log10(ca3))
  
   eql1=-1*np.log10(ca2*ca3/ca1)
   print ('pKeq',eql1)
   print ('proportion of OH- in contact layer',len(y[(y < die1) & (x < kill1)])/(frames))
   print ('proportion of H20 in contact layer',len(y[(y >= die1) & (y <= die2) & (x < kill1) ])/(frames))
   print ('-----------------------------------------------------')
