program sorting
implicit none


integer, dimension(:), allocatable :: x
      integer :: n,i,j,temp
 open (unit=99, file='data_set.dat', status='old', action='read')
 read(99, *), n
 allocate(x(n))
 read(99,*) x
do i=1,n   
do j=i+1,n
  if(x(i)>x(j))then 
    temp=x(i)
    x(i)=x(j)
    x(j)=temp
    end if
      end do
end do
 
open(2, file='data_new.dat', status='repalce',action='write')
write(2,*)x

close(99)
close(2)



 

end program sorting
