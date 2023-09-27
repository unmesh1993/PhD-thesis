program tanvalue 
implicit none
real::x=0,y,h
integer::i,n
write(*,*)"no. of points"
read(*,*)n

h=2/n
open(1,file='euler.dat' ,status='old')

do i=1,n

y=tan(x)
write(1,*)x,y
x=x+h
end do

end program tanvalue


