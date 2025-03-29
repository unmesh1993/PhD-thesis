program pwell
implicit none

Real*8::a,b,pi,v0
integer::n,i,j,info,num,lwork,nr
real*8,dimension(:),allocatable::k,eigen,work
real*8,dimension(:,:),allocatable::h

real*8 ::x,dx,norm,prob
complex*8 ::f


!--------------------------------------------------------------------------------------------------------

write(*,*)'potential of the well(V0)'
read(*,*)v0

write(*,*)'width of well(b)'
read(*,*)b

write(*,*)'periodicity and number of plane wave'
read(*,*)a,num

pi=3.14159265358979323846264338327d0
n=2*num+1





!---------------------------------------------------------------------------------------------------------


allocate(h(n,n),k(n),eigen(n),work(3*n))


!---------------------------------------------------------------------------------------------------------


k(1)=0.d0

do i=2,n-1,2

k(i)=.5d0*dfloat(i)*2.d0*pi/a
k(i+1)=(-.5d0)*dfloat(i)*2.d0*pi/a

end do

!----------------------------------------------------------------------------------------------------------

! here i=basis function index j=eigen value index

do i=1,n
do j=1,n

if (i==j) then

h(i,j)=k(i)**2.d0-v0*b/a

else

h(i,j)=-v0/a*sin((k(j)-k(i))*b/2.d0)/(k(j)-k(i))*2.d0

end if

end do
end do

!-------------------------------------------------------------------------------------------------------------

lwork=3.d0*n


call dsyev ('V','U',n,h,n,eigen,work,lwork,info)


if (info /= 0) stop 'matrix not diagonisable'

open(1,file='eigen_value.dat', status='unknown', form='formatted')

do i=1,n
write(1,*)i,eigen(i)
end do

open(2,file='eigen_vectors.dat', status='unknown', form='formatted')
do i=1,n
do j=1,n

write(2,*)h(j,i)

end do 
end do




write(*,*) eigen(1), eigen(2), eigen(n)




!---------------------------------------------------------------------------------------------------------------------

end program pwell



!-------------------------------------------------------------------------------------------------------------------








