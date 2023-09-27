program ising
implicit none
integer::i,j,k,a,b,c,energyi=0,lai,laf,lbi,lbf,lci,lcf,sums=0,intenergy=0,m=0,spin
real::x
real, DIMENSION(:,:,:), ALLOCATABLE ::s


!variables user has to enter
write(*,*)"dimension a,b,c and spin"
read (*,*)a,b,c,spin


allocate (s(a,b,c))





do i=1,a
do j=1,b
do k=1,c


s(i,j,k)=spin
m=m+s(i,j,k) 
end do
end do
end do

!x dimension
do i=1,a


if (i==a) then
laf=1
else
laf=i+1
end if

if (i==1) then
lai=a
else
lai=i-1
end if

!y dimension

do j=1,b


if (j==b) then
lbf=1
else
lbf=j+1
end if

if (j==1) then
lbi=b
else
lbi=j-1
end if

!z dimension
do k=1,c

if (k==c) then
lcf=1
else
lcf=k+1
end if

if (k==1) then
lci=c
else
lci=k-1
end if


sums=s(lai,j,k)+s(i,lbi,k)+s(i,j,lci)+s(laf,j,k)+s(i,lbf,k)+s(i,j,lcf)

energyi=energyi+sums*(-s(i,j,k))
intenergy=energyi/2
end do
end do
end do

write(*,*)intenergy/(a*b*c),m/(a*b*c)



















contains


Subroutine random(l)
implicit none
real::l
! variables for random seed setting 
  INTEGER :: i_seed
  INTEGER, DIMENSION(:), ALLOCATABLE :: a_seed
  INTEGER, DIMENSION(1:8) :: dt_seed
  !end of variables for seed setting 


 ! Set up random seed
  CALL RANDOM_SEED(size=i_seed)
  ALLOCATE(a_seed(1:i_seed))
  CALL RANDOM_SEED(get=a_seed)
  CALL DATE_AND_TIME(values=dt_seed)
  a_seed(i_seed)=dt_seed(8); a_seed(1)=dt_seed(8)*dt_seed(7)*dt_seed(6)
  CALL RANDOM_SEED(put=a_seed)
  DEALLOCATE(a_seed)
  ! Done setting up random seed 

CALL RANDOM_NUMBER(l)

end subroutine random

end program ising



