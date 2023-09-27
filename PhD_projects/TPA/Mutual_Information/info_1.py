import numpy as np
import matplotlib
#matplotlib.use('Agg')
from matplotlib import pyplot as plt
import os
import seaborn as sns
sns.set()


bin=int(100)
def kl_divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))

res1='/gpfs/scratch/pr1elh00/pr1elh03/PROD/PIMD/70k/16bead/analysis/all/00/properties_1.dat'
res2='/gpfs/scratch/pr1elh00/pr1elh03/PROD/PIMD/100k/16bead/analysis/all/00/properties_1.dat'
res3='/gpfs/scratch/pr1elh00/pr1elh03/PROD/PIMD/200k/16bead/analysis/all/00/properties_1.dat'
res4='/gpfs/scratch/pr1elh00/pr1elh03/PROD/PIMD/300k/16bead/analysis/all/00/properties_1.dat'
res5='/gpfs/scratch/pr1elh00/pr1elh03/PROD/PIMD_D/70k/16bead/analysis/all/00/properties_1.dat'

res1='/home/unmesh/Downloads/calculation/cp2k/TPA_path_integral/IR_PROP_CODING_TEST/PROP/del1'

for qw in range(1,2):
    if qw == 1:
       res=res1
    elif qw ==2:
       res=res2
    elif qw ==3:
       res=res3
    elif qw ==4:
       res=res4
    elif qw ==5:
       res=res5

    f=open(res,'r')
    a=f.readlines()
    f.close
    nft=2
    store=np.zeros((nft,nft),dtype=float)
    np.fill_diagonal(store, 1)

    nbonds=40
    frames=int(len(a)/(nbonds))
    V=np.zeros((frames,nft),dtype=float)
    for i in range(frames):
        for j in range(20):
            t1=a[j+(i)*nbonds].split()
            t2=a[j+20+(i)*nbonds].split()
            V[i,0]=t1[1]
            V[i,1]=t2[1]
            del t1,t2
    del a,nbonds,frames

    
    ###PLOT###############################################################
    corr_matrix=np.corrcoef(V.T)
    ######################################################################
    
    for l in range (0,nft-1):
      for ll in range (l+1,nft): 
          
        V1=np.array(V[:,l],float)
        V2=np.array(V[:,ll],float)
        max_V1=np.max(V1)
        min_V1=np.min(V1)
        max_V2=np.max(V2)
        min_V2=np.min(V2)
    
    
        V1=(V1-min_V1)/(max_V1-min_V1)
        V2=(V2-min_V2)/(max_V2-min_V2)
    
      
        pq=np.histogram2d(V1, V2, bins=(bin,bin))[0]
        
        pqn= pq.T   
    
        pqn=pqn/np.sum(pqn)
        N_pqn=np.count_nonzero(pqn)
        
        
        pqn[ pqn == 0 ] = 0.000000000000000001
        pqn[ pqn != 0 ] += -0.000000000000000001/N_pqn
        
        pn = np.ravel(pqn.sum(axis=1))
        qn = np.ravel(pqn.sum(axis=0))
        
        sum3=0
        for i in range(bin):
            for j in range(bin):
                sum3 = sum3 + kl_divergence(pqn[i,j] , pn[i]*qn[j])
        
        norm = (np.sum (-1 * pn * np.log (pn)) + np.sum (- 1 * qn * np.log (qn)) )/2 
        sum3=sum3/norm
    
    #    ff.write("%i  \t %i   \t  %.3f \t  %.3f \n" %(l,ll,sum3,corr_matrix[l,ll]))
        store[l,ll]    = sum3 
        store[ll,l]    = corr_matrix[l,ll]  

    print (store)
#    for l in range (nft):
#        for ll in range (nft):
#            print (l,ll,store[l,ll])

    del N_pqn,V,V1,V2,corr_matrix,i,j,l,ll,max_V1,max_V2,min_V1,min_V2
    del nft, norm, pn,pq,pqn,qn,store,sum3

#svm=sns.heatmap(store, annot = True, fmt=".2f", annot_kws={'size':4},square=True,cmap= 'coolwarm', linewidths=1, linecolor='black')
#figure = svm.get_figure()    
#figure.savefig('svm_conf.pdf')

#ff.close ()   
#os.system('nl output.dat > Info.dat')
#os.system('rm output.dat')

