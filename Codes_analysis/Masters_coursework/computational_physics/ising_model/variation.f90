program ising3
implicit none


real::temp,tempi,tempf,E,mag,energy,magnetisation,l,delE,boltzmann,start,finish,en,en2,mg,mg2,sen,sen2,smg,smg2,deltatemp,sus,hc

integer::i,j,k,left,right,up,down,back,front,x,y,z,tot,h,m,iteration,p,q,r



integer,dimension(:,:,:),allocatable::spin


!----------------------------------------------------------------------

write(*,*)'Enter temperature initial final  and deltatemp'
read(*,*)temp,tempf,deltatemp 

write(*,*)'dimension in 3D separated by commas'
read(*,*)x,y,z

m=20000
tempi=temp



!----------------------------------------------------------------------

Allocate (spin(x,y,z))

tot=x*y*z


!-----------------------------------------------------------------------

call cpu_time(start)

!-------------------------------------------------------------------------

mag=0

do i=1,x
do j=1,y
do k=1,z

call random_number(l)

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

call Ene(energy,x,y,z,spin)

!------------------------------------------------------------------------------

open(3,file='E-T.dat' ,status='unknown',form='formatted')
open(4,file='M-T.dat' ,status='unknown',form='formatted')
open(5,file='X_T.dat' ,status='unknown',form='formatted')
open(6,file='Cv-t.dat' ,status='unknown',form='formatted')

write(3,*)'&'
write(4,*)'&'
write(5,*)'&'
write(6,*)'&'

!-------------------------------------------------------------------------------

do while (tempi >= tempf)

do iteration=1,m

do h=1,tot


call random_number(l)
i=int(l*x) +1

call random_number(l)
j=int(l*y) +1

call random_number(l)
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

     spin(i,j,k)=(-1.0)*spin(i,j,k)!chnaged spin
     Energy=Energy+delE
     
else

     call random_number(l)
     boltzmann=exp((-1.0)*delE/real(tempi))

if (l .lt. boltzmann ) then

     spin(i,j,k)=(-1.0)*spin(i,j,k)!chnaged spin
     Energy=Energy+delE
     
end if
end if

end do

!--------------------------------------------------------------------------------------------------------------------------


magnetisation=sum(spin)

if (iteration > m*.2) then



en=en+energy
mg=mg+magnetisation
en2=en2+energy**2
mg2=mg2+magnetisation**2

end if

end do



sen=en/(.8*m*real(tot))
smg=mg/(.8*m*real(tot))
!sen2=en2/(.8*m*real(tot))
!smg2=mg2/(.8*m*real(tot))

hc=(en2/real(.8*m)-(en/real(.8*m))**2)/tempi**2
sus=(mg2/real(.8*m)-(mg/real(.8*m))**2)/tempi

write(3,*)tempi,sen
write(4,*)tempi,smg
write(5,*)tempi,sus
write(6,*)tempi,hc

en=0
en2=0
mg=0
mg2=0

tempi=tempi-deltatemp

end do


!--------------------------------------------------------------------------------------------------------------



call cpu_time(finish)

write(*,*)"time taken by cpu in s",finish-start

!---------------------------------------------------------------------------------------------------------------------

contains

subroutine Ene(energy,x,y,z,spin)

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

end subroutine Ene


!------------------------------------------------------------------------------------------------------------------------


!--------------------------------------------------------------------------------------------------------------------------------

end program ising3
