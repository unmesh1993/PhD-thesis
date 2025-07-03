program pi_circle
implicit none
integer::iteration=0,a,b,m
real::pi,kx,ky,ncircle,x,y,k=0




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
write(*,*)"no. of random numbers"
read(*,*)m



do while (iteration<=m)
CALL RANDOM_NUMBER(kx)
CALL RANDOM_NUMBER(ky)
x=2*kx-1
y=2*ky-1
ncircle=x**2+y**2
if (ncircle <= 1)then
k=k+1
end if	
iteration=iteration+1
end do
write(*,*)"number of points in the circle",k

pi=(k*4)/m


write(*,*)"pi",pi




!area of circle
end program pi_circle








