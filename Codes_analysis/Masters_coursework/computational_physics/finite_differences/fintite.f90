program finite
implicit none
real*8::h,c1,c2,c3,c4,yy,x,tolerance=5*10**(-4)
integer::iteration,n,i,j
real*8,dimension(:),allocatable::y

write(*,*)'number of iteration,stepsize'
read(*,*)iteration,h

n=1/h

allocate (y(n+1))



do i=1,n+1
y(i)=(100.d0/n)*(i-1)
end do

c1=1.d0-2.5d0*h
c2=1.d0+2.5d0*h
c3=-10.d0*h*h
c4=2.d0+c3


do i =1,iteration

x=0.d0

do j=2,n

x=x+h

yy=(c1*y(j+1)+c2*y(j-1)+c3*x)/c4

if (abs((yy-y(j))/yy) > tolerance ) then

y(j)=yy


end if

end do
 
end do

open(1,file='haha.dat',status='unknown',form='formatted')
do i=1,n+1
write(1,*)(i-1)*h,y(i)
end do

end program finite




