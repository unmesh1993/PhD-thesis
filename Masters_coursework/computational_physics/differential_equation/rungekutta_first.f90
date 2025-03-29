program rungekutta
implicit none
real::y,x,f0,f1,f2,f3,y1
real::h,pi=3.141592654
integer::n,i
write(*,*)"step size"
read(*,*)h



n=(3.14/2)/h

! runge kutta

x=0
y=0


open(1,file='euler.dat' ,status='old')

do i=1,n+1
if (i > 1) then

f0=1+y**2

f1=1+(y+h*.5*f0)**2

f2=1+(y+h*.5*f1)**2

f3=1+(y+h*f2)**2


y=y+(h/6)*(f0+2*f1+2*f2+f3)

end if


write(1,*)x,y

x=x+h

end do

close(1)




!original solution tan





open(1,file='euler.dat' ,status='old',position='append')
write(1,*)"&"
do i=0,n

x=i*h
y=tan(x)



write(1,*)x,y




end do






end program rungekutta




































