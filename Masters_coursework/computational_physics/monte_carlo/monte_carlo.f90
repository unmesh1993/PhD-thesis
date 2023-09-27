program monte_carlo
implicit none
integer::i,iteration,m
real::a,b,sums=0,integrand=0,start,finish
real ::x,f

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
write(*,*)"enter left bound, right bound and then no. of random numbers separated by comma"
read (*,*)a,b,m

do i=1,m
CALL RANDOM_NUMBER(x)
f=4/(1+x**2)
sums=sums+f



end do
integrand=integrand+sums/m
call cpu_time(finish)



write(*,*)"value of integration=",integrand
Write(*,*)"Cpu time in s=",finish-start


end program monte_carlo
