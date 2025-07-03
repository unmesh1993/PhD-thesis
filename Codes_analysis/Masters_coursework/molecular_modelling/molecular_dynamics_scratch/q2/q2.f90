program q2
implicit none
real::r,distance,tolerance,rxf,ryf,rzf,b,temp,vrms,sumvx=0,sumvy=0,sumvz=0,fvx,v
integer::i,k,iteration=0,a
real,dimension(:),allocatable::rx,ry,rz,trx,try,trz,vx,vy,vz

write(*,*)'enter box length(specific=100),angstrom,number of argon atom(=100),temperature(=300)'
read (*,*)b,a,temp

tolerance=1.88!vanderwaal radii of argon

 
allocate (rx(a))
allocate (ry(a))
allocate (rz(a))
allocate (trx(a))
allocate (try(a))
allocate (trz(a))
allocate (vx(a))
allocate (vy(a))
allocate (vz(a))







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


!position coordinate in angstrom

open(1,file='argon.xyz' ,status='old')
write(1,*)a
write(1,*)'Argon'
do i=1,a
write(1,*)'Ar',rx(i),ry(i),rz(i)
end do
close(1)


!velocity coordinate in m/s  

vrms=((temp*1.3806*6.022)/.039948)**.5

write(*,*)'vrms of argon atom at 300K in m/s',vrms

open(2,file='Ar_int.velocity.dat' ,status='old')
write(2,*)'velocity in m/s'
open(3,file='Ar_f(vx)-vx.dat' ,status='old')



do i=1,a
call gaussian(v)
vx(i)=vrms*v
call gaussian(v)
vy(i)=vrms*v
call gaussian(v)
vz(i)=vrms*v
sumvx=sumvx+vx(i)
sumvy=sumvy+vy(i)
sumvz=sumvz+vz(i)


fvx=(exp((vx(i)**2)/(-2*vrms**2)))/((2*3.14156)**0.5*vrms)

write(3,*)vx(i),fvx

write(2,*)i,vx(i),vy(i),vz(i)

end do

write(*,*)'avg. velocity in x direction in m/s=',sumvx/a
write(*,*)'avg. velocity in y direction in m/s=',sumvy/a
write(*,*)'avg. velocity in z direction in m/s=',sumvz/a


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

!random gaussian distribution


Subroutine gaussian(v)
implicit none
real::v,v1,v2,ra,l1,l2
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
    
 20 CALL RANDOM_NUMBER(l1)
    CALL RANDOM_NUMBER(l2)
v1=2*l1-1
v2=2*l2-1

ra=v1**2+v2**2
if (ra==0 .OR. ra>=1) then
goto 20
end if

v=((-2*log(ra)/ra)**.5)*(v1)

 

end subroutine gaussian


end program q2
