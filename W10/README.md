# Exercises for Week 10

## Problem 1. 2D Barcode

Write a function such that when given an input number `n >= 2`, it returns a string that represents a 
two-dimensional bar code with random `*` characters inside.  For example, if `n = 10`, the random
pattern could look like:

```
+----------+
|** ***  * |
|**  * * **|
|*   * *   |
|  ** *  * |
| * ***    |
|*****    *|
|*  * **  *|
|**** ***  |
|**    **  |
| *  ******|
+----------+
``` 

Note that the pattern includes a **frame** built with dashes, `-`, pipes, `|`, and plus signs, `+`.
How can you make your output pattern look like the example above?

*Hint*:  Import the `random` module and use the function `randrange(x)` to generate your *samples*.