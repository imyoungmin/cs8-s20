# Exercises for Weeks 3

## Problem 1: Palindromes semordnilaP

Given a string *s* of length 5, write a function to determine if *s* is palindromic. 

## Problem 2: A Vending Machine

Consider a vending machine represented as a dictionary with candy items (represented by their names)
mapped to prices. The names of the candy items are also stored in *names*, a list of strings. 
Write a program which outputs all candy names and their prices in the following form. 

* The price of [*name*] is [*price*]

As the vending machine was not profitable enough, the administrators decided to up the prices
by 150%. Implement these changes to the dictionary mapping *names* to *prices*.

Test your code in both of the above questions by creating your own dictionaries and names.


## Problem 3: It's Your Birthday!

Write a program that prompts the end user to enter their birthday's month and day in numeric format, and outputs
the corresponding string equivalences in a message with the format `"Your birthday is <month_str> <day>!"`.  
Suppose that both month and day are 1-based
numbers.  For example, consider the following execution:

```
>>> Input month: 4
>>> Input day: 31
>>> Your birthday is April 30!
```

There are several requirements for this problem:
1. Use a `list` to store the month names: `["January", "February", ..., "December"]`.  Notice that the list indices
are 0-based (i.e. index 0 maps to `"January"` and index 11 maps to `"December"`).
2. Use a `list` to store the total number of days in each month (assume no leap years).  These are:
    ```
    January: 31     February: 28     March: 31      April: 30     
    May: 31         June: 30         July: 31       August: 31      
    September: 30   October: 31      November: 30   December: 31
    ```
3. Use the `min()` and `max()` functions to clamp the input values to their corresponding ranges for month and day.
For example, if the user inputs `0` or `15` for a month, you should clamp it to `1` and `12`, respectively.
Likewise, clamp the day depending on the selected month.  In the example execution above, when the user inputs `4`
for `April`, the value `31` is clamped to `30` because April has only 30 days.
4. How would you modify your solution to use a **single** `dict` structure instead of two `lists`?

## Problem 4: Your Initials Here, Please...

Write a program that reads the first and (one-word) surname of a person, separated by a blank space, and
outputs the person's initials in capital letters.  For example:

```
>>> Input name: mónica ángeles
>>> Hello MÁ!
``` 

## Problem 5: Complex Numbers

Write a program that defines a **named tuple** `Complex`, which comes with two fields: `r` for the real part, and
`i` for the imaginary part.  Then, given two complex numbers, `c1` and `c2`, compute and print:
1. Their conjugates: if `c = x + yi` is a complex number, its conjugate is `c' = x - yi`.
2. The norm of `c1 - c2`: if `c = x + yi` is a complex number, its norm is the square root of x<sup>2</sup> +
y<sup>2</sup>.
3. The rotated version of `c1` by 90 degrees with respect to the real axis: if `c = x + yi` is a complex number, 
the rotation of `c` by θ *radians* is given by `c' = (x * cosθ - y * sinθ) + (x * sinθ + y * cosθ)i`. 

Test your program with `c1 = 1 + i` and `c2 = 1 - i`.

## Problem 6: Names and lengths

Write a program which takes 5 strings as inputs and appends them to a list `l`. 
Swap each element in *l* with its mirror - that is, for some element at index `i`, swap `l[i]` with `l[4-i]` if i < 3.

For instance, if `l = ['Alex', 'Bob', 'Charlie', 'David', 'Ethan']`, then after swapping, `l` should read
`['Ethan', 'David', 'Charlie', 'Bob', 'Alex']`

Finally, finish the program by creating a dictionary called `d` mapping each name to its length.

## Problem 7: Survivor Currency
In the reality television series, *Survivor*, castaways can exchange their fire tokens for various food and comfort items, as well as various advantages in the game. The exchange rates for these items are listed in a dictionary, tokens, in the file `survivor.py` with the key: value pair being item: cost respectively. 

a) Write a program that takes two inputs from the keyboard, the amount of fire tokens and a luxury item, and output how many of those luxury items a castaway can buy with the given tokens. *YOUR SOLUTION MUST NOT BE WRITTEN IN THE `survivor.py` FILE AND MUST INCLUDE THE `survivor.py` FILE.*

```
#Example 1: 
>>> Enter amount of fire tokens: 10
>>> Enter luxury item: hidden immunity idol(s)
>>> You can buy 3 hidden immunity idol(s) with 10 fire token(s)
```

```
#Example 2: 
>>> Enter amount of fire tokens: 5
>>> Enter luxury item: jar(s) of peanut butter
>>> You can buy 5 jar(s) of peanut butter with 5 fire token(s)
```

b) **BRIEFLY** explain why the strings defined at the top of the `survivor.py` file are not being outputted.

## Problem 8: Cash Register
a) Write a code snippet that takes a numeric input from the keyboard, cents, and outputs the coins in change a cashier would return. The following assumptions can be made:
1. The input will always be an integer between 0 and 99, inclusive.
2. The cashier will always return the least amount of coins possible.
3. The cashier only has quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent).

```
#Example 1: 
>>> Enter amount of change: 99
>>> Your change is equivalent to 3 quarter(s) + 2 dime(s) + 0 nickel(s) + 4 penny(ies)
```

```
#Example 2: 
>>> Enter amount of change: 43
>>> Your change is equivalent 1 quarter(s) + 1 dime(s) + 1 nickel(s) + 3 penny(ies)
```

b) **BRIEFLY** explain a possible error that can occur if we did not assume statement #1. 

## Problem 9: The Supermarket

The supermarket catalog is stored in a dictionary called `catalog` , which maps item names to their prices. Create your own catalog!

Write a program that prompts the user to enter three items that are on their shopping list (store these in a list called `shopping_list`). Compute the total cost of the user's purchases, and display it as shown in the example.

Example:
```
    >>> Enter the first item: milk
    >>> Enter the second item: apples
    >>> Enter the third item: bread
    >>> Receipt
    milk cost 3.09
    apples cost 2.79
    bread cost 4.19
    Total: 10.07
```

**Bonus #1**

When computing the total, also include the tax (5% on each item, which is equivalent to 5% on the total).

**Bonus #2**

Can this program be modified to allow a user to enter the number of units of each item they want?

## Link to a list of about topics covered in week 3
https://docs.google.com/document/d/1uWzUaBq783Dj1OplowvpWa3zMtXeOLtE_VNQYu-cP4k/edit

And its answer key (sorry for posting so late >_<)
https://docs.google.com/document/d/1YRL2mBbSJ-R8_QozU7Jv5ykSgh5XC6xw0FdipCMWCYY/edit?usp=sharing

## Week 3 Key Concepts Summary
https://docs.google.com/document/d/1I0nszlCkRRUNUGE_acpAYBI8I3C6-uL8_LSStaUx31o/edit?usp=sharing
