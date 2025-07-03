program spring
implicit none
real::x,f0,f1,f2,f3,y1,k0,k1,k2,k3,l=1,k=1,rx,ry
real::h,pi=3.141592654,p
real,dimension(:),allocatable::y,v
integer::i,a,j,t,right,left

write(*,*)"number of particles,step size,initialposition"
read(*,*)a,h,p

allocate (y(a))
allocate (v(a))



t=200/h

! runge kutta




open(1,file='movie.xyz' ,status='unknown',form='formatted')
write(1,*)a
write(1,*)'Spring'

do i=1,a
y(i)=0
y(1)=p
rx=5*(cos(2*3.14*i/a))
ry=5*(sin(2*3.14*i/a))

write(1,*)'N',rx,ry,y(i)

end do
close(1)






do i=1,t

open(1,file='movie.xyz' ,status='old',position='append')
write(1,*)a
write(1,*)'Spring'

do j=1,a

if (j==1)then
left=a
else
left=j-1
end if

if (j==a)then
right=1
else
right=j+1
end if

f0=v(j)
k0=-k*(y(left)+y(j)+y(right))

f1=v(j)+h*.5*k0
k1=-k*(y(j)+h*.5*f0)

f2=v(j)+h*.5*k1
k2=-k*(y(j)+h*.5*f1)

f3=(v(j)+h*k2)
k3=-k*(y(j)+h*f2)


y(j)=y(j)+(h/6)*(f0+2*f1+2*f2+f3)
v(j)=v(j)+(h/6)*(k0+2*k1+2*k2+k3)


rx=5*(cos(2*3.14*j/a))
ry=5*(sin(2*3.14*j/a))


write(1,*)'N',rx,ry,y(j)

end do
close(1)
end do



end program spring
