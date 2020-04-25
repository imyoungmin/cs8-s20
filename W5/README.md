# Exercises for Week 5

## Problem 1: Squares

Write a program that reads in the length of a hollow square and prints it using the character `*`.  For example,
suppose that the user inputs a length of `4`, then your program should print:

```
****
*  *
*  *
****
```

## Problem 2: Binary to Decimal

Write a program that reads in a non-negative integer containing only `0`s and `1`s (i.e. a binary number) and 
prints its decimal equivalence.

## Problem 3: Euler's Number

Write a program that reads in a non-negative integer `n` and prints the approximation of the Euler's number *e*
using `n + 1` terms from the formula:

```
         1     1     1           1
e = 1 + --- + --- + --- + ... + ---
         1!    2!    3!          n!
```

*Hint*: 0! = 1

## Problem 4: Monte Carlo Approximation of π

Suppose that we place a *unit square* (i.e. 1x1) centered at the origin of the 2D Cartesian plane.  Further, 
suppose that we inscribe a circle of radius 0.5, also centered at the origin of the system.  Then, the area 
of the circle is exactly π/4, while the square area is 1.  This allows us to establish that the *ratio* of the
circle's area to the square area is (π/4)/1 = π/4.  We can use this fact to approximate the value of π by 
sampling (random) points within the unit square and counting how many of these fall inside the circle as
follows:

- Let *N<sub>total</sub>* be the total number of random samples within the unit square centered at the origin.
- Let *N<sub>inner</sub>* be the number of random samples that lie *on* or *inside* the circle of radius 1/2
  centered at the origin.
  
Then
```
        π   N_inner                          N_inner
        - ≈ -------,        ∴        π ≈ 4 · -------
        4   N_total                          N_total
```

Write a program that estimates the value of π using the above formula with `N_total`, which must be read in
from the user.  Use the following information to build your solution:
- You can generate random samples in a given range with `random.uniform( lowerBound, upperBound )` from the
  `random` module.  For example, `random.uniform( -1, 1 )` yields a number in the range `[-1, 1)`.
- Generate a random *coordinate* for each of the `N_total` sample points.  That is, one random number for `xi`,
  and another random number for `yi` will make up the sample point located at `(xi, yi)` in the 2D plane.
- You can test whether a point falls within a circle centered at `(x0, y0)` of radius `r` by checking the value 
  of `d = (xi - x0)^2 + (yi - y0)^2`.  If `d <= r^2`, then the point is on or inside the circle; if 
  `d > r^2`, th epoint is outside the circle.
  
How many samples do you need to start seing a good approximation of π? 