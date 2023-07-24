name=start56
name2=1
mkdir ../$name
tail -n662 simulation.xc.xyz > ../$name/cord.xyz
tail -n662 simulation.xc.xyz > ../$name/tmp.xyz
cp dir$name2/TEST-56Pt4ang-highk-dump-1.psf ../$name/start.psf
cp *in* ../$name/
cp job.sh ../$name/



grep -B50000 R_BUF QMMM.inc > q2q2q.dat

echo "       &RESTART_INFO" >> q2q2q.dat
tac dir$name2/pimd_glet_${name2}.out | grep -B500 -m1 "BOB buffer new_indices" | tac | sed 's/BOB buffer new_indices/INDICES/g;s/BOB buffer new_labels/LABELS/g' | sed '/FORCE MIXING/,$d' | sed -z 's/\n/ ,\n /g' | sed "s/,/\\\/g" >> q2q2q.dat
echo "       &END RESTART_INFO" >> q2q2q.dat

grep -A10000 "&END FORCE_MIXING" QMMM.inc >> q2q2q.dat

mv q2q2q.dat ../$name/QMMM.inc

sed '/HOST/c\HOST localhost' in.cp2k > ../$name/in.cp2k

#sed '/address/c\   <address>localhost</address>' simulation.chk  > ../$name/input.xml
sed '/address/c\   <address>localhost</address>' RESTART  > ../$name/input.xml