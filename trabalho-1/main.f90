PROGRAM main
  IMPLICIT NONE

  real :: k
  integer :: i, j
  integer, parameter :: n = 20000
  real, dimension (n,n) :: A
  real, dimension (n,1) :: x, b

  ! Popular x e A com números aleatórios

  do i = 1, n
    call random_number(k)
    x(i,1) = k
  end do

  do i = 1, n
    do j = 1, n
      call random_number(k)
      A(i,j) = k
    end do
  end do

  ! A*x = b
  b = 0.0

  do i = 1, n
    do j = 1, n
      b(i,1) = b(i,1) + A(i,j) * x(j,1)
    end do
  end do



    print*, ""
    print*, "Matriz b:"
    do i = 1, n
      print*, b(i,1)
    end do
 
END PROGRAM main
