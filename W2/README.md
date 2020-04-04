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