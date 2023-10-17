# Matlab CheatSheet
Cheat Sheet for MATLAB Tools Course at ETH Zürich, created by Res Jöhr.
Modified by Christian Toderascu.

**last update: 20231017**

last update available on [GitHub - Matlab CheatSheet.md](https://github.com/Todochris/CheatSheets/blob/main/Matlab%20CheatSheet.md)
[MATLAB Documentation](mathworks.com/help/matlab/)



## File commands

## Basics
---------

### Workspace
| command           | description       |
| :---------------- | :---------------- |
| ans               | Most recent answer
| clc               | clear command window
| clear             | var clear variables Workspace
| clf               | Clear all plots
| close all         | Close all plots
| ctrl-c            | Kill the current calculation
| doc fun           | open documentation
| disp(’text’)      | Print text
| sprintf("text%g",num) | Format text by replacing "%g" by the number from num
| sprintf("text%s",str) | Format text by replacing "%s" by the string from str
| format shortG     | Set output display format todo change from MTFEM
| help fun          | open in-line help
| load filename {vars} | load variables from .mat file
| save {-append} file {vars} | save var to file
| addpath path      | include path to ..
| iskeyword arg     | Check if arg is keyword
| % comment         | In-line comment
| ...               | connect lines (with break)
| ";"               | (after command) suppresses output
| scriptname        | runs scriptname.m
| tic, toc          | start and stop timer
| ver               | List of installed toolboxes
| userpath          | returns the folder that is included in your path
| userpath('clear') | deletes the default MATLAB folder from your path for all your sessions from now on

### Defining and Changing Variables

```matlab
a = 5                   % Define variable a to be 5
A = [1, 2,  3,  4;      % Set A to be a 3×4 matrix
     5, 6,  7,  8;      % ”,” separates columns
     9, 10, 11, 12]     % ”;” separates rows
```

| command           | description       |
| :---------------- | :---------------- |
| [A,B], horzcat(A,B)   | Concatenate arrays horizontally
| [A;B], vertcat(A,B)   | Concatenate arrays vertically
| x(2) = 7          | Change 2nd element of x to 7
| A(2,1) = 0        | Change A2,1 to 0
| x(2:12)           | The 2nd to the 12th elem. of x
| x(1:3:end)        | Every 3rd elem. of x (1st to last)
| x(x>6)            | List elements > 6.
| x(x>8)=8          | change elements using condition
| A(4,:)            | Get the 4th row of A
| A(:,3)            | Get the 3rd column of A
| A(6, 1:3)         | Get 1st to 3rd elem in 6th row
| zeros(9, 5)       | Make a 9 × 5 matrix of zeros
| ones(9, 5)        | Make a 9 × 5 matrix of ones
| eye(7)            | Make a 7 × 7 identity matrix
| diag(x)           | Create diagonal matrix
| diag(A)           | Get diagonal elements of matrix
| meshgrid(x)       | 2-D and 3-D grids
| 7:15              | Row vector of 7, 8,...,14, 15
| a:ds:b            | lin. spaced vector with spacing ds
| linspace(1,20,35) | Lin. spaced vector (35 elements)
| logspace(1, 1e5, 50)  | Log. spaced vector (50 elements)

### Arithmetics
| command           | description       |
| :---------------- | :---------------- |
| +, -              | Addition, Subtraction (elementwise)
| A * B             | Matrix multiplication
| A .* B            | elementwise multiplication
| A./B              | elementwise division
| B.\A              | Left array division
| /                 | Solve xA = B for x
| \                 | Solve Ax = B for x
| A∧n               | normal/(square) matrix power
| A.∧n              | Elementwise power of A
| sum(X)            | Sum of elements (along columns)
| prod(X)           | Product of elements (along columns)

### Elementary Functions

Only sin functions are given in example but there are analogous elementwise trigonometric functions for cos, tan and cot

| command           | description       |
| :---------------- | :---------------- |
| sin(A)            | Sine of argument in radians
| sind(A)           | Sine of argument in degrees
| asin(A)           | Inverse sine in radians
| sinh(A)           | Hyperbolic sine
| abs(A)            | Compute |x| √
| sqrt(x)           | Compute x
| log(x)            | Compute ln(x)
| log10(x)          | Compute log10(x)
| sign(x)           | sign of x
| exp(x)            | exponential of x

### Complex Numbers

| command           | description       |
| :---------------- | :---------------- |
| abs(z)            | Absolute value and complex magnitude
| angle(z)          | Phase angle
| complex(a,b)      | Create complex numbers
| conj(z)           | Elementwise complex conjugate
| i or j            | Imaginary unit
| imag(z)           | Imaginary part of complex number
| isreal(z)         | Determine whether array is real
| real(z)           | Real part of complex number
| ctranspose(Z)     | Complex conjugate transpose

### Constants

| command           | description       |
| :---------------- | :---------------- |
| pi                | π = 3.141592653589793
| NaN               | Not a number (i.e. 0/0)
| Inf               | Infinity
| eps               | Floating-point relative accuracy
| realmax           | Largest positive floating-point number
| realmin           | Smallest positive floating-point number

## Numerics and Linear Algebra
------------------------------


### Numerical Integration and Differentiation

| command           | description       |
| :---------------- | :---------------- |
| integral(f,a,b)   | Numerical integration
| integral2(f,a,b,c,d)      | 2D num. integration
| integral3(f,a,b,..,r,s)   | 3D num. integration
| trapz(x,y)        | Trapezoidal integration
| cumtrapz(x,y)     | Cumulative trapez integration
| diff(X)           | Differences (along columns)
| gradient(X)       | Numerical gradient

### Matrix Functions/ Linear Algebra

| command           | description       |
| :---------------- | :---------------- |
| A’                | Transpose of matrix or vector
| inv(A)            | inverse of A (use with care!)
| det(A)            | determinant of A
| eig(A),eigs(A)    | eigenvalues of A (subset)
| cross(A,B)        | Cross product
| dot(A,B)          | Dot product
| kron(A,B)         | Kronecker tensor product
| norm(x)           | Vector and matrix norms
| linsolve(A,B)     | Solve linear system of equations
| rank(A)           | Rank of matrix
| trace(A)          | Sum of diagonal elements
| curl(X,Y,Z,U,V,W) | Curl and angular velocity
| divergence(X,..,W)| Compute divergence of vector field
| null(A)           | Null space of matrix
| orth(A)           | Orthonormal basis for matrix range
| mldivide(A,B)     | Solve linear system Ax = B for x
| mrdivide(B,A)     | Solve linear system xA = B for x
| decomposition(A)  | Matrix decomposition
| lsqminnorm(A,B)   | Least-squares solution to linear eq.
| rref(A)           | Reduced row echelon form
| balance(A)        | Diagonal scaling (improve eig. vec.)
| svd(A)            | Singular value decomposition
| gsvd(A,B)         | Generalized svd
| chol(A)           | Cholesky factorization

### Matrix manipulation

| command           | description       |
| :---------------- | :---------------- |
| cat(dim,A,B)      | Concatenate arrays
| ndims(A)          | Number of array dimensions
| flip(A)           | Flip order of elements
| fliplr(A)         | Flip array left to right
| flipud(A)         | Flip array up to down
| squeeze(A)        | Remove dimensions of length 1
| reshape(A,sz)     | Reshape array
| size(A)           | size of A
| sort(A)           | Sort array elements
| sortrows(A)       | Sort rows of matrix or table
| length(A)         | Length of largest array dimension


## Graphics

### Plotting

| command           | description       |
| :---------------- | :---------------- |
| plot(x,y)         | Plot y vs. x
| axis equal        | Scale axes equally
| title(’A Title’)  | Add title to the plot
| xlabel(’x axis’)  | Add label to the x axis
| ylabel(’y axis’)  | Add label to the y axis
| legend(’foo’, ’bar’) | Label 2 curves for the plot
| grid              | Add a grid to the plot
| hold on / off     | Multiple plots on single figure
| xlim /ylim / zlim | get or set axes range
| figure            | Start a new plot

### Plot types
![Plot gallery](/img/matlab_plots.png "Credits: GitHub, Inc. @ mathworks.com/products/matlab/plot-gallery")

## Programming methods

### Functions
% defined in m-file
% File must have the same name as the function 
```matlab
function output = addNumbers(x, y)
    % function summing up two numbers
    % Args:
        % x (int, float) : a number
        % y (int, float) : a number
    % Returns:
        % output (int, float) : the result
    output = x + y; %multiple or var nr of args possible end
```

### Anonymous Functions
```matlab
% defined via function handles
f = @(x) cos(x.ˆ2)./(3*x);
```

### Relational and logical operations

| command           | description       |
| :---------------- | :---------------- |
| ==                | Check equality
| ∼=                | Check inequality
| >                 | greater than
| >=                | greater or equal to
| <                 | less than
| <=                | less or equal to
| ~                 | logical NOT
| & , &&            | logical AND, AND for numbers
| `| , ||`          | logical OR, OR for numbers
| xor               | logical exclusive-OR

### if, elseif Conditions
```matlab
if n<10
    disp('n smaller 10')
elseif n<20
    disp('n between 10 and 20')
else
    disp('n larger than 20')
end % control structures terminate with end
```

### Switch Case
```matlab
n = input('Enter a number: '); 
switch n
    case -1
        disp('negative one')
    case 0 
        disp('zero')
    case {1,2,3} %check three cases together 
        disp('positive one')
    otherwise
        disp('other value')
end % control structures terminate with end
```
### For-Loop`
```matlab
%loop a specific number of times, and keep track of each ... 
% iteration with an incrementing index variable
%parfor might be used to parallelize the execution
for i = 1:3
    disp('cool'); % comment with some $\latex in it \pi x^2$
end % control structures terminate with end
```

### While-Loop
```matlab
%loops as long as a condition remains true
n = 1;
nFactorial = 1;
while nFactorial < 1e100
    n = n + 1;
    nFactorial = nFactorial * n;
end % control structures terminate with end
```

### Scalable function in matlab

```matlab
add_var.param1 = 5 ; 

disp(fun(1,[])); % this will use the default parameters
disp(fun(1,add_var)); % this will use the parameters defined in add_var

function output = fun(var1, add_var)
    % scalable function in matlab
    % Args:
        % var1 (int, float) : a mandatory variable for your function
        % add_var (structured variable) : 
            % = [] for default values in the function
            % add_var.param1 (int, float) : param1 value instead of default
    % Returns:
        % output () : the result

    if ~isempty(add_var) & any(ismember(fields(add_var),'param1'))
        param1 = add_var.param1;
    else
        param1 = 1 ; % "default_value"
    end

    output = var1*param1;

end
```


## Special Topics

### Polynomials
| command           | description       |
| :---------------- | :---------------- |
| poly(x)           | Polynomial with roots x
| poly(A)           | Characteristic polynomial of matrix
| polyeig(x)        | Polynomial eigenvalue problem
| polyfit(x,y,d)    | Polynomial curve fitting
| residue(b,a)      | Partial fraction expansion/decomposition
| roots(x)          | Polynomial roots
| polyval(p,x)      | Evaluate poly p at points x
| conv(u,v)         | Convolution and polynomial multiplication
| deconv(u,v)       | Deconvolution and polynomial division
| polyint(p,k)      | Polynomial integration
| polyder(p)        | Polynomial differentiation

### Interpolation and fitting
| command           | description       |
| :---------------- | :---------------- |
| interp1(x,v,xq)   | 1-D data interpolation (table lookup)
| interp2(X,Y,V,Xq,Yq)  | 2D interpolation for meshgrid data
| interp3(X,..V,..Zq)   | 3D interpolation for meshgrid data
| pchip(x,v,xq)     | Piecew. cubic Hermite poly interpol
| spline(x,v,xq)    | Cubic spline data interpolation
| ppval(pp,xq)      | Evaluate piecewise polynomial
| mkpp(breaks,coeffs)   | Make piecewise polynomial
| unmkpp(pp)        | Extract piecewise polynomial details

### Differential equations
| command           | description       |
| :---------------- | :---------------- |
| ode45(ode,tspan,y0)   | Solve system of nonstiff ODE
| ode15s(ode,tspan,y0)  | Solve system of stiff ODE
| pdepe(m,pde,ic,bc,xm,ts)  | Solve 1D PDEs
| pdeval(m,xmesh,usol,xq)   | Interpolate num. PDE solution

### Optimization
| command           | description       |
| :---------------- | :---------------- |
| fminbnd(fun,x1,x2)    | Find minimum of fun(x) in [x1, x2]
| fminsearch(fun,x0)    | Find minimum of function
| lsqnonneg(C,d)        | Solve non-neg. lin. least-squares prob.
| fzero(fun,x0)         | Root of nonlinear function
| optimget(opt,’par’)   | Optimization options values
| optimset(’opt’,val)   | Define optimization options

### Descriptive Statistics
| command           | description       |
| :---------------- | :---------------- |
| bounds(A)         | Smallest and largest elements
| max(A)            | Maximum elements of an array
| min(A)            | Minimum elements of an array
| mode(A)           | Most frequent values in array
| mean(A)           | Average or mean value of array
| median(A)         | Median value of array
| std(A)            | Standard deviation
| var(A)            | Variance
| hist(X)           | calculate and plot histogram
| corrcoef(A)       | Correlation coefficients
| cov(A)            | Covariance
| xcorr(x,y)        | Cross-correlation
| xcov(x,y)         | Cross-covariance
| rand              | Uniformly distributed random numbers
| randn             | Normally distributed random numbers
| randi             | Uniformly distributed pseudorandom integers


further functions: movmax, movmin, cummax, cummin, movprod, movsum, cumsum, cumprod, movmean, movmedian, movstd, movvar.

### Discrete Math
| command           | description       |
| :---------------- | :---------------- |
| factor(n)         | Prime factors
| factorial(n)      | Factorial of input
| gcd(n,m)          | Greatest common divisor
| lcm(n,m)          | least common multiple
| mod(a,m)          | Remainder after division (modulo operation)
| ceil(X)           | Round toward positive infinity
| fix(X)            | Round toward zero
| floor(X)          | Round toward negative infinity
| round(X)          | Round to nearest decimal or integer
