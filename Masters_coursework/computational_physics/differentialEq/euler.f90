program euler
implicit none
real::y,x,y1
real::h,pi=3.141592654
integer::n,i
write(*,*)"step size"
read(*,*)h



n=1.5/h

! euler

x=0
y=0


open(1,file='euler.dat' ,status='old')

do i=1,n+1
if (i>1) then

y=y+(1+(y**2))*h!first derivative

end if


write(1,*)x,y

x=x+h

end do

close(1)


!modified euler



y=0!initial condition
x=0!initial condition

open(1,file='euler.dat' ,status='old',position='append')
write(1,*)"&"

do i=1,n+1
if (i > 1) then

y=y+(0.5*h*(1+y**2+1+(y+h*(1+y**2))**2))!first derivative
x=(i-1)*h
end if

write(1,*)x,y



end do
close (1)


!original solution tan





open(1,file='euler.dat' ,status='old',position='append')
write(1,*)"&"
do i=0,n

x=i*h
y=tan(x)



write(1,*)x,y




end do






end program euler




































