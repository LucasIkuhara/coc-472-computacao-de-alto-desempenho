PROGRAM main
  IMPLICIT NONE

  real :: k
  integer :: i, j
  character(100) :: nAsChar
  real, allocatable, dimension (:, :) :: A
  real, allocatable, dimension (:, :) :: x, b
  integer :: n
  
  ! Ler N da chamada do programa
  CALL GET_COMMAND_ARGUMENT(1,nAsChar)
  READ(nAsChar,*)n
  
  ! Alocar vetores com os tamanhos lidos
  allocate(A(n,n))
  allocate(x(n,1))
  allocate(b(n,1))

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

  print*, b(1,1)    
 
END PROGRAM main
