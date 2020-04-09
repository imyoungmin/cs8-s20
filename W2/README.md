# Exercises for Weeks 1 and 2

## Problem 1

Write a program that reads in the name of two persons and their respective
ages.  In addition, compute their mean age, and then, output a message with
the following format:

```
<person_1> is <age_1> years old and
<person_2> is <age_2> years old.
Their mean age is <mean_age> years.
```

Notice the usage of newlines.

## Problem 2

Write a program that assigns the string `'-'` to `s1`, and `'+'` to `s2`.
Next, write expressions involving `s1` and `s2` and the string operators `+` and `*`
that evaluate to:

1. `'-+'`
2. `'+--'`
3. `'+--+--'`
4. `'+-+++--+-+++--+-+++--'`

## Problem 3

A ladder put up right against a wall will fall over unless put up at a certain 
angle less than 90 degrees.  Given variables `length` and `angle` storing the
length of the ladder and the angle that it forms with the ground as it leans
against the wall, write a Python program that reads `length` and `angle` from
the end user, and computes the height reached by the ladder.

* **Note**: You'll need the fact that `sin(angle) = height / length`, and that
 `radians = pi * degrees / 180`.

* **Think!**  How do you make sure that the input `length` value is at least 1m,
 and the `angle` is between 0˚ and 89˚?

Test your program with the following values when inputting `length` and `angle`:
1. 16m and 75˚
2. 0m and 0˚
3. 24m and 45˚
4. 24m and 120˚.

## Problem 4

Consider the a function named *distance* which takes 4 (int) inputs separately using the following prompts.

Disregard the subscript and just ask for *Point P1* and *Point P2*
1. Enter `x` coordinate for *Point P*<sub>1</sub>:
2. Enter `y` coordinate for *Point P*<sub>1</sub>:
3. Enter `x` coordinate for *Point P*<sub>2</sub>:
4. Enter `y` coordinate for *Point P*<sub>2</sub>:

Given these inputs, write a function that calculates the distance between *P*<sub>1</sub> and *P*<sub>2</sub>
and stores it in a variable named *dist*. Then, print *dist*. 
Recall that the formula to calculate the distance between two points is the square root of 
(x<sub>1</sub> - x<sub>2</sub>)<sup>2</sup> + (y<sub>1</sub> - y<sub>2</sub>)<sup>2</sup>

## Problem 5

Consider a function which takes 3 (int) inputs with the following prompts
and stores them in variables *a*, *b*, and *c*, respectively.

1. Enter first number:
2. Enter second number:
3. Enter third number:

Write a program which calculates the remainder when `a * b` is divided by `c`. You **may not** use the built-in 
modulo function (denoted by `%`).

## Problem 6

Write a program that takes the user's hourly wage, the number of hours they work in a month, and their monthly expenditure as input (stored in `wage`, `hours`, and `expenses` respectively). Compute their savings for the month using the formula 

savings = (wages x hours) - expenses

and print out the savings. 
