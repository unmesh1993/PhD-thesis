program box_muller2
implicit none
integer::i,m
real::x1,sum=0,mean,sum2,mean2,std,finish,start
real, DIMENSION(:), ALLOCATABLE ::x


!clock
call cpu_time(start)

allocate (x(m))


!variables user has to enter
write(*,*)"total no. of random numbers"
read (*,*)m





open (2,file='gaussian_random.dat', status='old')
  do i=1,m
call gaussian(x1)


write(2,*) x1
sum=x1+sum
sum2=sum2+x1*x1

end do
mean=sum/m
mean2=sum2/m
std=(mean2-mean)**.5
write(*,*)"mean=",mean,"standard deviation=",std
close(2)

call cpu_time(finish)




write(*,*)"time taken by cpu in s=",finish-start

contains


Subroutine gaussian(v)
implicit none
real::v,v1,v2,r,l1,l2
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



   20 CALL RANDOM_NUMBER(l1)
    CALL RANDOM_NUMBER(l2)
v1=2*l1-1
v2=2*l2-1

r=v1**2+v2**2
if (r==0 .OR. r>=1) then
goto 20
end if

v=((-2*log(r)/r)**.5)*(v1)

 

end subroutine gaussian

end program box_muller2



