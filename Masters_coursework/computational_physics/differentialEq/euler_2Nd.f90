program euler
implicit none
real::y,x,v,k=1,y1,v1,ke
real::h,pi=3.141592654
integer::n,i
write(*,*)"step size"
read(*,*)h



n=20/h

! euler


open(1,file='euler.dat' ,status='old',position='append')

y=0!initial condition
x=0!initial condition
v=0.1!initial condition

do i=1,n
if (i > 1) then
y1=y+v*h!first derivative
v1=v+h*(-k*y)
y=y1
v=v1

x=(i-1)*h
end if

ke=.5*y*y+.5*v*v

write(1,*)x,y
!write(1,*)x,y



end do

close(1)


!modified euler





open(1,file='euler.dat' ,status='old',position='append')
write(1,*)"&"

y=0!initial condition
x=0!initial condition
v=0.1!initial condition

do i=1,n
if (i > 1) then
y1=y+0.5*h*(v+v+h*(-k*y))
v1=v+(0.5*h*(-k*y-k*y1))
y=y1
v=v1
end if

ke=.5*y*y+.5*v*v

write(1,*)x,y
x=x+h



end do
close (1)


!original solution 





open(1,file='euler.dat' ,status='old',position='append')
write(1,*)"&"

do i=0,n
v=0.1
x=i*h
y=(sin(x*k**.5))*(v/k**.5)



write(1,*)x,y




end do






end program euler
