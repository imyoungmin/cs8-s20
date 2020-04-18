# Exercises for Week 4

## Problem 1: 2020 Is a Leap Year, Isn't It?

A **leap year** is a calendar year that contains an additional day added to keep the calendar year synchronized with 
the astronomical year.  Given an integer year, it is said to be a leap year if its multiple of 4, but if it is 
divisible by 100, it is also evenly divisible by 400.  For example, 2008 was a leap year, as well as 2000; 
nevertheless, 1900 was not a leap year because despite being a multiple of 4 and of 100, it is not a multiple of 400.

Write a program that reads in an integer year and ouputs whether it is a leap or common year. 

## Problem 2: Triangles

Write a program that reads in three numbers and determines and prints if these can be used to build a *non-
degenerate* triangle (i.e. non flat).  Make sure that your program works only with positive values.

**Note**: If the lengths of a triangle are `a`, `b`, and `c`, then each of them must be smaller than the *sum*
of the other two sides.  This is known as the *triangle inequality* for non-degenerate cases.