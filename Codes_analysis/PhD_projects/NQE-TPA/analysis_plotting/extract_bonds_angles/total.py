import numpy as np
import os
import math
import time





#start_time = time.time()

###################################################################

#res=(input ("name of .xyz file: "))
#f=open('/home/unmesh/Downloads/calculation/cp2k/TPA_path_integral/F1A2/DFT-D3/AIMD/GLE/50K/analysis/TPA-pos-1.xyz','r')
res="pos_tot.xyz"
res="cord.xyz"

f=open(res,'r')
a=f.readlines()
f.close

#####################################################################

tim=2
if tim == 1:
    res=(input ("name of .ener file for time: "))
    f=open(res,'r')
    h=f.readlines()
    f.close
    del h[0]

    coord1=[]
    for i in range(len(h)):
        x=h[i].split()
        coord1.append(x)
    del x,h
    coord1=np.array(coord1,float)

#############################################

natoms=360
frames=int(len(a)/(natoms+2))

###########################################

from TPA_dihedral import TPA

TPA(natoms,frames,a)

##############################################

from TPA_H_a import TPA

TPA(natoms,frames,a)

###########################################

from TPA_H_b import TPA

TPA(natoms,frames,a)


###########################################

from TPA_H_d import TPA

TPA(natoms,frames,a)


###########################################

from TPA_H_c import TPA

TPA(natoms,frames,a)


###########################################


del natoms,frames,a,tim

#print("--- %s seconds ---" % (time.time() - start_time))
