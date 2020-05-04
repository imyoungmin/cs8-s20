# Exercises for Week 6

## Problem 1: Perfect Numbers

A positive integer is said to be a **perfect number** if its factors, including 1 but excluding the number
itself, add up to the same number.  For instance, 6 is a perfect number because 6 = 1 + 2 + 3.  Write a 
function `perfect( number )` that determines if its parameter `number` is a perfect number.  Use this
function in a program that determines and prints all perfect numbers between 1 and 1000.  Print also all of
the factors of each perfect number you find to confirm that they are truly perfect.

For example, for the case of 6, your program should output:
```
6: 1 2 3
``` 

## Problem 2: Diamonds

Write a function that receives `n`,  a positive odd number, and returns a string that reproduces a diamond 
with the given width ( and height).  For example, the following program:

```python
def diamond( n ):
    return "Your string using " + n + " as parameter."

print( diamond( 9 ) )
```

should produce:
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

## Problem 3: Inverting Numbers

Write a function that takes in an integer value and returns the number with its digits in reversed order.
For example, given the number -7630, the function should return -367.  Notice that negative numbers are
valid, and the sign should be preserved in the final result.

## Problem 4: Min4

Write a function min4() that takes in 4 numbers as parameters and returns the smallest of those 4 numbers. Do not use the min function.

## Problem 5: Transpose

Transpose is a matrix operation which swaps the rows and columns of an element. Write a function, transpose(), which takes a two-dimensional list (which represents a matrix), and returns the transpose of that two-dimensional list.

```
Example:
matrix = [[1, 2, 3], 
          [4, 5, 6]]
transposedMatrix = [[1, 4],
                    [2, 5],
                    [3, 6]]
```

**Challenge: Rewrite the transpose() function without making a new 2D list.**
                
## Additional Practice Problems

https://docs.google.com/document/d/1YXqsS-N0S1bh6hITCOmLlWvIHjyL-UexYnZ3q6ei0js/edit

## Week 6 Key Concepts Summary
https://docs.google.com/document/d/18r7iHWw8sOXbMdGanUdkdSE88Mo4VCxQl7cwHEUpxy0/edit?usp=sharing

