program trapezoidal
integer::i,iteration,m
real::a,b,sumc=0,integrand,start,finish
real ::kx,x

! variables for random seed setting 
  INTEGER :: i_seed
  INTEGER, DIMENSION(:), ALLOCATABLE :: a_seed
  INTEGER, DIMENSION(1:8) :: dt_seed
  !end of variables for seed setting 
!clock
call cpu_time(start)
  

 ! Set up random seed
  CALL RANDOM_SEED(size=i_seed)
  ALLOCATE(a_seed(1:i_seed))
  CALL RANDOM_SEED(get=a_seed)
  CALL DATE_AND_TIME(values=dt_seed)
  a_seed(i_seed)=dt_seed(8); a_seed(1)=dt_seed(8)*dt_seed(7)*dt_seed(6)
  CALL RANDOM_SEED(put=a_seed)
  DEALLOCATE(a_seed)
  ! Done setting up random seed

!variables user has to enter
write(*,*)"enter left bound, right bound and then no. of random numbers all separated by comma"
read (*,*)a,b,m

do i=1,m

CALL RANDOM_NUMBER(kx)


!arrays in specified range

x=(b-a)*kx+a

f=4/(1+x**2)

sumc=sumc+f

end do

integrand=(2*sumc+4/(1+a**2)+4/(1+b**2))*((b-a)/(2*m))

call cpu_time(finish)


write(*,*)"value of integration=",integrand

write(*,*)"time taken by cpu in s=",finish-start

end program trapezoidal
