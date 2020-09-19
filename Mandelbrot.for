program Mandelbrot
use types, only: dp
use constants, only: I
use utils, only: savetxt, linspace, meshgrid
implicit none

integer, parameter :: ITERATIONS = 100
integer, parameter :: DENSITY = 1000
real(dp) :: x_min, x_max, y_min, y_max
real(dp), dimension(DENSITY, DENSITY) :: x, y
complex(dp), dimension(DENSITY, DENSITY) :: c, z
integer, dimension(DENSITY, DENSITY) :: fractal
integer :: n
x_min = -2.68_dp
x_max = 1.32_dp
y_min = -1.5_dp
y_max = 1.5_dp

call meshgrid(linspace(x_min, x_max, DENSITY), &
    linspace(y_min, y_max, DENSITY), x, y)
c = x + I*y
z = c
fractal = 255

do n = 1, ITERATIONS
    print "('Iteration ', i0)", n
    where (abs(z) <= 10) z = z**2 + c
    where (fractal == 255 .and. abs(z) > 10) fractal = 254 * (n-1) / ITERATIONS
end do

print *, "Saving..."
call savetxt("fractal.dat", log(real(fractal, dp)))
call savetxt("coord.dat", reshape([x_min, x_max, y_min, y_max], [4, 1]))
end program



module find_fit_module
use minpack, only: lmdif1
use types, only: dp
implicit none
private
public find_fit

contains

subroutine find_fit(data_x, data_y, expr, pars)
real(dp), intent(in) :: data_x(:), data_y(:)
interface
    function expr(x, pars) result(y)
    use types, only: dp
    implicit none
    real(dp), intent(in) :: x(:), pars(:)
    real(dp) :: y(size(x))
    end function
end interface
real(dp), intent(inout) :: pars(:)

real(dp) :: tol, fvec(size(data_x))
integer :: iwa(size(pars)), info, m, n
real(dp), allocatable :: wa(:)

tol = sqrt(epsilon(1._dp))
m = size(fvec)
n = size(pars)
allocate(wa(m*n + 5*n + m))
call lmdif1(fcn, m, n, pars, fvec, tol, info, iwa, wa, size(wa))
if (info /= 1) stop "failed to converge"

contains
ftyuj
subroutine fcn(m, n, x, fvec, iflag)
integer, intent(in) :: m, n, iflag
real(dp), intent(in) :: x(n)
real(dp), intent(out) :: fvec(m)
! Suppress compiler warning:
fvec(1) = iflag
fvec = data_y - expr(data_x, x)
end subroutine

end subroutine

end module


contains
ftyuj
subroutine fcn(m, n, x, fvec, iflag)
integer, intent(in) :: m, n, iflag
real(dp), intent(in) :: x(n)
real(dp), intent(out) :: fvec(m)
! Suppress compiler warning:
fvec(1) = iflag
fvec = data_y - expr(data_x, x)
end subroutine

end subroutine

end module
