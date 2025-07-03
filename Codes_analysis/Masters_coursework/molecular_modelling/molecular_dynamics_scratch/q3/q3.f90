program q3
implicit none
real::r,distance,tolerance,rxf,ryf,rzf,b,sigma=3.401,epsilon=.978638
real::sr2,sr6,sr12,forcex,forcey,forcez,force,potential,temp,pot=0
integer::i,j,k,a
real,dimension(:),allocatable::rx,ry,rz,trx,try,trz,fx,fy,fz

write(*,*)'enter box length(=100),angstrom,number of argon atom(=100),temperature(=300)'
read (*,*)b,a,temp


tolerance=1.88!vanderwaal radii of argon
 

 
allocate (rx(a))
allocate (ry(a))
allocate (rz(a))
allocate (trx(a))
allocate (try(a))
allocate (trz(a))
allocate (fx(a))
allocate (fy(a))
allocate (fz(a))

call random(r)
rx(1)=r
call random(r)
ry(1)=r
call random(r)
rz(1)=r

do i=2,a

10 call random(r)
trx(i)=r
call random(r)
try(i)=r
call random(r)
trz(i)=r

do k=1,i-1 

rxf=trx(i)-rx(k)
ryf=try(i)-ry(k)
rzf=trz(i)-rz(k)


distance=(rxf**2+ryf**2+rzf**2)**.5

if(distance < tolerance) then
goto 10
end if
end do

rx(i)=trx(i)
ry(i)=try(i)
rz(i)=trz(i)

end do

do i=1,a
fx(i)=0
fy(i)=0
fz(i)=0
end do

open(1,file='l_j_potential.dat' ,status='old')

do i=1,a-1
do j=i+1,a

rxf=rx(j)-rx(i)
ryf=ry(j)-ry(i)
rzf=rz(j)-rz(i)



distance=(rxf**2+ryf**2+rzf**2)

sr2=sigma**2/distance
sr6=sr2**3
sr12=sr6**2

potential=(sr12-sr6)*4*epsilon

force=48*epsilon*(sr12 - 0.5*sr6)/distance!in kj/mol A**2
forcex=force*rxf !in kj/mol A
forcey=force*ryf
forcez=force*rzf



fx(i)=fx(i)+forcex*(10**4)!in terms GigaNewton per mol
fx(j)=fx(j)-forcex*(10**4)

fy(i)=fy(i)+forcey*(10**4)
fy(j)=fy(j)-forcey*(10**4)

fz(i)=fz(i)+forcez*(10**4)
fz(j)=fz(j)-forcez*(10**4)


write(1,*)distance**.5,potential

pot=pot+potential

end do 
end do

write(*,*)'potential of each argon atom in KJ/mol',pot/a



close(1)



!Force in Newton/mol

open(3,file='Ar_force.dat',status='old')
write(3,*)'Force in GigaNewton/mol'
do i=1,a
write(3,*)i,fx(i),fy(i),fz(i)
end do

contains

Subroutine random(r)
implicit none
real::l,r

! variables for random seed setting 
  INTEGER :: i_seed
  INTEGER, DIMENSION(:), ALLOCATABLE :: a_seed
  INTEGER, DIMENSION(1:8) :: dt_seed
  !end of variables for seed setting 


 ! Set up random seed
  CALL RANDOM_SEED(size=i_seed)
  ALLOCATE(a_seed(1:i_seed))
  CALL RANDOM_SEED(get=a_seed)
  CALL DATE_AND_TIME(values=dt_seed)
  a_seed(i_seed)=dt_seed(8); a_seed(1)=dt_seed(8)*dt_seed(7)*dt_seed(6)
  CALL RANDOM_SEED(put=a_seed)
  DEALLOCATE(a_seed)
  ! Done setting up random seed 

CALL RANDOM_NUMBER(l)
r=b*l


end subroutine random


end program q3
