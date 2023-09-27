program q2
implicit none

real*8::r,g,distance,tolerance,rxf,ryf,rzf,temp,vrms,b,c,Ekin=0.d0,potential=0.d0

real*8::sigma=1.d0,epsilon=1.d0,mass=1.d0,sr2,sr6,sr12,forcex,forcey,forcez,force,dt,pe,te,potcut



integer::i,j,k,a,n

real*8,dimension(:),allocatable::rx,ry,rz,trx,try,trz,vx,vy,vz,ax,ay,az

real*8::sumvx,sumvy,sumvz,sf,avx,avy,avz,ksr2,ksr6,ksr12

real*8::nu=0.0001

!nu:frequency of collision with water bath

write(*,*)'enter box length(=100) angstrom,number of  atom (=100),number of timestep(=500)'
read (*,*)b,a,n



tolerance=1.2*sigma
potcut=2.5d0*sigma
temp=1



allocate (rx(a))
allocate (ry(a))
allocate (rz(a))
allocate (trx(a))
allocate (try(a))
allocate (trz(a))
allocate (vx(a))
allocate (vy(a))
allocate (vz(a))
allocate (ax(a))
allocate (ay(a))
allocate (az(a))

!--------------------------------------------------------------------------------------------------

open(7,file='average.dat' ,status='unknown', form='formatted')
write(7,*)'   x-direction              y-direction               z-direction'
close(7)


open(6,file='total_energy.agr',status='unknown', form='formatted')
write(6,*)'     '
close(6)


open(5,file='potential.dat',status='unknown', form='formatted')
write(5,*)'     '
close(5)

open(4,file='ke.dat',status='unknown', form='formatted')
write(4,*)'     '
close(4)

open(3,file='acceleration.dat' ,status='unknown', form='formatted')
write(3,*)'     '
close(3)



!--------------------------------------------------------------------------------------------------

open(10,file='traj.xyz' ,status='unknown', form='formatted')
write(10,*)'1'
write(10,*)'Argon_atom'

open(1,file='position.xyz' ,status='unknown', form='formatted')
write(1,*)a
write(1,*)'Argon_atom'


call random(r)
rx(1)=r
call random(r)
ry(1)=r
call random(r)
rz(1)=r

write(1,*)'Ar',rx(1),ry(1),rz(1)
write(10,*)'Ar',rx(1),ry(1),rz(1)

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
ryf=trz(i)-rz(k)



distance=(rxf**2+ryf**2+rzf**2)**.5

if(distance < tolerance) then
goto 10
end if
end do

rx(i)=trx(i)   
ry(i)=try(i)
rz(i)=trz(i)


write(1,*)'Ar',rx(i),ry(i),rz(i)
end do
close(1)
close(10)


!----------------------------------------------------------------------------------------------


vrms=sqrt(temp) 

do i= 1,a


call gaussian(g)
vx(i)=vrms*g

call gaussian(g)
vy(i)=vrms*g

call gaussian(g)
vz(i)=vrms*g

end do

!------------------------------------------------------------------------------------------------------

!rescaling velocity and setting centre of mass velocity to zero

sumvx=sum(vx)/a
sumvy=sum(vy)/a
sumvz=sum(vz)/a




Ekin=(dot_product(vx,vx)+dot_product(vy,vy)+dot_product(vz,vz))

sf=sqrt(3.d0*(a-1)*temp/Ekin)

Ekin=0.d0

!(vx-sumvx):fixing centre of mass velocity drift
!sf:velocity rescaling 

do i=1,a
vx(i)=(vx(i)-sumvx)*sf
vy(i)=(vy(i)-sumvy)*sf
vz(i)=(vz(i)-sumvz)*sf
end do

sumvx=0.d0
sumvy=0.d0
sumvz=0.d0

!---------------------------------------------------------------------------------------------------------



open(2,file='velocity.dat',status='unknown', form='formatted')
write(2,*)'dt=0'

