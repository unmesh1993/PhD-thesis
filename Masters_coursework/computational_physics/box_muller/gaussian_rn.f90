program box_muller
implicit none
integer::i,m
real::a,b,sumc=0,integrand=0,x1,x2,x3,y1,y2,y3,z1,z2,z3,zz,f,start,finish

!clock
 call cpu_time(start)


!variables user has to enter
write(*,*)"total no. of random numbers"
read (*,*)m



do i=1,m
call gaussian(x1) 
call gaussian(x2)
call gaussian(x3)
call gaussian(y1)
call gaussian(y2)
call gaussian(y3)

z1=y1-x1
z2=y2-x2
z3=y3-x3
zz=z1**2+z2**2+z3**2

f=(3.1415**3)*exp(-zz/2)
sumc=sumc+f
end do
integrand=sumc/m
call cpu_time(finish)
write(*,*)"value of integration=",integrand
Write(*,*)"Cpu time in s=",finish-start


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

v=((-1*log(r)/r)**.5)*(v1)

end subroutine gaussian

end program box_muller






