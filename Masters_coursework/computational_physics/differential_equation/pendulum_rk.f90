program pendulum
implicit none
real::y,x,f0,f1,f2,f3,y1,v,v1,k0,k1,k2,k3,l,theta,omega,kc,pe,ke,te,mass
real::h,pi=3.141592654,g=9.8
integer::n,i
write(*,*)"step size,int.theta,int.omega,length of the pendulum,mass of pendulum "
read(*,*)h,theta,omega,l,mass

!angular frequency is v
!angular displacement is y
!time is t


kc=g/l


n=100/h

! runge kutta for pendulum_d20/dt2=-(g/l)sin0

open(1,file='pendulum.dat' ,status='old')


x=0!initial condition
y=theta
v=omega

do i=1,n+1
if (i > 1) then

f0=v
k0=-kc*sin(y)

f1=v+h*.5*k0
k1=-kc*sin(y+h*.5*f0)

f2=v+h*.5*k1
k2=-kc*sin(y+h*.5*f1)

f3=(v+h*k2)
k3=-kc*sin(y+h*f2)


y=y+(h/6)*(f0+2*f1+2*f2+f3)
v=v+(h/6)*(k0+2*k1+2*k2+k3)

end if

pe=mass*g*l*(1-cos(y))
ke=.5*mass*(l**2)*v**2

te=pe+ke
!write(1,*)x,te


write(1,*)x,y

x=x+h

end do

close(1)

! runge kutta for pendulum_d20/dt2=-(g/l)sin0

open(1,file='pendulum.dat' ,status='old',position='append')
write(1,*)'&'


x=0!initial condition
y=theta
v=omega

do i=1,n+1
if (i > 1) then

f0=v
k0=-kc*sin(y)

f1=v+h*.5*k0
k1=-kc*sin(y+h*.5*f0)

f2=v+h*.5*k1
k2=-kc*sin(y+h*.5*f1)

f3=(v+h*k2)
k3=-kc*sin(y+h*f2)


y=y+(h/6)*(f0+2*f1+2*f2+f3)
v=v+(h/6)*(k0+2*k1+2*k2+k3)

end if

pe=mass*g*l*(1-cos(y))
ke=.5*mass*(l**2)*v**2

te=pe+ke
!write(1,*)x,te


write(1,*)x,v

x=x+h

end do

close(1)



end program pendulum
