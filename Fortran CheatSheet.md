# template CheatSheet
Cheat Sheet for Fortran programming language, created by Guangzhi.
Modified by Christian Toderascu.

**last update: 20240205**

last update available on [GitHub - Fortran CheatSheet.md](https://github.com/Todochris/CheatSheets/blob/main/Fortran%20CheatSheet.md)  
[link of the source](https://numbersmithy.com/fortran-cheat-sheet/)



# Fortran cheat sheet – Number-Smithy
Program template
----------------

```
program program_name
implicit none

! program body

end program program_name

```


Case insensitive
----------------

Line continuation
-----------------

Use `&` at the end and at the beginning to break a long line into 2. E.g.

```
real, dimension (1:16) :: pad1 = (/ 1, 2, 3, 4, &
  & 5, 6, 7, 8 /)

```


Declare variable
----------------

```
real :: var1,x,y

```


integer type
------------

`huge()` gives the largest number that can be held by the specified integer type. E.g.

```
integer :: largeval
print *, huge(largeval)

```


To specify the number of bytes, use `kind` specifier:

```
integer(kind=2) :: shortvar
integer(kind=8) :: longvar

```


logical type
------------

`.TURE.`, `.FALSE.`

Complex type
------------

`cx = 1.0 + 2.0i` `cx = cmplx(1.0, 2.0)`

Custom type
-----------

### To define a custom type:

```
type :: type_name
    integer :: id
    integer :: age
    character(len=50) :: name
    character(len=2) :: sex
end type

```


The double `::` in `type :: type_name` is optional.

### To declare a custom type variable:

```
type(type_name) :: var1

```


### To assign values:

```
var1%id=1
var1%age=20
var1="mark"
var1%sex="M"

```


or

```
var1=type_name(1,20,"mark","M")

```


### To access a field:

```
var1%field_name

```


### To create an array of custom types:

```
type(type_name), dimension(10) :: type_array

```


### To access an element:

```
type_array(2)%fieldname

```


Print string
------------

```
print *, 'This is a string.'
print *, "The answer is ", answer

```


or

```
write(*,*) "new string."

```


where `*` is for the default output option (screen).

Format output
-------------

### Integer and real number specification

syntax:

```
write(output_device, label) vars label format_spec

```


E.g.

```
integer :: num1, num2
write(*,1) num1 1 format(2i10)
write(*,2) num2 2 format(f6.2)

```


Another general form:

```
read (unit=u, fmt=fmt) variable_list
write (unit=u, fmt=fmt) variable_list

```


where `fmt` is formatting string. E.g. `(i3,f6.4)`. `u` is a unit number, a number associated with a file.

E.g.

```
write(*,"(i10.2)") number

```


*   `*`: output device is screen.
*   `2i10`: right justified integer, <= 10 digits, 2 digits per line.
*   `f6.2`: no more than 6 digits in total (including sign if there is one and decimal point), 2 decimal places.
*   `i10.2`: <= 10 digits, >= 2 digits.

### Exponential specification

`nEm.d`:

*   `d`: number of decimal places.
*   `m`: total width (including sign if any, E and its sign, decimal point and all numbers).
*   `n`: number of exponential numbers per line.

E.g.

```
format(2E14.5)

```


### Character specification

`nAm`

*   `m`: max number of characters.
*   `n`: number of strings per line.

E.g. `format(2a10)`

### Print new line in formatted output

Use `//` in the format string:

```
write(*,"(i3//i3)") 10, 10

```


### Print spaces in formatted output:

Use `nx` in format string, `n` is the number of spaces. E.g.

```
write(*,"(A,2x,A,2x,A,i3)") 'name', trim(tt), 'length', tt%length

```


The output looks like:

> name mark length 5

### More on formatted I/O

Input
-----

```
read *, x
read *, y

```


Character variables
-------------------

### To declare a character variable with a max length:

```
character :: var*10

```


or

```
character (len=10) :: var
character(10) :: var
character(len=*) :: var    ! unknown length

```


### To get substring, use indexing:

```
var(1:4)

```


Both ends included.

### To concatenate characters, use `//`:

```
name=title//firstname//surname

```


### Some string functions

*   `len(str)`: length.
*   `len_trim(str)`: length after removing trailing blanks.
*   `index(str,substr)`: find index location of a substring. Return 0 if not found.
*   `achar(int)`: convert an integer to a character. E.g. 65->A, 90->Z.
*   `ichar(c)`: convert a character to an integer.
*   `trim(str)`: remove trailing blanks (similar as `rstrip()` in python).
*   `scan(str,chars)`: find the index location of the 1st occurrence of `chars`. Return 0 if not found.
*   `verify(str,chars)`: find the 1st occurrence of any character not contained in `chars`. Return 0 if only the characters in `chars` have been found.
*   `repeat(str,n)`: repeat `str` by `n` times.
*   `adjusl(str)`: remove leading blanks, and append them to the end.
*   `adjustr(str)`: remove trailing blanks, and insert at the front.

Named constants
---------------

Define constants use the `parameter` keyword:

```
real, parameter :: pi = 3.1415

```


Power (same as in python)
-------------------------

`=10**2=`

Common math functions
---------------------

**NOTE** that input args should be real or complex, e.g. sin(10.0) rather than sin(10).

sin(x), cos(x), tan(x), atan(x), abs(x), sqrt(x), exp(x), log10(x) floor(x), int(x).

`nint(x)`: round to nearest integer. `mod(a,p)`: remainder of a/p.

if block
--------

```
if (expression) then
    ...
else if (expression) then
    ...
else
    ...
end if

```


Simpler if statement
--------------------

```
if (num <0) stop
if (num <10) print *, "less than 10"
if (num >10) print *, "> 10"

```


Logical operators
-----------------

*   \== or .eq.
    
*   /= or .ne.
    
*   > or .gt.
    
*   > \= or .ge.
    
*   < or .lt.
    
*   <= .le.
    
*   *   or .not.
*   .and.
    
*   .or.
    
    if (x>y .and. y>z) then … end if
    

stop
----

`stop`: stops the program.

pause
-----

Pause the program, until user hit Enter.

Integer division
----------------

Same as Python2, need to involve one real to get real division result. E.g.

```
integer :: x
real :: y
x=1
y=x/3   ! gives 0.00000
y=x/3.0 ! gives 0.33333

```


do loop
-------

```
do i=start,stop[,step]
   ...
end do

```


E.g.

```
do i=0,20
  print *, i
end do

do i=5,-5,-2
  print *, i
end do

```


exit: same as break
-------------------

cycle: same as continue
-----------------------

Named do loop
-------------

When need to nest do-loops, it is usually helpful to make the code clearer by naming the outer and inner loops, E.g.

```
outer: do i=1,10
    inner: do j=1,20
	if (i==3) exit outer
	if (j==2) cycle inner
	array(i,j)=2*i+j
    end do inner
end do outer

```


do while loop
-------------

```
do while (expression)
    ...
end do

```


forall loop
-----------

```
forall(i=1:5, j=1:10, a(i,j)<10)
    a(i,j)=1
end forall

```


Read from file
--------------

Use `open()` for file handling. The general form:

```
open(unit=u, file=filename, status=st, action=act, iostat=ios)

```


where

*   `u`: a positive integer, unit number. Often the range 1-99 is allowed (processor-specific). 0 is often special. 5 is for console input. 6 for output to screen. Therefore, don’t use 0, 5, 6.
*   `st`: str,
    *   "new": create new, the file should not yet exists.
    *   "old": open existing file.
    *   "replace": create new if not exits, otherwise overwrite.
    *   "scratch": a file is used only during the execution of the program.
*   `filename`: must not use when `st` is "scratch".
*   `act`: "read", "write", "readwrite".
*   `ios`: an integer variable. It’s set to 0 if open is successful, a positive integer otherwise.

E.g.

```
real :: x,y,z
open(10, file='mydata.txt')
read(10,*) x,y,z

```


where:

*   `mydata.txt`: has 3 values which are read and saved to x,y,z.
*   `10`: named input device.

Write to file
-------------

E.g.

```
open(12, file="myoutput")
write(12,*) var

```


E.g.

```
open(8, file="myoutput")
write(8, "(a2, 3(f10.6))") dtype,x,y,z

```


E.g.

```
program file_example
  implicit none
  integer :: ierror
  open(unit=13, file="test.dat", status="new", action="write", iostat=ierror)
  if (ierror /= 0) then
    print *, "Failed to open test.data"
    stop
  end if
  write (unit=13, fmt=*) "Hello world"
  close (unit=13)
end program file_example

```


It is good programming practice to test if the open statement was successful. If failed, the program would have crashed when trying to write into it.

Close opened file
-----------------

When a file is no longer needed, use `close()` to close it:

```
close (unit=u, iostat=ios, status=st)

```


where:

*   st:
    *   "keep": keep the file. Default, except for "scratch" files.
    *   "delete": delete the file. Default for "scratch" files.

Internal files
--------------

`read()` and `write()` can also read or write into internal files. An internal file is a character variable.

E.g.

```
character (len=8) :: string
write (string, "a", iostat=ios) "abcdfefgh"

```


Extend single precision
-----------------------

In Fortran 77, the prevision of `real` type can be increased by using the `double precision` attribute:

```
double precision :: x

```


In Fortran 90, the types of integer, real, complex and logical have a "default kind" and a number of other kinds. How many other kinds there are for a certain type depends on the particular processor. Each kind has its own kind type parameter, which is an integer of positive value. For example, if, for a certain processor, a kind value of 8 yields a precision equivalent to the old double precision type of Fortran 77, then the following statement

```
real (kind=8) :: x1

```


is equivalent to the Fortran 77 statement

```
double precision x1

```


However, this is not very portable, because the required kind value may be different on another computer. Although many computers use kind values that indicate the number of bytes used for storage of the variable, you cannot rely on this.

In Fortran 90, there are 2 intrinsic functions to obtain the kind value for the required precision:

*   `selected_real_kind()`: for precision of real.
*   `selected_int_kind()`: for precision of int.

The `selected_real_kind()` function returns an integer that is the kind type parameter value necessary for a given decimal precision `p` and decimal exponent range `r`.

E.g.

```
integer, parameter :: ikind=selected_real_kind(p=7, r=10)

```


The integer `ikind` now contains the kind value needed for a precision of 7 decimal places, and a range of at least (10^{-10} to 10^{10}).

If the kind value for the required precision or range is not available, a negative integer is returned.

To use the ikind value in a type declaration statement, it has to be a constant. E.g.

```
integer, parameter :: ikind=selected_real_kind(p=15)
real (kind=ikind) :: sum,x

```


Valid values for `p` are 6, 15 and 18. Unlike variables, parameters can’t change once declared.

To use constants in a program that uses extended precision, append `_ikind` after the constant, where `ikind` is the precision parameter. E.g.

```
integer, parameter :: ikind=selected_real_kind(p=15)
real (kind=ikind) :: x
x=10.0_ikind/3

```


The `selected_int_kind` function returns the lowest kind value needed for the integers with the specified range:

E.g.

```
integer, parameter :: ikind=selected_int_kind(r=10)
integer (kind=ikind) :: big_number

```


Now the integer `big_number` can represent integers in the range (-10^{10} – 10^{10}).

Random number
-------------

*   `random_seed()`: start random number generator, must call this before calling other random number functions.
*   `random_number(t)`: \[0,1) uniform random.

Define subroutine
-----------------

```
subroutine NAME ()
implicit none
...
end subroutine

```


Can use `return` in subroutine to return at given point. If not give, return at the last line.

Subroutine with arguments
-------------------------

Main program and subroutines don’t share namespaces.

To make subroutines take arguments:

```
subroutine NAME(arg1,arg2...)
implicit none
real :: arg1, arg2,...
end subroutine

```


Argument passing are achieved by passing their ram addresses. NOTE that still need to declare args inside subroutine. NOTE that arguments changed inside subroutine will be changed in the main program.

Call subroutine
---------------

```
call NAME()
call NAME(arg1,arg2,...)

```


When it reaches `end subroutine`, the values of the input args are returned to the main program.

Custom functions
----------------

Syntax

```
function FUNC(arg1, arg2,...)
implicit none
real :: FUNC
...
end function

```


Call a function
---------------

```
program NAME
implicit none
real, external :: FUNC
...
FUN(arg1,arg2,...)
end program

```


**NOTE**:

*   must declare the data type of the function both in the main program and in the function itself as if it were a variable.
*   `external` is optional, but helpful in distinguishing variables and functions.
*   functions return 1 value, which is assigned to the function name.
*   variables inside functions, except input arguments, have local scope (not accessible from outside).

If you want the returned value to be stored in some other name than (can’t be the same as function name) the function name, use the `result` option:

```
function funcname(arg1,arg2,...) result (return_name)
   ...
end function

```


Pass functions as function arguments
------------------------------------

Can pass a function name as argument to another function. E.g.

```
program main
implicit none

real, external :: func  ! declare a func
real, intrinsic :: sin  ! build-in sin func

call Exefunc(func)
call Exefunc(sin)

end program

subroutine Exefunc(f)
implicit none
real, external :: f
write (*,*) f(1.0)
end subroutine

real function func(num)
implicit none
real :: num
func=num*2
end function

```


**NOTE** that `external` cannot be omitted here. Subroutines names can also be passed to other subroutines.

One-liner function
------------------

```
real, external :: func
func(a,b) = a+b

```


**NOTE** that such functions cannot be called from outside the main program.

Intent attribute
----------------

Use the `intent` attribute to specify the intention of the arguments in subroutine or function.

The possible attribute values:

*   in: used as input values, not changed in function (read only)
*   out: use as output, they are overwritten
*   inout: arguments are used and overwritten, same as not specifying intent.

E.g.

```
subroutine intent_example (a,b,c,d)
implicit none

real, intent (in) :: a
real, intent (in) :: b
real, intent (in) :: c
real, intent (out) :: d

d= b * b - 4.0 * a * c
end subroutine intent_example

```


It’s good practice to use `intent` attributes, which make the code clearer and more transparent. It also makes the compiler catch mistakes, for instance, when modifying an argument which is denoted as `intent(in)`.

Optional arguments
------------------

Use `optional` attribute to declare an argument as optional, and use `present()` function to check whether the optional argument is passed in. E.g.

```
program main
implicit none

interface
    subroutine sub(a,b)
	implicit none
	interger :: a
	interger, optional :: b
    end subroutine
end interface

call sub(1,2)
call sub(2)

subroutine sub(a,b)
    implicit none
    integer :: a
    integer, optional :: b
    if (present(b)) then
	...
    else
	...
    end if
end subroutine

```


**NOTE** that variable-argument type function/subroutine has to be inside `interface` block, unless inside a _module_. This can be used to create functions with default arguments, and function call can use keyword argument syntax, where the order is insignificant:

```
call func(a=1,b=2,c=3)
call func(b=2,a=1,c=3)
call func(b=2,a=1) ! make c an optional arg, and give it a default value if present(c) is .false.

```


**NOTE** that you can’t use a var that is not present, have to define one for receiving the optional argument, and another for actual computation:

E.g.

```
subroutine sub1(arr,opt_x)
    implicit none

    real, dimension(:,:), intent(in) :: arr
    integer, optional :: opt_x
    integer :: x

    if (present(opt_x)) then
	x=opt_x
    else
	x=10
    end if

    ...
    ! use x so on
    ...
end subroutine

```


Recursive procedures
--------------------

Declare a recursive function/subroutine using the `recursive` keyword. When a function is defined as recursive, the `result` option must be used.

E.g.

```
recursive function factorial(n) result(fac)
implicit none
integer :: fac
integer, intent(in) :: n

select case(n)
    case (0:1)
	fac=1
    case default
	fac=n*factorial(n-1)
end select
end function factorial

```


Local functions/subroutines
---------------------------

Put function/subroutine definitions inside a `contains` – `end contains` block to make it private (cannot access from other program/function/subroutine).

Elemental functions/subroutines
-------------------------------

Put `elemental` keyword before function/subroutine definition to make it elmental E.g.

```
interface
    elemental function func(num)
	implicit none
	integer, intent(in) :: num
    end function
end interface

elemental function func(num)
    implicit none
    integer, intent(in):: num
    func=...
end function

```


**NOTE** that elemental func/sub cannot take arrays as argument, and has to be inside `interface` block.

To call an elemental function:

```
a = func(a)

```


where `a` is an array, and `func()` is defined based on scalar computations, but its `elemental` feature broadcasts the computation to an array, equivalent to `do` a do loop over all elements.

Interface blocks are used to specify the types of functionn arguments and return values. When a procedure is external (defined outside of the main programe), the compiler will (in most cases) know about the procedure’s interface, and can’t check if the precedure call is consistent with the procedure declaration. It’s such good practice to provide interfaces for external procedures.

These following scenarios require an interface:

1.  function returns an array.
2.  function has variable number of arguments
3.  function takes pointer as arguments or returns pointers.

Syntax:

```
interface
    function func_name(arg1,arg2,...)
	implicit none
	!------ declare arg types --------
	real :: arg1
	integer :: arg2
	...
	!------- declare return value type ------
	real :: func_name(10) ! an array
     end function

     subroutine sub_name
	 implicit none
	 interger :: ....
	 ...
     end subroutine
 end interface

```


The interface block is placed at the beginning of the program.

If a procedure `proc1` calls another procedure `proc2`, then the interface block of `proc2` should be placed at the beginning of the procedure `proc1`.

The `date_and_time()` function returns the date and time. E.g.

```
charater(len=8) :: dateinfo     ! ccyymmdd
charater(len=4) :: year, month*2, day*2
charater(len=10) :: timeinfo    ! hhmmss.sss
charater(len=2) :: hour, minute, second*6

call date_and_time(dateinfo, timeinfo)

year=dateinfo(1:4)
month=dateinfo(5:6)
day=dateinfo(7:8)

```


Declare array
-------------

```
type, dimension(n) :: x

```


E.g.

```
real, dimension(10) :: x

```


Use parameter in defining array size, e.g.

```
integer, parameter :: imax = 10
real, dimension(imax) :: x
real :: sum, average
integer :: i
sum=0.0
do i=1,imax
    sum=sum+x(i)
end do
average=sum/imax

```


Declare dynamic array when size is unknown
------------------------------------------

The size of a dynamic array is unknown until execution time.

To declare:

```
integer, dimension(:), allocatable :: array1
real, dimension(:,:), allocatable :: array2

```


**NOTE** that the number of dimensions has to be specified.

To allocate memory, use `allocate()`. E.g.

```
integer, allocatable, dimension(:) :: vector
integer :: size
read *, size
allocate(vector(size))

```


To prevent memory shortage error, get the return value of `allocate()`, if it is 0, then memory allocation is successful.

E.g.

```
integer :: size, return=0
integer, allocatable, dimension(:) :: array

allocate(array(size),stat=return)
if (error/=0) exit

```


To clear up the memory of an array, use `deallocate()`

```
deallocate(vecotr)

```


Declare array with explicit bounds:
-----------------------------------

```
real, dimension(2:6) :: numbers
integer, dimension(-3:2, 0:4) :: matrix

```


Multi-dimensional arrays
------------------------

```
integer, dimension(m,n) :: a

```


Fortran allows the dimension size up to 7. To declare an extended precision 3-d array:

```
real (kind=ikind), dimension(3,4,5) :: a

```


Assign values
-------------

```
do i=1,5
  number(i) = i*20
end do

```


1-D array can be assigned using a shorthand:

```
numbers = (/1,2,3,4,5/)
numbers2 = [ 1,2,3,4,5 ]
numbers3 = (/ (i, i=1,10,2) /)    ! (1,3,5,7,9)
numbers4 = (/ (i*2. i=1,5) /)     ! (2.0,4.0,6.0,8.0,10.0)

```


Use array constructors to define array constants:

```
integer, dimension(8), parameter :: p = (/1,2,3,5,7,11,13,17,19/)

```


Indexing
--------

**Array indexing starts from 1**, using parentheses: e.g. `x(2)`. **Both ends are included**.

Syntax: `array(start:stop:step)` E.g.

```
a(1:7)
b(1:10:2)
c(5:)
d(1, 1:4:2)

```


Array functions
---------------

*   `size(a[,dim])` : total size.
*   `dot_product(vector_a, vector_b)` : dot product.
*   `matmul(matrix_a, matrix_b)` : matrix multiplication.
*   `transpose()` : transpose.
*   `all(condition[,dim])` : similar to `numpy.all()`. If `dim` is given, only  
    along given dimension.
*   `any(condition[,dim])` : similar to `numpy.any()`.
*   `count(condition[,dim])` : count the number of `.true.` values returned by condition.
*   `maxval(array[,dim,condition])` : return max value of array, optionally along dimension `dim`, satisfying requirement `condition`.
*   `minval(array[,dim,condition])`.
*   `product(array[,dim,condition])` : return product of all elements, optionally along given dimension and filtered by mask.
*   `sum(array[,dim,condition])`.
*   `allocated(array)`: check if the array if allocated.
*   `lbound(array[,dim])`: get the lower dimension limit for the array. If `dim` not given, get an integer vector. If `dim` given, return lower bound of given dimension.
*   `ubound(array[,dim])`: upper bound.
*   `shape(array)`: same as python.
*   `merge(x,y,condition)`: same as `np.where(condition,x,y)`.

### reshape(array,shape\[,pad,order\])

E.g.

```
real, dimension(3,2) :: a
a=reshape((/1,2,3,4,5,6/), (/3, 2/))

```


*   if `pad` is given, will pad `array` with numbers from `pad` to fill up the new shape.
*   `order` is like the order in `numpy.ndarray`, and specifies the order in which numbers are filling. Default is column-wise.

E.g.

```
integer, dimension(9) :: a = (/1,2,3,4,5,6,7,8,9/)
integer, dimension(10) :: pad = (/-1,-2,-3,-4,-5,-6,-7,-8,-9,-10/)
integer, dimension(4,4) :: c
c=reshape(a, (/4,4/), pad=pad, order=(/2,1/))

```


c will be:

> 1 2 3 4 5 6 7 8 9 -1 -2 -3 -4 -5 -6 -7

### spread(array,dim,n):

array/slab grow. Grow `array` along the `dim` dimension by `n` copies. E.g.

```
integer, dimension(10) :: a = (/1,2,3,4,5,6,7,8,9,10/)
integer, dimension(2,5) :: b
integer, dimension(2,2,5) :: c
b=reshape(a,(/2,5/))
c=spread(b,1,2)

```


b will be:

> 1 3 5 7 9 2 4 6 8 10

c(1) and c(2) will both be:

> 1 2 3 4 5 6 7 8 9 10

### cshift(array,shift,dim)

Similar to `np.roll(array,shift,axis)`. If `shift` is positive, shift to the left, otherwise to the right.

E.g.

```
integer, dimension(5) :: a = (/1,2,3,4,5/)
integer, dimension(5) :: b
b=cshift(a,1,1)

```


b will be `2 3 4 5 1`.

### eoshift(array,shift,boundary,dim)

Similar to `cshift` except that new elements are taken from `boundary` which is a scalar. If boundary is not given, pad with 0s.

E.g.

```
integer, dimension(5) :: a = (/1,2,3,4,5/)
integer, dimension(5) :: b
b=eoshift(a,boundary=-10,shift=2)

```


b will be `3 4 5 -10 -10`.

### maxloc(array\[,condition\])

Find the max element indices in `array`, optionally satisfying the `condition`. Equivalent to `np.where(a==np.max(a))`.

Return a vector containing the indices.

E.g.

```
integer, dimension(6) :: a=(/1,2,3,4,5,6/)
integer, dimension(2,3) :: b
integer, dimension(2) :: c
b=reshape(a,shape(b))
c=maxloc(b,b<=5)

```


b is:

> 1 3 5 2 4 6

c will be `1 3`.

### minloc(array\[,condition\])

Similar to `maxloc()`.

### pack(array,mask)

Fancy indexing an array using a logical mask. E.g.

```
integer, dimension(5) :: data = (/ 1,2,3,4,5 /)
logical, dimension(5) :: mask

mask=.TRUE.
mask(1)=.FALSE.
mask(3)=.FALSE.

write(*,*) pack(data,mask)

```


will print `2,4,5`.

**NOTE** that if both `array` and `mask` are n-dimensional (e.g. both being (3×3)), `pack(array,mask)` always returns an 1D array.

### where statement

Syntax:

```
where (condition)
    ...
[elsewhere (condition)
    ...]
[elsewhere
    ...]
end where

```


E.g.

```
integer, dimension(6) :: a = (/1,2,3,4,5,6/)
where (a<4)
    a=1
elsewhere
    a=10
end where

```


a will be `1 1 1 10 10 10`.

File name convention
--------------------

File names ending in `.f90` and `.f95` are assumed to be **free form**, suitable for Fortran 90/95 compilation.

File names ending in `.f` and `.for` are assumed to be **fixed form**, compatible with Fortran 77.

Compile a program
-----------------

### Basic compilation

The simplest command:

```
gfortran myprog.f90

```


This creates an executable `a.out` in the current directory. To specify the name of the executable:

```
gfortran myprog.f90 -o myprog

```


### Compile with include files

The path of include files can be given with the `-I` option:

```
gfortran myprog.f90 -o myprog -I/home/user/fortran/inc

```


or

```
gfortran myprog.f90 -o myprog -I$MYINC

```


where the environment variable `MYINC` is set with

```
MYINC=/home/user/fortran/inc/

```


### Speed optimization

The `-Olevel` option performs some optimization of the executable and can lead to significant increases in execution speed.

E.g.

```
gfortran myprog.f90 -o myprog -O2

```


### Warning options

The `-Wlevel` option enables most warning messages. Such messages are generated at compile-time warning of, for example, unused or unset variables.

E.g.

```
gfortran myprog.f90 -o myprog -O2 -Wall

```


### Runtime options

Various run-time options can be selected, these options cause extra code to be added to the executable and so can cause significant decreases in execution speed. However these options can be very useful during program development and debugging.

E.g.

```
gfortran myprog.f90 -o myprog -O2 -fbounds-check

```


This causes the executable to check for "array index out of bounds conditions".

### Recommended options

For better safety:

```
gfortran myprog.f90 -o myprog -Wall -fbounds-check -ftrace=full -O2

```


If speed of execution is important then use the following options:

```
gfortran myprog.f90 -o myprog -Wuninitialized -Wimplicit-none -Wunused-vars -Wunset-vars -O2

```


Compile subprograms
-------------------

If a Fortran 90/95 project contains more than one program source files, then to compile all source files to an executable, use when:

### subprograms are external

```
gfortran main.f90 sub1.f90 sub2.f90 sub3.f90 -o myprog

```


**NOTE** main file in front of subprogram files.

### subprograms are defined in module

```
gfortran mod.f90 main.f90 -o myprog

```


**NOTE** module file in front of main file.

Create and link object files
----------------------------

When working on large projects, especially projects that are shared between a number of programmers/users, it is useful to create object files or libraries of object files that can be shared between programmers and users.

If a subprogram has been compiled, it’s not necessary to recompile it again during the development of other parts of the project. Completed subprograms can be compiled into _object files_ that can be linked during the compilation of the whole program.

E.g.

```
gfortran main.f90 sub1.o sub2.o sub3.o -o myprog

```


where the `.o` object files are created by

```
gfortran -c sub1.f90
gfortran -c sub2.f90
gfortran -c sub3.f90

```


Create and link library files
-----------------------------

If many object files are to be linked then it is convenient to place them in a library.

Libraries can be created using the `ar` command. To place object files in a library:

```
ar rcvf libsubs.a sub1.o sub2.o sub3.o

```


The library created is named `libsubs.a`, containing 3 objects: `sub1.o`, `sub2.o`, `sub3.o`.

**NOTE** that the name of the library must begin with `lib` and end with `.a`.

To add more objects into the library file:

```
ar rcvf libsubs.a sub4.o

```


To list the contents of a library:

```
ar tv libsubs.a

```


To list subroutines and functions in the library:

```
nm libsubs.a

```


To delete object from the library:

```
ar dv libsubs.a sub.o

```


To link a library while compiling a program:

```
gfortran main.f90 -o myprog -L. -lsubs

```


(The `-L.` option tells the linker that the library is in the current directory.)

If the library is not in the current directory, need to give the path:

```
gfortran main.f90 -o myprog -L/home/user/fortran/lib/ -lsubs

```


Linux library types
-------------------

There are 2 types of library files:

### 1\. static library `.a`

Library of object code which is linked at compilation and becomes part of the application. If there is any change in the lib, you need to recompile the application.

### 2\. dynamically linked shared object library `.so`

Two possible ways of usage:

1.  Dynamically linked at run time but statically aware.
    
    The libraries must be available during compile/link phase. The shared objects are not included into the executable component but are tied to the execution.
    
2.  Dynamically loaded/unloaded and linked during execution.
    
    Use the dynamic linking loader system function. If there is any change in the `.so` file, no need to recompile the main program, but do need to make sure the main program is linked to the updated lib file.
    

At compile time, the linker insures that all the necessary symbols are either linked into the executable, or can be linked at runtime from the shared library. Executables compiled from shared libraries are smaller, but the shared libraries must be included with the executable to function correctly. When multiple programs use the same shared library, only one copy of the library is required in memory.

Library naming conventions
--------------------------

Libraries are typically named with a `lib` prefix. When linking, the command line reference to the library will **NOT** contain the `lib` prefix. E.g.

```
gcc src-file.c -lm -lpthread

```


The 2 libraries linked in the above example are:

*   `m` -> `libm.a`
*   `pthread` -> `libpthread.a`.

Both files can be found in `/usr/lib/` by default.

Create shared lib `.so` file from Fortran code
----------------------------------------------

1.  Use the `-shared` option.
2.  On Linux systems using IA-32 architecture and Intel@64 architecture, you must also specify `-fpic` for the compilation of each object file you want to include in the shared library.
3.  Use the `-o` option to specify the output file name.

E.g.

```
gfortran -shared -fpic -o octagon.so octagon.f90

```


This will create `octagon.so`.

Install shared libraries
------------------------

Once the shared library is created, it must be installed for private or system-wide use before you run a program that refers to it:

*   To install a private shared library (when you are testing, for example), set the environment variable `LD_LIBRARY_PATH`, as described in `ld(1)`.
    
*   To install a system-wide shared library, place the shared library file in one of the standard directory paths used by `ld` or `libtool`.
    

Link the shared library
-----------------------

1.  Create the shared lib `.so`.
2.  Compile the main program.
3.  Link using `gfortran`.

E.g.

```
gfortran -shared -fpic -o mylib.so mylib.f90
gfortran -c main.f90
gfortran -o main.exe main.o mylib.so

```


**NOTE** that in the last command, the main goes in front of the linked lib. This also holds for linking to LAPACK or BLAS: **write the name of the source file first**. E.g.

```
gfortran mylapack.f90 -llapack -lblas -o mylapack

```


**NOTE** that if the shared lib files are not in the system’s dynamic linker path, need to either modify the `LD_LIBRARY_PATH` variable to include it, or give the path to the `gfortran` command:

```
gfortran -o main.exe main.o -L/path/to/lib/ mylib.so

```


gdb – GNU debugger
------------------

Generally comes with Linux. `xxgdb` is a GUI to gdb for X window.

In order to use a debugger like `gdb` to track the execution of your Fortran program, it is necessary to compile the program with the `-g` option.

E.g. suppose your source file is called `foo.f`. To compile it:

```
gfortran -g foo.f -o foo

```


To start execution of a program named `foo` under `gdb`:

```
gdb foo

```


Then it will enter the `gdb` session. Then type:

```
break main
run

```


This will start execution of the program, but execution will pause just before the first executable statement.

Commands in `gdb` and `xxgdb`:

*   `break` : set a breakpoint.
*   `run` : begin.
*   `cont` (or `c`) : continue.
*   `next` (or `n`) : next line.
*   `step` (or `s`) : step in.
*   `print` (or `p`) expr : display the value of the expression.
*   `list` (or `l`) : same as `l` in pdb.

dbx debugger
------------

*   `run` : begin.
*   `cont` (or `c`) : continue.
*   `next` (or `n`) : next line.
*   `step` (or `s`) : step in.
*   `stop [var]` : breakpoint when the variable \[var\] changes.
*   `stop in [proc]` : stop when procedure \[proc\] is entered.
*   `stop at [line]` : breakpoint at line \[line\].

Some free libraries:

*   RANDLIB: random number and statistical distribution generators
*   BLAS
*   EISPACK
*   GAMS–NIST: Guide to Available Math Software
*   Some statistical and other routines from NIST
*   LAPACK
*   LINPACK
*   MINPACK
*   MUDPACK
*   NCAR Mathematical Library
*   The Netlib collection of mathematical software, papers, and databases.
*   ODEPACK
*   ODERPACK: a set of routines for rankning and ording
*   Expokit for computing matrix exponentials
*   SLATEC
*   SPECFUN: Common Mathematical Library: a comprehensive software library containing over 1400 general purpose mathematical and statistical routines written in Fortran 77 ([http://www.netlib.org/slatec/index.html](http://www.netlib.org/slatec/index.html)) and Fotran 90 ([http://people.sc.fsu.edu/~jburkardt/f\_src/slatec/slatec.html](http://people.sc.fsu.edu/~jburkardt/f_src/slatec/slatec.html)).
*   STARPAC
*   StatLib statistical library
*   TOMS
*   Sorting and merging strings

A module serves as a packaging means for subprogrames, data and interface blocks, a new feature of Fortran 90. They make `common` blocks (routinely used in Fortran 77) and `include` statements obsolete.

module structure
----------------

A typical module has 2 parts:

1.  declaration (including `interface` blocks, `type` and `parameter` declarations).
    
2.  a `contains` part for subroutine and function definitions.
    
    module mod\_name implicit none \[declarations\] contains ! function definitions ! subroutine definitions end contains end module
    

A module can have just the declaration or subprogram part, or both.

Procedures defined inside a program are internal procedures.

An internal procedure is local to its host, and have access to host’s variables.

It is often better to use external (define outside main program) rather than internal, because they can be called from more than one program, and they are safer that variables from the calling program are hidden from the procedure.

If `implicit none` is used at the beginning of module definition, it’s not necessary to put `implicit none` in the subprograms in the module.

When a subroutine is defined in a module, then there is no need to provide an explicit interface in the calling program (as long as the module’s contents are made available to the program via the `use` statement).

use module
----------

To use a module in a program or a subroutine

```
use mod_name1
use mod_name2
...

```


**NOTE** `use` statement has to be before `implicit none` in the main program (only comments are allowed before `use`).

accessibility of module variables and procedures
------------------------------------------------

By default, all variables, functions and subroutines are available to the program that uses the module, by the `use` statement.

*   Variables declared in a module are global to the module.
*   Variables declared in a module are global in the importing program/routine.

Can use the `private` and `public` attributes to control accessibility.

E.g.

```
module my_module
implicit none
    real, parameter, private :: pi = 3.1415

contains
    subroutine show_const()
	write (*,*) pi
    end subroutine
end module

```


The default accessibility of the module can be set by the `public` or `private` statements. If `private` is specified, then all module contents are private, except those that are explicitly defined as public:

E.g.

```
module my_module
implicit none
private
integer :: status, count

! public variables
public :: ndim, nvar, max_number, data_array
! public procedures
public :: getData, getList

contains
    subroutine getData()
    ...
    end subroutine

    subroutine getList()
    ...
    end subroutine
end my_module

```


Selecting module elements
-------------------------

Generally, the `use` statement makes available all (public) elements of a module.

However, when only a subset of the module is needed, the accessibility can be restricted with `only`.

E.g.

```
program convert_temperature
    use convertT, only: CtoF, FtoC
...
end program convert_temperature

```


Aliasing element names in use
-----------------------------

```
use A, only: Afoo=>foo

```


is equivalent to

```
from A import foo as Afoo

```


Data encapsulation
------------------

Modules allow data and operations to be hidden from the rest of the program. Data encapsulation functions as a security tool, because the data in the object is only available through the methods.

E.g.

```
module student_class
  implicit none
  private
  public :: create_student, get_mark

  type student_data
    character (len=50) :: name
    real :: mark
  end type student_data

  type (student_data), dimension (100) :: student

  contains
    subroutine create_student (student_n, name, mark)
    ! here some code to set the name and mark of a student
    end subroutine create_student

    subroutine get_mark (name, mark)
    ! dummy arguments
	character (len=*), intent (in) :: name
	real, intent (out) :: mark
	! local variables
	integer :: i

	do i = 1,100
	if (student(i) == name) then
	    mark = student(i)%mark
	end if
	end do
    end subroutine get_mark
end module students

```


The `student_class` module defines a data type (`student_data`) to hold information of a student (name and a mark). Only the subroutines, `create_student` and `get_mark`, are accessible from outside the module, all other module contents are private. Thus, one cannot obtain the mark of a student by writing:

```
mark1 = student(1)%mark

```


because the array `student` is private.

Global data management – no more common blocks
----------------------------------------------

Procedures can communicate with each other via their argument lists. However, a program may consist of many procedures that require access to the same data. It would be convenient if this data were globally accessible to the whole program.

In FORTRAN 77, this was accomplished by `common` blocks. However, modules can replace all uses of `common` blocks. Global data can be packed in a module, and all procedures requiring this data can simply use the module.

Modules are much safer and cleaner than `common` blocks. `Common` blocks have no mechanisms to check errors, variables can be renamed implicitly, and there are no access restrictions. So, don’t use `common` blocks, use modules instead!

A pointer in Fortran is a data object with the pointer attribute, containing information about a particular object, such as its type, rank, extent, and memory address.

A pointer variable is declared with the `pointer` attribute. A pointer variable that is an array must be a `deferred-shape` array (only the rank of the array is specified).

E.g.

```
integer, pointer :: p   ! pointer to integer
real, pointer, dimension(:) :: rp         ! pointer to 1d array
real, pointer, dimension(:,:) :: rp2      ! pointer to 2d array

```


In contrast to a normal data object, a pointer has initially no space set aside for its contents. It can only be used after space has been associated with it.

A target is the space that becomes associated with the pointer.

A pointer can point to:

*   an area of dynamically allocated memory, as illustrated in the next section.
*   a data object of the same type as the pointer, with the target attribute (see section on targets below)

allocating space for a pointer
------------------------------

E.g.

```
integer, pointer :: p
allocate(p)
p=1

```


The allocated storage space can be deallocated by the `deallocate` statement. It is a good idea to deallocate storage space that is not any more needed, to avoid accumulation of unused and unusable memory space.

target
------

To act as a target for a pointer it must be declared with the target attribute. This is to allow code optimization by the compiler.

```
integer, pointer :: p1
integer, target :: t1
p1=>t1
p1=1

```


After the statement \`p1=>t1\`, the pointer `p1` acts as an alias for `t1`. Changing `p1` has the effect of changing `t1`.

Association
-----------

The association status of a pointer can be:

*   undefined
*   associated
*   disassociated

If the association status is not undefined, it can be tested using the associated function:

*   `associated(ptr)`: check if pointer ptr is associated with any target.
*   `associated(ptr,target)`: check if pointer is associated with target.

A pointer can be explicitly disassociated with a target using the `nullify` statement:

```
nullify(ptr)

```


It is a good idea to nullify pointers instead of leaving their status undefined, because they can then be tested with the associated function.

**Nullify does not deallocate the targets (because there can be more than one pointer pointing to the same target). Deallocate implies nullification as well.**

Linked lists
------------

A _linked list_ is a special kind of data storage structure. It is a series of derived type that are linked together by pointers.

There are several kinds of linked lists (single-linked lists, double-linked lists, binary trees).

Each element (also called node or link) of a linked list is an object of derived type that consists of a part with data and a pointer to the next object of the same list:

The pointer is of the same type as the other elements of the list.

The derived type can for example be something like:

```
type node
  integer :: i
  real :: value
  type(node), pointer :: next
end type node

```


The “next” pointer of the last link in the list should be nullified. You also need a pointer (often referred to as head pointer) that refers to the first item in the list.

Differences between linked lists and arrays
-------------------------------------------

*   Linked lists can be allocated dynamically, so you don’t need to know before the program is executed how many elements are needed (this also saves memory space).
*   The size of the list can change during execution (links can be added and removed).
*   Links can be added at any position in the list.
*   The links are not necessarily stored contiguously in memory.

Example
-------

```
program linkedlist
  implicit none

  type :: link
    integer :: i
    type (link), pointer :: next
  end type link

  type (link), pointer :: first, current
  integer :: number
  nullify (first)
  nullify (current)

  ! read in a number, until 0 is entered
  do
    read*, number
    if (number == 0) then
      exit
    end if

    allocate (current)     ! create new link

    current%i = number
    current%next => first  ! point to previous link
    first => current       ! update head pointer
  end do

  ! print the contents of the list
  current => first
  ! point to beginning of the list
  do
    if (.not. associated (current)) then     ! end of list reached 
      exit
    end if

    print*, current%i
    current => current%next        ! go the next link in the list
  end do

end program linkedlist

```


In this program a link is defined that can hold an integer. The pointer “first” is the head pointer. In the first do loop, numbers are read in until a 0 is entered. After each number is read in, a new link is created and added before the previous link.

See this explanation from [stackoverflow](https://stackoverflow.com/questions/15662371/fortran-difference-between-include-and-modules).

The short conclusion is: prefer modules to `include` in most cases.

One possible valid case to use include is: when a single module file gets too long, then separate it into different files, and use `include` in the module file to package them together.

namelist input format
---------------------

```
! comments

 &GROUP_NAME

  fields = 'cin' ! use single/double quotes for strings
  mercator_defs = .true.  ! no need to use quotes on boolean
  interp_method = 1 ! no need to use qutoes on numbers
  interp_levels = 1000.,900.,500.  ! use comma to separate
   ...  
 /

 &GROUP_NAME2
   ...
 /

```


*   Order of key-value pairs in group is not important.
*   Order of groups is important.

Usage of namelist
-----------------

In the main program:

```
namelist /namelist_name/ key1, key2, ...  
open(1,file='namelist_file')
read(1, namelist_name)

```


linspace
--------

```
subroutine linspace(x1, x2, n, arr)
    ! linspace, real
    implicit none
    integer :: n, i
    real :: x1, x2, dx
    real, dimension(n), intent(out) :: arr

    dx=(x2-x1)/n
    arr=(/ (i*dx, i=1, n) /)

end subroutine linspace

```


Measure execution time
----------------------

Use `CPU_TIME()` to get cpu time. E.g.

```
real :: t1, t2
call CPU_TIME(t1)
! do stuff
call CPU_TIME(t2)
write (*,*) 'cpu time:', t2-t1

```


pretty print of 2d matrix
-------------------------

NOTE that this subroutine has optional arguments and inferred input dimension (arr), need to put it in a module, or add an interface block.

```
subroutine print2D_r(arr,pre,space)
    ! Pretty print of 2D matrix
	implicit none

	real, dimension(:,:), intent(in) :: arr
	integer, optional :: pre, space ! precision, spacing
	character(len=20) :: f_str
	character(len=1) :: s1,s2

	integer :: nx, ny, i, j
	integer :: pre2, space2 ! max len, spacing

	if (present(pre) .eqv. .false.) then
	    pre2=4
	else
	    pre2=pre
	end if
	if (present(space) .eqv. .false.) then
	    space2=4
	else
	    space2=space
	end if

	ny=size(arr,1)
	nx=size(arr,2)

	!--------------Compose format string--------------
	! f_str = '(f8.n,mx)'
	! n = decimal places (pre)
	! m = spaces between numbers (space)
	write (s1, "(I1)") pre2
	write (s2, "(I1)") space2
	f_str='(f8.'//s1//','//s2//'x)'

	do i = 1,ny
	    do j = 1,nx
		write(*,trim(f_str),advance='no') arr(i,j)
	    end do
	    write(*,*) 
	end do
	write(*,*) 

    end subroutine print2D_r

```


use with netcdf fortran
-----------------------

Install netcdf c and fortran libraries from the package manager.

To compile a script with `use netcdf` in it:

```
f95 -o outfile -I/usr/include fortran_code.f90 -lnetcdff -lnetcdf

```


or try this:

```
gfortran -o outfile -I/usr/include/ -L/usr/lib/ -lnetcdf simple_xy_wr.f90 /usr/lib/libnetcdff.a

```


See the explanations here: [https://stackoverflow.com/questions/13941549/compiling-fortran-netcdf-programs-on-ubuntu](https://stackoverflow.com/questions/13941549/compiling-fortran-netcdf-programs-on-ubuntu)

Specifically:

> Ordering of object files and archives on the linker command line is very important on Unix systems since the default linker behaviour is to search for symbol definitions only in archives that follow the object file or archive, where an unresolved reference was found, referred to single pass linking.
> 
> This means that if your code references \_<sub>netcdf</sub><sub>MOD</sub><sub>nf90</sub><sub>strerror</sub>, then the archive that contains the definition of this symbol (libnetcdff.a) must appear after the list of object files from your program. libnetcdff.a itself references symbols from the C library libnetcdf.a, hence it must be linked after libnetcdff.a. So the correct link order is:
> 
> f95 -o xy -I/usr/include/ simple<sub>xy</sub><sub>wr.f90</sub> -lnetcdff -lnetcdf