do i= 1,a


write(2,*)i,vx(i),vy(i),vz(i)

end do
close(2)

!-------------------------------------------------------------------------------------------------------------



!----------------------------------------------------------------------------------------------------------

!velocity verlet algorithm dt 



dt=0

call acceleration(ax,ay,az,rx,ry,rz,a,b,dt,tolerance,pe)

!-------------------------------------------------------------------------------------------------------------

dt=1

do while(dt <= n)



do i=1,a

rx(i)=rx(i)+dt*vx(i)/(10**4)+(dt*dt*.5*ax(i))/(10**8)
ry(i)=ry(i)+dt*vy(i)/(10**4)+(dt*dt*.5*ax(i))/(10**8)
rz(i)=rz(i)+dt*vz(i)/(10**4)+(dt*dt*.5*ax(i))/(10**8)

vx(i)=vx(i)+(dt*.5d0*ax(i))/(10**4)
vy(i)=vy(i)+(dt*.5d0*ax(i))/(10**4)
vz(i)=vz(i)+(dt*.5d0*ax(i))/(10**4)

end do


sumvx=sum(vx)/a
sumvy=sum(vy)/a
sumvz=sum(vz)/a

Ekin=(dot_product(vx,vx)+dot_product(vy,vy)+dot_product(vz,vz))

sf=sqrt(3.d0*(a-1)*temp/Ekin)

Ekin=0.d0

!(vx-sumvx):fixing centre of mass velocity drift
!sf:velocity rescaling 

do i=1,a
vx(i)=(vx(i)-sumvx)*sf
vy(i)=(vy(i)-sumvy)*sf
vz(i)=(vz(i)-sumvz)*sf
end do

sumvx=0.d0
sumvy=0.d0
sumvz=0.d0

!------------------------------------------------------------------------------------------------------

call pbc(rx,ry,rz,a,b,dt)



!------------------------------------------------------------------------------------------------------------


call acceleration(ax,ay,az,rx,ry,rz,a,b,dt,tolerance,pe)


!-------------------------------------------------------------------------------------------------------------



do i=1,a

vx(i)=vx(i)+(dt*.5d0*ax(i))/(10**4)
vy(i)=vy(i)+(dt*.5d0*ax(i))/(10**4)
vz(i)=vz(i)+(dt*.5d0*ax(i))/(10**4)

end do


!------------------------------------------------------------------------------------------------------

!normal thermostat


sumvx=sum(vx)/a
sumvy=sum(vy)/a
sumvz=sum(vz)/a

Ekin=(dot_product(vx,vx)+dot_product(vy,vy)+dot_product(vz,vz))

sf=sqrt(3.d0*(a-1)*temp/Ekin)

Ekin=0.d0

!(vx-sumvx):fixing centre of mass velocity drift
!sf:velocity rescaling 

do i=1,a
vx(i)=(vx(i)-sumvx)*sf
vy(i)=(vy(i)-sumvy)*sf
vz(i)=(vz(i)-sumvz)*sf
end do


open(7,file='average.dat',status='old',position='append')
write(7,*)sumvx,sumvy,sumvz
close(7)


sumvx=0
sumvy=0
sumvz=0



!---------------------------------------------------------------------------------------



open(2,file='velocity.dat' ,status='old',position='append')
write(2,*)'dt=',dt/(10**4)

do i=1,a
write(2,*)i,vx(i),vy(i),vz(i)
end do

close(2)

!--------------------------------------------------------------------------------------------------------------


open(4,file='ke.dat',status='old',position='append')
open(6,file='total_energy.agr',status='old',position='append')

Ekin=(dot_product(vx,vx)+dot_product(vy,vy)+dot_product(vz,vz))/a

Ekin=.5*Ekin 
te=pe+Ekin  

write(4,*)dt/(10**4),Ekin
write(6,*)dt/(10**4),te

