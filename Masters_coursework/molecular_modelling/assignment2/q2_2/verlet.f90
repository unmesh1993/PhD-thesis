program q2
implicit none

real*8::r,g,distance,tolerance,rxf,ryf,rzf,temp,vrms,b,c,Ekin=0,potential=0

real*8::sigma=3.4010,epsilon=.978638,mass=.039948,sr2,sr6,sr12,forcex,forcey,forcez,force,dt,pe,te

!sigma in ang : epsilon in Kj/mol   :mass in Kg/mol  : 1Kj/mol=0.01eV

integer::i,j,k,a,n

real*8,dimension(:),allocatable::rx,ry,rz,trx,try,trz,vx,vy,vz,ax,ay,az

write(*,*)'enter box length(=100) angstrom,number of argon atom (=100),temperature(=300),number of timestep(=500)'
read (*,*)b,a,temp,n



tolerance=1.96!vanderwaal radii of argon



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
open(6,file='total_energy.agr',status='old')
write(6,*)'     '
close(6)


open(5,file='potential.dat',status='old')
write(5,*)'     '
close(5)

open(4,file='ke_drift.dat',status='old')
write(4,*)'     '
close(4)

open(3,file='acceleration.dat' ,status='old')
write(3,*)'     '
close(3)


!--------------------------------------------------------------------------------------------------




open(1,file='position.xyz' ,status='old')
write(1,*)'100'
write(1,*)'Argon_atom'


call random(r)
rx(1)=r
call random(r)
ry(1)=r
call random(r)
rz(1)=r
write(1,*)'Ar',rx(1),ry(1),rz(1)

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

rx(i)=trx(i)   !Ang
ry(i)=try(i)
rz(i)=trz(i)


write(1,*)'Ar',rx(i),ry(i),rz(i)
end do
close(1)


!----------------------------------------------------------------------------------------------


vrms=0.01*((temp*1.3806*6.022)/mass)**.5  !Ang/ps 



open(2,file='velocity.dat',status='old')
write(2,*)'dt=0'

do i= 1,a


call gaussian(g)
vx(i)=vrms*g

call gaussian(g)
vy(i)=vrms*g

call gaussian(g)
vz(i)=vrms*g


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

open(2,file='velocity.dat',status='old',position='append')
write(2,*)'dt=',(dt-.5)

do i=1,a

rx(i)=rx(i)+dt*vx(i)+dt*dt*.5*ax(i)
ry(i)=ry(i)+dt*vy(i)+dt*dt*.5*ay(i)
rz(i)=rz(i)+dt*vz(i)+dt*dt*.5*az(i)

vx(i)=vx(i)+dt*.5*ax(i)
vy(i)=vy(i)+dt*.5*ay(i)
vz(i)=vz(i)+dt*.5*az(i)



write(2,*)i,vx(i),vy(i),vz(i)

end do
close(2)

!-----------------------------------------------------------------------------------------------------------




call pbc(rx,ry,rz,a,b,dt)



!------------------------------------------------------------------------------------------------------------


call acceleration(ax,ay,az,rx,ry,rz,a,b,dt,tolerance,pe)


!-------------------------------------------------------------------------------------------------------------


open(2,file='velocity.dat' ,status='old',position='append')
write(2,*)'dt=',dt

do i=1,a

vx(i)=vx(i)+dt*.5*ax(i)
vy(i)=vy(i)+dt*.5*ay(i)
vz(i)=vz(i)+dt*.5*az(i)

write(2,*)i,vx(i),vy(i),vz(i)

Ekin=Ekin+(vx(i)**2+vy(i)**2+vz(i)**2)
end do

close(2)

open(4,file='ke_drift.dat',status='old',position='append')
open(6,file='total_energy.agr',status='old',position='append')

Ekin=.5*0.1*mass*Ekin/a  !eV
te=pe*0.01+Ekin  !eV

write(4,*)dt,Ekin
write(6,*)dt,te

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

if (distance > tolerance**2) then !potential truncation-consequence of mbc

sr2=sigma**2/distance
sr6=sr2**3
sr12=sr6**2



potential=potential+(sr12-sr6)*4*epsilon   ! KJ/mol


force=48*epsilon*(sr12-0.5*sr6)/distance   ! KJ/mol Ang2

forcex=force*rxf    ! KJ/mol Ang
forcey=force*ryf
forcez=force*rzf

ax(i)=ax(i)+(0.1*forcex/mass)   ! Ang/ps2
ax(j)=ax(j)-(0.1*forcex/mass)


ay(i)=ay(i)+(0.1*forcey/mass)
ay(j)=ay(j)-(0.1*forcey/mass)


az(i)=az(i)+(0.1*forcez/mass)
az(j)=az(j)-(0.1*forcez/mass)

elseif (distance <= tolerance**2) then

potential=potential

ax(i)=ax(i)
ay(i)=ay(i)
az(i)=az(i)



end if

end do

end do

open(5,file='potential.dat',status='old',position='append')

write(5,*)dt,potential/a !potential in kJ/mol

pe=potential/a
potential=0




open(3,file='acceleration.dat' ,status='old',position='append')
write(3,*)'dt=',dt

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


open(1,file='position.xyz' ,status='old',position='append')
write(1,*)'100'
write(1,*)'Argon_atom'


do i=1,a

write(1,*)'Ar',rx(i),ry(i),rz(i)
end do

close(1)

end subroutine pbc


end program q2
