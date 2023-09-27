program monte_carlo2
integer::i,iteration,m
real::a,b,sumc=0,integrand,start,finish
real ::kx1,kx2,kx3,ky1,ky2,ky3,xx,yy,f,x1,x2,x3,y1,y2,y3,z1,z2,z3,zz

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
CALL RANDOM_NUMBER(kx1)
CALL RANDOM_NUMBER(kx2)
CALL RANDOM_NUMBER(kx3)
CALL RANDOM_NUMBER(ky1)
CALL RANDOM_NUMBER(ky2)
CALL RANDOM_NUMBER(ky3)



!arrays in specified range

x1=(b-a)*kx1+a
x2=(b-a)*kx2+a
x3=(b-a)*kx3+a
y1=(b-a)*ky1+a
y2=(b-a)*ky2+a
y3=(b-a)*ky3+a
z1=x1-y1
z2=x2-y2
z3=x3-y3
zz=z1**2+z2**2+z3**2


xx=x1**2+x2**2+x3**2
yy=y1**2+y2**2+y3**2

f=exp((-xx-yy-zz/2))
sumc=sumc+f

end do

integrand=(sumc/m)*((b-a)**6)

call cpu_time(finish)


write(*,*)"value of integration=",integrand

write(*,*)"time taken by cpu in s=",finish-start

end program monte_carlo2
