program rungekutta
implicit none
real::y,x,f0,f1,f2,f3,y1,v,k0,k1,k2,k3,l=1,ke
real::h,pi=3.141592654
integer::n,i
write(*,*)"step size"
read(*,*)h



n=20/h

! runge kutta

x=0
y=0
v=0.1


open(1,file='euler.dat' ,status='old')

do i=1,n+1
if (i > 1) then

f0=v
k0=-y

f1=v+h*.5*k0
k1=-(y+h*.5*f0)

f2=v+h*.5*k1
k2=-(y+h*.5*f1)

f3=(v+h*k2)
k3=-(y+h*f2)


y=y+(h/6)*(f0+2*f1+2*f2+f3)
v=v+(h/6)*(k0+2*k1+2*k2+k3)

end if

ke=.5*(y**2)+.5*v*v


write(1,*)x,y

x=x+h

end do

close(1)










!original solution 





open(1,file='euler.dat' ,status='old',position='append')
write(1,*)"&"

do i=0,n
v=0.1
x=i*h
y=(sin(x*l**.5))*(v/l**.5)



write(1,*)x,y




end do






end program rungekutta




































