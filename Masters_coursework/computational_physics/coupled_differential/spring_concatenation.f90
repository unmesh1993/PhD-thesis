program euler
implicit none

integer,parameter :: nop=50
integer :: niter,i, dx1000,kk,kkp1,kkn1
real*8 :: init_t,inity(nop),init_vel(nop)
real*8 :: yim(nop),vim(nop),y_temp,v_temp
real*8,parameter :: km=1.0d0, mass=1.0d0
real*8  :: dt,t,dtby2,ke,pe,zpos,twopi,r,theta(nop)
real*8  :: f0(nop),f1(nop),f2(nop),f3(nop),f0v(nop),f1v(nop),f2v(nop),f3v(nop)
real*8  :: y1(nop),y2(nop),y3(nop),v1(nop),v2(nop),v3(nop),force(nop)
character(len=30) :: charac_a,charac_e,charac_m,charac_i ! charac_b stores the name dump_pos

charac_m = 'x_energy_vi1.8_dt_'
charac_i = 'kx_coor_dt_'

! PARAMETER DEFINITION
niter = 2000; init_t = 0.0d0; inity =0.0d0; init_vel= 0.1d0; dt = 0.02d0

dx1000 = int(dt*1000.d0); dtby2 = dt/2.0d0

! INITIALIZATION OF POSITION AND VELOCITY.
t=init_t


yim(1) =0.8d0
!vim(1) = init_vel

! OTHER VARIABLES ! TO ARRANGE PARTICLES IN A RING.
zpos = 0.0d0; r =5.0d0; twopi = 4.0*asin(1.0d0)
 do i = 1,nop
 theta(i) = dfloat(i)*twopi/dfloat(nop)
! vim(i) = 0.2d0*sin(dfloat(i)*twopi/dfloat(nop))
 enddo

do i=1,nop
!yim(i) = 0.2d0*sin(1.0*theta(i))
!vim(i) = 0.2d0*cos(1.0*theta(i))
enddo

charac_a = charac_m
call addnumtostring(charac_a,dx1000)
open(080,file=charac_a,status='unknown',form='formatted')


!   write(*,*)'ke',vim*vim,km*yim*yim

do i = 1,niter
   t = t + dt

   do kk=1,nop
      kkp1 = kk+1; kkn1=kk-1 ! IDENTIFY NEIGHBOURS.
      if(kk.eq.1) kkn1 = nop
      if(kk.eq.nop) kkp1 = 1
   
      f0(kk) = vim(kk) ! dx/dt = v
      f0v(kk) = km*(yim(kkp1) + yim(kkn1) - 2.0d0*yim(kk)) ! dv/dt = -k y
   enddo

! Calculate variables y and v at time  t + dt/2 
    
   do kk=1,nop
      y1(kk) = yim(kk) + f0(kk)*dtby2; v1(kk) = vim(kk) + f0v(kk)*dtby2
   enddo

   do kk=1,nop
      kkp1 = kk+1; kkn1=kk-1 ! IDENTIFY NEIGHBOURS.
      if(kk.eq.1) kkn1 = nop
      if(kk.eq.nop) kkp1 = 1
   
      f1(kk) = v1(kk); f1v(kk) = km*(y1(kkp1) + y1(kkn1) - 2.0d0*y1(kk))
   enddo
! Calculate variables y and v at time  t + dt/2 : more accurate value.
   do kk=1,nop
      y2(kk) = yim(kk) + dtby2*f1(kk); v2(kk) = vim(kk) + dtby2*f1v(kk)
   enddo

   do kk=1,nop
      kkp1 = kk+1; kkn1=kk-1 ! IDENTIFY NEIGHBOURS.
      if(kk.eq.1) kkn1 = nop
      if(kk.eq.nop) kkp1 = 1
   
      f2(kk) = v2(kk) ; f2v(kk) = km*(y2(kkp1) + y2(kkn1) - 2.0d0*y2(kk))
   enddo
! Calculate variables y and v at time  t + dt: using f2(t+ dt/2)
   do kk=1,nop
      y3(kk) = yim(kk) + dt*f2(kk); v3(kk) = vim(kk) + dt*f2v(kk)
   enddo

   do kk=1,nop
      kkp1 = kk+1; kkn1=kk-1 ! IDENTIFY NEIGHBOURS.
      if(kk.eq.1) kkn1 = nop
      if(kk.eq.nop) kkp1 = 1
   
      f3(kk) = v3(kk); f3v(kk) = km*(y3(kkp1) + y3(kkn1) - 2.0d0*y3(kk))
   enddo

   yim = yim + dt*(f0 + 2.0d0*f1 + 2.0d0*f2 + f3)/6.0d0
    force = (f0v + 2.0d0*f1v + 2.0d0*f2v + f3v)/6.0d0
   vim = vim + dt*(f0v + 2.0d0*f1v + 2.0d0*f2v + f3v)/6.0d0

!    write(*,*) sum(force),sum(vim)

   ke=0.0d0;pe=0.0d0  ! SET KE, PE =0

    do kk=1,nop
        kkp1 = kk+1; kkn1=kk-1 ! IDENTIFY NEIGHBOURS.
        if(kk.eq.1) kkn1 = nop
        if(kk.eq.nop) kkp1 = 1

        ke = ke + mass*0.5*vim(kk)*vim(kk) 
  !  NOTE 0.25 FACTOR AS  0.5 kx^2 for a PAIR OF particles. 
        pe = pe + km*0.25*( (yim(kkp1)-yim(kk))**2 + (yim(kkn1)-yim(kk))**2 ) 
    enddo
    write(80,fmt='(9g25.15)') t,ke+pe,ke,pe ! WRITE DOWN KE AND PE


    if(mod(i,10)==0) then ! EVERY 10 STEPS PRINT POSITIONS TO MAKE A MOVIE
      charac_a = charac_i
!      call addnumtostring(charac_a,dx1000)
      call addnumtostring(charac_a,i) 
      open(081,file=charac_a,status='unknown',form='formatted')
         do kk=1,nop
          write(081,'(A,3g25.15)') 'N',r*cos(theta(kk)),r*sin(theta(kk)),yim(kk)
!          write(081,'(A,3g25.15)') 'N',dfloat(kk)+yim(kk),1.0d0,1.0d0
         enddo
      close(81)
    endif


enddo

close(80)
!close(79)

stop
end program euler

!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
subroutine addnumtostring(string,number)
implicit none
integer :: i,strlen,number,nodig,num,snum
character*(*) ::  string

      snum=number
      do i=len(string),1,-1
       if (string(i:i) .ne. ' ') goto 10
      enddo
   10 strlen=i


        nodig=int(log10(1.0*snum+0.1))+1
        do i=nodig,1,-1
       num=snum/10**(i-1)
       string(strlen+1:strlen+1)=char(48+num)
       strlen=strlen+1
       snum=snum-num*10**(i-1)
        enddo

        return
end subroutine addnumtostring


