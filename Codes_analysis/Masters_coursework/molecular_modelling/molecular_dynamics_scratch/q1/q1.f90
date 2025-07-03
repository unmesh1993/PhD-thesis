program q1
implicit none
real::r,distance,tolerance,rxf,ryf,rzf,b,x,y,z
integer::i,j,k,iteration=0,a,q
real,dimension(:),allocatable::rx,ry,rz,trx,try,trz,rh1x,rh1y,rh1z,rh2x,rh2y,rh2z

write(*,*)'number of particles at temperature 300 K'
read (*,*)a


tolerance=2.8!vanderwaal radii of watermolecule
b=(a*18.01528*10/6.022*.9970)**(.333)! length of box  in angstrom 

 
allocate (rx(a))
allocate (ry(a))
allocate (rz(a))
allocate (trx(a))
allocate (try(a))
allocate (trz(a))
allocate (rh1x(a))
allocate (rh1y(a))
allocate (rh1z(a))
allocate (rh2x(a))
allocate (rh2y(a))
allocate (rh2z(a))





call random(r,x)
rx(1)=r
call random(r,x)
ry(1)=r
call random(r,x)
rz(1)=r

write(1,*)1,rx(1),ry(1),rz(1)

do i=2,a

10 call random(r,x)
trx(i)=r
call random(r,x)
try(i)=r
call random(r,x)
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

!OH distance=.991
call random(r,x)
call random(r,y)
rh1x(i)=rx(i)+.991*sin(3.14156*x)*cos(2*3.14156*y)
rh1y(i)=ry(i)+.991*sin(3.14156*x)*sin(2*3.14156*y)
rh1z(i)=rz(i)+.991*cos(3.14156*x)


rh2x(i)=rx(i)+.991*sin(3.14156*x+105.5)*cos(2*3.14156*y)
rh2y(i)=ry(i)+.991*sin(3.14156*x+105.5)*sin(2*3.14156*y)
rh2z(i)=rz(i)+.991*cos(3.14156*x+105.5)



end do







open(1,file='water.xyz' ,status='old')
write(1,*)3*a
write(1,*)'water molecule'

do i=1,a

write(1,*)'O',rx(i),ry(i),rz(i)
write(1,*)'H',rh1x(i),rh1y(i),rh1z(i)
write(1,*)'H',rh2x(i),rh2y(i),rh2z(i)

end do


contains

Subroutine random(r,l)
implicit none
real::r,l
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
 
r=(b-1)*l+1

end subroutine random

end program q1
