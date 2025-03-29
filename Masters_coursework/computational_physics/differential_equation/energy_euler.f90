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


n=30/h

!euler for pendulum_d20/dt2=-(g/l)sin0

open(1,file='pendulum.dat' ,status='old')


x=0!initial condition
y=theta
v=omega


do i=1,n+1
if (i > 1) then
y1=y+v*h!first derivative
v1=v+h*(-kc*sin(y))
y=y1
v=v1
end if


!write(1,*)x,y

pe=mass*g*l*(1-cos(y))
ke=.5*mass*(l**2)*v**2

te=pe+ke
write(1,*)x,te


!write(1,*)x,y,x,v

x=x+h

end do

close(1)



end program pendulum
