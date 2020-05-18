# Exercises for Week 8

## Problem 1: RGB Triplets

Write a function `rgbToDecimal` that transforms a hexadecimal string of RGB color into a tuple of three 
integers in the range of [0,255], indicating the amount of red, green, and blue primaries present in the 
input triplet.  The input hexadecimal string has the following format:

```
"RRGGBB"
```

where `RR` is the amount of red, `GG` is the amount of green, and `BB` is the amount of blue.  Each single
hexadecimal "digit" `R`, `G`, or `B`, takes the value of `0, 1, ..., 9, A, ..., F`.  For example,
`FF0000` is pure red, while `FFFF00` is yellow, and `00FFFF` is cyan.  The corresponding decimal-based
color equivalences are `(255, 0, 0)`, `(255, 255, 0)`, and `(0, 255, 255)`.  Also, `003660` 
![#003660](https://via.placeholder.com/15/003660/000000?text=+) is the navy blue official *UCSB* color 
with decimal triplet `(0, 54, 96)` (https://brand.ucsb.edu/visual-identity/color#digital)!

To modularize your work, write a function `hexToDec` that converts a hexadecimal string into decimal, and
then call this function from your `rgbToDecimal(.)` method.

## Problem 2: Median and Mode

Write a function to compute the median and the mode(s) of an input list of numbers.  By definition, the 
mode is the most frequent value, and the median is the value (or the average of two values) that are
located midway the sorted list.  Your function should return both statistics in a tuple.  For example,
if the input list is the following:

```
[ 9, 2, 3, 1, 1, 3]
```
the median is 2.5 (when sorting the numbers, 2 and 3 are halfway the list), and the modes are [1, 3] 
(frequency 2 each).

To modularize your work, write a function `median` to compute the median of the list, and `mode` to 
extract a list of mode(s).  Then, call these two functions from your main `medianAndMode(.)` function to
return the expected tuple.

**Note**: Your function should not modify the original input list in any way!  Also, the mode can be
multy-valued like in the example above.

## Week 8 Key Concepts Summary
https://docs.google.com/document/d/1wF6IP6yMpWdgWgR270TPntBnFrD6k6jTHsN_IjkApcg/edit?usp=sharing