Ekin=0

close(4)
close(6)

dt=dt+1

end do

!-----------------------------------------------------------------------------------------------------------------

contains 


Subroutine random(r)
implicit none
real*8::l,r

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


!-----------------------------------------------------------------------------------------------

!random gaussian distribution

Subroutine gaussian(v)
implicit none
real*8::v,v1,v2,ra,l1,l2
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

!-----------------------------------------------------------------------------------------------------------------

subroutine acceleration(ax,ay,az,rx,ry,rz,a,b,dt,tolerance,pe)
implicit none
real*8::ax(a),ay(a),az(a),rx(a),ry(a),rz(a),b,dt,tolerance,pe
integer::a


do i =1,a
ax(i)=0
ay(i)=0
az(i)=0
end do



do i=1,a-1
do j=i+1,a

rxf=rx(j)-rx(i)
ryf=ry(j)-ry(i)
rzf=rz(j)-rz(i)


!minimum image convention
rxf=rxf-b*nint(rxf/b)

ryf=ryf-b*nint(ryf/b)

rzf=rzf-b*nint(rzf/b)

distance=(rxf**2+ryf**2+rzf**2)



if (sqrt(distance) < potcut) then

sr2=sigma**2/distance
sr6=sr2**3
sr12=sr6**2

ksr2=(sigma/potcut)**2
ksr6=ksr2**3
ksr12=ksr6**2



force=48*epsilon*(sr12-0.5*sr6)/distance



forcex=force*rxf-48*epsilon*((ksr12/potcut)-.5*(ksr12/potcut))   
forcey=force*ryf-48*epsilon*((ksr12/potcut)-.5*(ksr12/potcut))
forcez=force*rzf-48*epsilon*((ksr12/potcut)-.5*(ksr12/potcut))

potential=potential+(sr12-sr6)*4*epsilon+sqrt((force*rxf*rxf)**2+(force*ryf*ryf)**2+(force*rzf*rzf)**2)-4*epsilon*(ksr12-ksr6)


ax(i)=ax(i)+(forcex/mass)   
ax(j)=ax(j)-(forcex/mass)


ay(i)=ay(i)+(forcey/mass)
ay(j)=ay(j)-(forcey/mass)


az(i)=az(i)+(forcez/mass)
az(j)=az(j)-(forcez/mass)

elseif (sqrt(distance) >= potcut) then

potential=potential

ax(i)=ax(i)
ax(j)=ax(j)

ay(i)=ay(i)
ay(j)=ay(j)

az(i)=az(i)
az(j)=az(j)


end if

end do

end do

open(5,file='potential.dat',status='old',position='append')

write(5,*)dt/(10**4),potential/a 

pe=potential/a
potential=0




open(3,file='acceleration.dat' ,status='old',position='append')
write(3,*)'dt=',dt/(10**4)

do i=1,a

write(3,*)i,ax(i),ay(i),az(i)

end do

close(3)


end subroutine acceleration

!-----------------------------------------------------------------------------------------------------------

!using pbc such keep everything in the box

subroutine pbc(rx,ry,rz,a,b,dt)

implicit none

real*8::rx(a),ry(a),rz(a),b,dt
integer::a

do i= 1,a


rx(i)=rx(i)-b*nint(rx(i)/b)

ry(i)=ry(i)-b*nint(ry(i)/b)

rz(i)=rz(i)-b*nint(rz(i)/b)




end do

open(10,file='traj.xyz' ,status='old',position='append')
write(10,*)'1'
write(10,*)'Argon_atom'
write(10,*)'Ar',rx(1),ry(1),rz(1)

open(1,file='position.xyz' ,status='old',position='append')
write(1,*)a
write(1,*)'Argon_atom'


do i=1,a

write(1,*)'Ar',rx(i),ry(i),rz(i)


end do

close(1)
close(10)

end subroutine pbc


end program q2
