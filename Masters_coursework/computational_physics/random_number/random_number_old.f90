program random_num
implicit none
integer::iteration=0,a,b,i
real*4::x(1000),l(1000),add=0,average,variance,stddeviation



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

read(*,*)a,b!variables user has to enter

do while (iteration<=1000)
CALL RANDOM_NUMBER(x)
iteration=iteration+1
end do

 !generating random velocities in three direction in specified range
l=(b-a)*x+a

!mean and std.dev
do i=1,1000
add=add+l(i)
end do
average=add/1000
 write(*,*)"average=",average
  do i=1,1000
    variance=variance+((l(i)-average)**2)/1000
    end do
    stddeviation=(variance)**.5
    write(*,*)"standard deviation=",stddeviation



open (1, file='test1000.dat',status='old')
do i=1,999
write(1,*) l(i),l(i+1)
end do
close(1)
end program random_num








