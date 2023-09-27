# coding: utf8


import numpy as np
import os


print ("there are issues with first step. number of wannier center printed is wrong. please check with analysis ")

os.system('rm output.txt')

fn=input ('input .dcd file: ')

# DCD file header 
#   (name, dtype, shape)
# numpy dtypes:
#   i4  = int32
#   f4  = float32 (single precision)
#   f8  = float64 (double precision)
#   S80 = string of length 80 (80 chars)
HEADER_TYPES = [\
    ('blk0-0',  'i4',1  ),  # 84 (start of first block, size=84 bytes)                    
    ('hdr',     'S4',1  ),  # 'CORD'
    ('9int',    'i4',9  ),  # 9 ints, mostly 0
    ('timestep','f4',1  ),  # timestep (float32)
    ('10int',   'i4',10 ),  # 10 ints, mostly 0, last is 24
    ('blk0-1',  'i4',1  ),  # 84
    ('blk1-0',  'i4',1  ),  # 164 
    ('ntitle',  'i4',1  ),  # 2
    ('remark1', 'S80',1 ),  # remark1
    ('remark2', 'S80',1 ),  # remark2
    ('blk1-1',  'i4',1  ),  # 164
    ('blk2-0',  'i4',1  ),  # 4 (4 bytes = int32)
    ('natoms',  'i4',1  ),  # natoms (int32)
    ('blk2-1',  'i4',1  ),  # 4
    ] 

HEADER_DTYPE = np.dtype(HEADER_TYPES)




"""Read dcd file. Fastest version. Calculates nstep from bytes between
end-of-header and EOF.

Parameters
----------
fn : str
    filename
convang : bool
    convert angles from cosine to degree (only useful for lammps style dcd
    files)

Returns
-------
ret : (cryst_const, coords)
    | cryst_const : (nstep,6) float64 array, (a,b,c,alpha,beta,gamma),
    |               Angstrom, degrees
    | coords : (nstep, natoms, 3) float32 array, cartesian coords Angstrom

Examples
--------
>>> # default settings read cp2k files
>>> cc,co = read_dcd_data('cp2k.dcd')
>>> cc,co = read_dcd_data('cp2k.dcd', convang=False)
>>> cc,co = read_dcd_data('lammps.dcd', convang=True)
"""
fd = open(fn, 'rb')
natoms = np.fromfile(fd, HEADER_DTYPE, 1)[0]['natoms']
fd_pos = fd.tell()
# seek to end
fd.seek(0, os.SEEK_END) 
# number of bytes between fd_pos and end
fd_rest = fd.tell() - fd_pos  
# reset to pos after header
fd.seek(fd_pos)
# calculate nstep: fd_rest / bytes_per_timestep
# 4 - initial 48
# 6*8 - cryst_const_dcd
# 7*4 - markers between x,y,z and at the end of the block
# 3*4*natoms - float32 cartesian coords
nstep = fd_rest / (4 + 6*8 + 7*4 + 3*4*natoms*1.0)
assert nstep % 1.0 == 0.0, ("calculated nstep is not int, cannot "
                            "read file '{}'".format(fn))
nstep = int(nstep)
# dtype for fromfile: nstep times dtype of a timestep data block
dtype = \
    np.dtype(([('x0', 'i4'), 
               ('x1', 'f8', (6,)), 
               ('x2', 'i4', (2,)), 
               ('x3', 'f4', (natoms,)), 
               ('x4', 'i4', (2,)), 
               ('x5', 'f4', (natoms,)), 
               ('x6', 'i4', (2,)), 
               ('x7', 'f4', (natoms,)), 
               ('x8', 'i4')], 
               (nstep,)))
arr = np.fromfile(fd, dtype, 1)
fd.close()
cryst_const = np.empty((nstep,6), dtype=np.float64)
cryst_const[:,0] = arr['x1'][0,:,0]
cryst_const[:,1] = arr['x1'][0,:,2]
cryst_const[:,2] = arr['x1'][0,:,5]
cryst_const[:,3] = arr['x1'][0,:,4]
cryst_const[:,4] = arr['x1'][0,:,3]
cryst_const[:,5] = arr['x1'][0,:,1]
coords = np.empty((nstep,natoms,3), dtype=np.float32)
coords[...,0] = arr['x3'][0,...]
coords[...,1] = arr['x5'][0,...]
coords[...,2] = arr['x7'][0,...]
#if convang:
#    cryst_const[:,3:] = np.arccos(cryst_const[:,3:])*180.0/np.pi

label=[]
fn=input('template xyz file: ')
fd = open(fn,'r')
a=fd.readlines()
fd.close

del a[1],a[0]
for i in range(natoms):
    x=a[i].split()[0]
    label.append(x)

n=360

for i in range(nstep):
    print (natoms-n,file=open("output.txt", "a"))
    print (cryst_const[i,0],cryst_const[i,1],cryst_const[i,2],cryst_const[i,3],cryst_const[i,4],cryst_const[i,5],file=open("output.txt", "a"))
    for k in range(n,natoms):
        print (label[k],coords[i,k,0],coords[i,k,1],coords[i,k,2],file=open("output.txt", "a"))

os.system('mv output.txt position_dcd.xyz')


