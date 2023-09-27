program md
implicit none

real*8::r,g,distance,tolerance,rxf,ryf,rzf,temp,temp1,vrms,b,c,Ekin=0.d0,potential=0.d0

real*8::sigma=1.d0,epsilon=1.d0,mass=1.d0,sr2,sr6,sr12,forcex,forcey,forcez,force,dt,pe,te,potcut

integer::i,j,k,a,n

real*8,dimension(:),allocatable::rx,ry,rz,trx,try,trz,vx,vy,vz,ax,ay,az

real*8::sumvx,sumvy,sumvz,sf,avx,avy,avz,ksr2,ksr6,ksr12,fminus,pminus

real*8::m=0.01

!nu:frequency of collision with water bath

write(*,*)'enter box length(=100) angstrom,number of  atom (=100),number of timestep(=500)'
read (*,*)b,a,n



tolerance=1.2d0*sigma
potcut=2.5d0*sigma
temp=1.d0


!---------------------------------------------------------------------------------------------
ksr2=(sigma/potcut)**2
ksr6=ksr2**3
ksr12=ksr6**2
fminus=48.d0*epsilon*(ksr12-.5d0*ksr6)/potcut
pminus=4.d0*epsilon*(ksr12-ksr6)
write(*,*)fminus,pminus
!---------------------------------------------------------------------------------------------


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

open(8,file='temp.dat',status='unknown',form='formatted')
write(8,*)'     '
close(8)

!------------------------------------------------------------------------------------------------------



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






Ekin=(dot_product(vx,vx)+dot_product(vy,vy)+dot_product(vz,vz))/a

sf=sqrt(3.d0*temp/Ekin)

vx=vx*sf
vy=vy*sf
vz=vz*sf

Ekin=0.d0

!(vx-sumvx):fixing centre of mass velocity drift
!sf:velocity rescaling 

sumvx=sum(vx)/a
sumvy=sum(vy)/a
sumvz=sum(vz)/a

do i=1,a
vx(i)=(vx(i)-sumvx)
vy(i)=(vy(i)-sumvy)
vz(i)=(vz(i)-sumvz)
end do

sumvx=0.d0
sumvy=0.d0
sumvz=0.d0

!---------------------------------------------------------------------------------------------------------



open(2,file='velocity.dat',status='unknown', form='formatted')

do i= 1,a
write(2,*)vx(i),vy(i),vz(i)
end do

close(2)

!-------------------------------------------------------------------------------------------------------------

!velocity verlet algorithm dt 

dt=0.d0

call acceleration(ax,ay,az,rx,ry,rz,a,b,dt,pe)

!-------------------------------------------------------------------------------------------------------------

dt=1.d0

do while(dt < n)

do i=1,a

rx(i)=rx(i)+dt*vx(i)*m+dt*dt*.5d0*ax(i)*m*m
ry(i)=ry(i)+dt*vy(i)*m+dt*dt*.5d0*ay(i)*m*m
rz(i)=rz(i)+dt*vz(i)*m+dt*dt*.5d0*az(i)*m*m


rx(i)=rx(i)-b*anint(rx(i)/b)
ry(i)=ry(i)-b*anint(ry(i)/b)
rz(i)=rz(i)-b*anint(rz(i)/b)


vx(i)=vx(i)+dt*.5d0*ax(i)*m
vy(i)=vy(i)+dt*.5d0*ay(i)*m
vz(i)=vz(i)+dt*.5d0*az(i)*m




end do

!-----------------------------------------------------------------------------------------------------------




!------------------------------------------------------------------------------------------------------


if (mod(n,10)==0) call pbc(rx,ry,rz,a,b,dt)


call acceleration(ax,ay,az,rx,ry,rz,a,b,dt,pe)

!-------------------------------------------------------------------------------------------------------------



do i=1,a

vx(i)=vx(i)+dt*.5d0*ax(i)*m
vy(i)=vy(i)+dt*.5d0*ay(i)*m
vz(i)=vz(i)+dt*.5d0*az(i)*m

end do


!------------------------------------------------------------------------------------------------------

Ekin=(dot_product(vx,vx)+dot_product(vy,vy)+dot_product(vz,vz))/a

temp1=Ekin/3.d0

open(8,file='temp.dat',status='old',position='append')
write(8,*)dt*m,temp1
close(8)


sumvx=sum(vx)/a
sumvy=sum(vy)/a
sumvz=sum(vz)/a



if (mod(n,100)==0) then



Ekin=(dot_product(vx,vx)+dot_product(vy,vy)+dot_product(vz,vz))/a

sf=sqrt(3.d0*temp/Ekin)

vx=vx*sf
vy=vy*sf
vz=vz*sf

Ekin=0.d0

!(vx-sumvx):fixing centre of mass velocity drift
!sf:velocity rescaling 

sumvx=sum(vx)/a
sumvy=sum(vy)/a
sumvz=sum(vz)/a

do i=1,a
vx(i)=(vx(i)-sumvx)
vy(i)=(vy(i)-sumvy)
vz(i)=(vz(i)-sumvz)
end do









open(7,file='average.dat',status='old',position='append')
write(7,*)sumvx,sumvy,sumvz
close(7)


sumvx=0
sumvy=0
sumvz=0

end if



!---------------------------------------------------------------------------------------

!--------------------------------------------------------------------------------------------------------------


open(4,file='ke.dat',status='old',position='append')
open(6,file='total_energy.agr',status='old',position='append')

Ekin=(dot_product(vx,vx)+dot_product(vy,vy)+dot_product(vz,vz))/a

Ekin=.5*Ekin 
te=pe+Ekin  

write(4,*)dt*m,Ekin
write(6,*)dt*m,te

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


subroutine acceleration(ax,ay,az,rx,ry,rz,a,b,dt,pe)
implicit none
real*8::ax(a),ay(a),az(a),rx(a),ry(a),rz(a),b,dt,pe,rxi,ryi,rzi,axi,ayi,azi
integer::a


do i=1,a

ax(i)=0
ay(i)=0
az(i)=0

end do


potential=0

do i=1,a-1
do j=i+1,a

rxf=rx(i)-rx(j)
ryf=ry(i)-ry(j)
rzf=rz(i)-rz(j)


!minimum image convention


rxf=rxf-b*anint(rxf/b)

ryf=ryf-b*anint(ryf/b)

rzf=rzf-b*anint(rzf/b)

distance=(rxf**2+ryf**2+rzf**2)



if (sqrt(distance) < potcut ) then

sr2=sigma**2/distance
sr6=sr2**3
sr12=sr6**2


force=(48*epsilon*(sr12-0.5*sr6)-fminus)/distance


forcex=force*rxf
forcey=force*ryf
forcez=force*rzf

potential=potential+(sr12-sr6)*4*epsilon-(sqrt(distance)-potcut)*fminus-pminus


ax(i)=ax(i)+forcex    
ax(j)=ax(j)-forcex


ay(i)=ay(i)+forcey
ay(j)=ay(j)-forcey


az(i)=az(i)+forcez
az(j)=az(j)-forcez


end if

end do
end do

open(5,file='potential.dat',status='old',position='append')

write(5,*)dt*m,potential/a 

pe=potential/a






end subroutine acceleration

!-----------------------------------------------------------------------------------------------------------

subroutine pbc(rx,ry,rz,a,b,dt)

implicit none

real*8::rx(a),ry(a),rz(a),b,dt
integer::a

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


end program md
