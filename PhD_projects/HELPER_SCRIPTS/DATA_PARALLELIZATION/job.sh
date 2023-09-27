#!/bin/bash
#SBATCH -N 4
#SBATCH --ntasks-per-node=48
#SBATCH --job-name=mm
##SBATCH --output=X_%j.out
##SBATCH --error=X_%j.err
#SBATCH --time=22:00:00
##SBATCH --qos=

##################################################
module purge
module load compiler/intel/2017.7.259
module load anaconda3/anaconda3
cd $SLURM_SUBMIT_DIR


##################################################
now=$(date +"%T")
echo "Current time : $now"

rm prop_1.dat prop_2.dat prop_3.dat

file='~/TEST-56Pt4ang-highk-pos-1-pbc.xyz'
prop='~/data_plot/small_H0/finale/bond_2021.py'

nprocs=180
###########################
lines=$(wc -l ${file} | awk '{print $1}')
float=$(python -c "print ($lines / (662 * $nprocs))")
frames=${float%.*}

echo  $frames
rm -r del_1
mkdir del_1
for (( i = 1; i <= $nprocs; i++ ))
do
ii=$(python -c "print (( $i - 1 ) * 662 * $frames + 1)")
ff=$(python -c "print ($i * 662 * $frames)")
if [ $i -eq $nprocs ] ; then
   ff=$lines
fi

sed -n ${ii},${ff}p $file > del_1/test${i}.xyz
done

cd del_1/
for (( i = 1; i <= $nprocs; i++ ))
do
mkdir dir$i
cd dir$i
srun --exclusive -N1 -n1 python $prop ../test${i}.xyz  layer1.dat layer2.dat layer3.dat &
cd ../
done
wait

cd ../

rm fuck.dat
for (( i = 1; i <= $nprocs; i++ ))
do
    cat del_1/dir$i/layer1.dat >> fuck1.dat
    cat del_1/dir$i/layer2.dat >> fuck2.dat
    cat del_1/dir$i/layer3.dat >> fuck3.dat
done
mv fuck1.dat prop_1.dat
mv fuck2.dat prop_2.dat
mv fuck3.dat prop_3.dat

rm -r del_1


now=$(date +"%T")
echo "Current time : $now"
