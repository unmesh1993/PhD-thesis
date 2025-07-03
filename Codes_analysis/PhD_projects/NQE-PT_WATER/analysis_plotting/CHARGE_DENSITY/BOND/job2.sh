#PBS -q batch
#PBS -l nodes=1:ppn=28
#PBS -N scf_5
#PBS -e error-1n.out
#PBS -o output-1n.out
#PBS -l walltime=96:00:00
module purge



module load compiler/intel_2015
#module load apps/intel/cp2k/4.1-2015



cd $PBS_O_WORKDIR
echo "job started on 'hostname' at 'date'"
echo $HOSTNAME
# mention your executable with arguments here

##################################################

frame=49

rm -r classical2
mkdir classical2
cd classical2/
for i in `seq 0 $frame`
do
cat /home/unmesh/calculation/cp2k/Pt_H2O/NSM_Pt111/BOMD/ModelA/H0/AIMD/analysis/charge_transfer2/coordinates/dir$i/cord.xyz   >> del1 
done
~/software/anaconda3/bin/python ../tabulate_1.py del1 prop_1.dat prop_2.dat prop_3.dat  
cd ../

mkdir quantum2
cd quantum2/
for i in `seq 0 $frame`
do
cat /home/unmesh/calculation/cp2k/Pt_H2O/NSM_Pt111/BOMD/ModelA/H0/PIMD/analysis/charge_transfer2/coordinates/dir$i/cord.xyz  >> del1
done
~/software/anaconda3/bin/python ../tabulate_1.py del1 prop_1.dat prop_2.dat prop_3.dat 
cd ../


now=$(date +"%T")
echo "Current time : $now"


