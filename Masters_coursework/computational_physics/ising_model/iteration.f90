program ising3
implicit none


real::temp,E,mag,energy,magnetisation,l,delE,boltzmann,start,finish

integer::i,j,k,left,right,up,down,back,front,x,y,z,tot,h,m,iteration,p,q,r



integer,dimension(:,:,:),allocatable::spin


!----------------------------------------------------------------------

write(*,*)'Enter temperature'
read(*,*)temp 

write(*,*)'dimension in 3D separated by commas'
read(*,*)x,y,z

m=20000

!----------------------------------------------------------------------

Allocate (spin(x,y,z))

tot=x*y*z
write(*,*)tot

!-----------------------------------------------------------------------

call cpu_time(start)

!-------------------------------------------------------------------------

mag=0

do i=1,x
do j=1,y
do k=1,z

call random(l)

if(l <= 0.5) then
spin(i,j,k)=-1
else
spin(i,j,k)=1
end if


mag=mag+spin(i,j,k)

end do 
end do
end do

magnetisation=mag


!--------------------------------------------------------------------------------

call En(energy,x,y,z,spin)

write(*,*)"energy per spin=",energy/(real(tot))
write(*,*)"magnetisation per spin=",magnetisation/(real(tot))

!------------------------------------------------------------------------------

!metropolis algorithm
open(1,file='energy.dat' ,status='unknown',form='formatted')
open(2,file='mag.dat' ,status='unknown',form='formatted')

!-------------------------------------------------------------------------------

do iteration=1,m

do h=1,tot


call random(l)
i=int(l*x) +1

call random(l)
j=int(l*y) +1

call random(l)
k=int(l*z) +1


!x dimension

if (i==1) then
left=x
else
left=i-1
end if


if (i==x)then 
right=1
else
right=i+1
end if


!y dimension


if (j==1) then
up=y
else
up=j-1
end if

if (j==y)then
down=1
else
down=j+1
end if



!z dimension

if (k==1) then 
back=z
else
back=k-1
end if

if (k==z) then
front=1
else
front=k+1
end if



delE=2*spin(i,j,k)*(spin(left,j,k)+spin(right,j,k)+spin(i,up,k)+spin(i,down,k)+spin(i,j,back)+spin(i,j,front))


!-------------------------------------------------------------------------------------------------------------------------



if (delE .lt. 0.000)  then

     spin(i,j,k)=(-1)*spin(i,j,k)!chnaged spin
     Energy=Energy+delE
     
else

     call random(l)
     boltzmann=exp((-1.0)*delE/real(temp))

if (l .lt. boltzmann ) then

     spin(i,j,k)=(-1.0)*spin(i,j,k)!chnaged spin
     Energy=Energy+delE
     
end if
end if

end do

!--------------------------------------------------------------------------------------------------------------------------




if (iteration > m/4) then

magnetisation=sum(spin)



write(1,*)iteration,energy/(real(tot))
write(2,*)iteration,magnetisation/(real(tot))

energy=0

end if

end do

close(1)
close(2)

!--------------------------------------------------------------------------------------------------------------



call cpu_time(finish)

write(*,*)"time taken by cpu in s",finish-start

!---------------------------------------------------------------------------------------------------------------------

contains

subroutine En(energy,x,y,z,spin)

real::energy
integer::x,y,z,spin(x,y,z)


E=0

do i=1,x
do j=1,y
do k=1,z


!x dimension

if (i==1) then
left=x
else
left=i-1
end if


if (i==x)then 
right=1
else
right=i+1
end if


!y dimension


if (j==1) then
up=y
else
up=j-1
end if

if (j==y)then
down=1
else
down=j+1
end if



!z dimension

if (k==1) then 
back=z
else
back=k-1
end if

if (k==z) then
front=1
else
front=k+1
end if



E=E-spin(i,j,k)*(spin(left,j,k)+spin(right,j,k)+spin(i,up,k)+spin(i,down,k)+spin(i,j,back)+spin(i,j,front))


end do 
end do
end do


energy=E/2

end subroutine En


!------------------------------------------------------------------------------------------------------------------------


Subroutine random(l)
implicit none
real::l
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

end subroutine random

!--------------------------------------------------------------------------------------------------------------------------------

end program ising3
