program random_num
implicit none
integer::iteration=0,a,b,i,m,j,k
real::add=0,average,variance,stddeviation,sumc=0,averagecorr
real, DIMENSION(:), ALLOCATABLE ::x,l,corrcoeff



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


!variables user has to enter
write(*,*)"enter left bound, right bound and then no. of random numbers separated by comma"
read (*,*)a,b,m

allocate (x(m))
allocate (l(m))

do while (iteration<=m)
CALL RANDOM_NUMBER(x)
iteration=iteration+1
end do

 !generating random numbers in specified range
l=(b-a)*x+a
deallocate(x)


!average 
do i=1,m
add=add+l(i)
end do
average=add/m
 write(*,*)"average=",average



!standard deviation  
do i=1,m
variance=variance+((l(i)-average)**2)/m
end do
stddeviation=(variance)**.5
write(*,*)"standard deviation=",stddeviation





! degree of correlation coeffiecient
allocate (corrcoeff(m-1))

do k=1,m-1
sumc=0
do i=1,m-k
sumc=sumc+l(i)*l(i+k)
end do
averagecorr=sumc/(m-k)
corrcoeff(k)=(averagecorr-average**2)/(variance-average**2)
end do

!degree of correlation plot
open(3,file='degreecorr.dat', status='unknown',form='formatted')
do i=1,m-1
write(3,*)i,corrcoeff(i)
end do
close(3)

deallocate(corrcoeff)



!correlation plot
open (1, file='test.dat',status='unknown',form='formatted')
do i=1,m-1
write(1,*) l(i),l(i+1)
end do
close(1)

!average and std deviation plot

open (2,file='avg_stdD.dat', status='unknown',form='formatted')
write(2,*) "number of random number=",m
write(2,*) '',m,'average=',average
write(2,*) '',m,'standard deviation=',stddeviation
close(2)

end program random_num








