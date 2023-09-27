program q1
implicit none
real::dx,dy,dz,b,tolerance,distance,r
integer::i,a,j,k
real,dimension(:),allocatable::rx,ry,rz

write(*,*)'enter box length(=100),angstrom,number of argon atom(=100)'
read (*,*)b,a

tolerance=1.96!vanderwaal radii of argon

 
allocate (rx(a))
allocate (ry(a))
allocate (rz(a))







do i=1,a

call random(r)
rx(i)=r
call random(r)
ry(i)=r
call random(r)
rz(i)=r

end do

open(1,file='mbi.dat',status='old')

!minimum image convention
do i=1,a-1
do j=i+1,a
dx=rx(i)-rx(j)
dy=ry(i)-ry(j)
dz=rz(i)-rz(j)

dx=dx-b*nint(dx/b)

dy=dy-b*nint(dy/b)

dz=dz-b*nint(dz/b)


!calculate potential and forces
write(1,*)dx,dy,dz

end do
end do




!periodic boundary condition


open(2,file='pbc.dat',status='old')


do i= 1,a

!changing the initial position


rx(i)=(100)*rx(i)

ry(i)=(505)*ry(i)

rz(i)=(-54500)*rz(i)

!using pbc such keep everything in the box

rx(i)=rx(i)-b*nint(rx(i)/b)

ry(i)=ry(i)-b*nint(ry(i)/b)

rz(i)=rz(i)-b*nint(rz(i)/b)

write(2,*)i,rx(i),ry(i),rz(i)

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
 
r=b*l-b/2

end subroutine random

end program q1



 



