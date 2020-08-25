# exp-solver

This repository contains the source code for `exp-solver`, a simple command-line application for evaluating and numerically solving complex mathematical expressions.

## Examples

Evaluating simple expressions
```
~$ python exp-solver.py eval 5+3
8
```

Evaluating the complex product of two numbers
```
~$ python exp-solver.py eval z*r where z=2+3i r=1+1.2i
-1.6+5.4i
```

Computing the length of a natural number `n`
```
~$ python exp-solver.py eval 'ceil(log(n))' where n=18942
5
```

Using hillclimbing to solve the equation `x^2+2` for the unknown `x`
```
~$ python exp-solver.py hillclimb x^2+2 x
1.414213562i
```

## Features

This application includes methods of evaluating and solving expressions written basic mathematical notation. The currently supported features include
 - methods of evaluating expressions
 - methods of solving expressions using the hillclimbing optimisation algorithm
 - methods of adding additional variable bindings using the `where` clause (`a+b where a=1 b=2`)
 - support for complex numbers and vectors
 - support for first-class and higher-order functions
 - support for basic arithmetic operations
 - support for common mathematical functions
 - support for basic, inverse, secant, and hyperbolic trigonometric functions
 - support for common mathematical constants `i`, `e`, `pi`, `tau`, and `phi`
