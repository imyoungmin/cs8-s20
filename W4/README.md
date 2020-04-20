# Exercises for Week 4

## Problem 1: 2020 Is a Leap Year, Isn't It?

A **leap year** is a calendar year that contains an additional day added to keep the calendar year synchronized with 
the astronomical year.  Given an integer year, it is said to be a leap year if its multiple of 4, but if it is 
divisible by 100, it is also evenly divisible by 400.  For example, 2008 was a leap year, as well as 2000; 
nevertheless, 1900 was not a leap year because despite being a multiple of 4 and of 100, it is not a multiple of 400.

Write a program that reads in an integer year and ouputs whether it is a leap or common year. 

## Problem 2: Triangles

Write a program that reads in three numbers and determines and prints if these can be used to build a 
*non-degenerate* triangle (i.e. non flat).  Make sure that your program works only with positive values.

**Note**: If the lengths of a triangle are `a`, `b`, and `c`, then each of them must be smaller than the *sum*
of the other two sides.  This is known as the *triangle inequality* for non-degenerate cases.

## Problem 3: Cyphering and Decyphering

A company wishes to transfer data though the phone, but they are worried that phone lines can be intercepted.
All of their data are transmitted as 4-digit integers.  They are asking you to write a program to cypher their
data in such a way that information can be sent more safely.  Your program must read in a 4-digit integer and
cypher it as follows:
1. Replace each digit by the *(the sum of the digit plus 7) modulo 10*.
2. Next, interchange the first digit with the third digit, and the second digit with the fourth digit.

Finally, print the cyphered number.

**Challenge!**  Write a second section in your program that takes the cyphered number and produces the 
original (decyphered) number.  Verify whether these values coincide by comparing them.  

## Problem 4: Travel Quiz

Write a program that accepts a number between 1 & 10 (inclusive), and returns a travel destination based on the following criteria.

| Number   | Destination  |
|----------|--------------|
| 1-3      |  Greece      |
| 4-6      |  Thailand    |
| 7-9      |  Switzerland |
| 10       |  France      |
    

If the number is less than zero or greater than 10, print `Your choice is invalid.`

For example
```
    >>> Enter a number between 1 & 10 (inclusive): 6
    >>> You will travel to Thailand next!
```

## Problem 5: Attendance Credit

A student receives credit for attending a lab section only if they are enrolled in that section. Create a list of students enrolled in the section you attend. Allow the user to enter the name of a student, and determine whether the student receives credit for attending your section or not.

*Hint: The membership operators can help you decide this.*

## Problem 6: Roshambo

Write a python script, `roshambo.py`, that takes in two inputs from the keyboard, player1_move and player2_move, and outputs which player wins that round of rock-paper-scissors according to the game’s rules.
*Recall that ‘paper’ beats ‘rock’, ‘scissors’ beats ‘paper’, and ‘rock’ beats ‘scissors’*

```
#Example 1:
>>> Player 1, enter your move: rock
>>> Player 2, enter your move: scissors
>>> Player 1’s rock beats player 2’s scissors!

#Example 2:
>>> Player 1, enter your move: paper
>>> Player 2, enter your move: paper
>>> Player 1’s paper ties with player 2’s paper!

#Example 3:
>>> Player 1, enter your move: gordon
>>> Player 2, enter your move: ramsay
>>> ERROR! Please only enter the values ‘rock’, ‘paper’, or ‘scissors’
```

## Problem 7: Rock Paper Scissors Lizard Spock
Continuing from problem 6, edit your ```roshambo.py``` file to implement an extended version of the RPS game: Rock, Paper, Scissors, Lizard, Spock. The rules to the game are explained in the origins of the game from The Big Bang Theory: https://www.youtube.com/watch?v=x5Q6-wMx-K8. The rules are also written in detail here: https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock.

## Additional Practice Problems
https://docs.google.com/document/d/1345d-ENx0PqvTErIYQYBs0G_o4j4NpXBC_WJTbFrhxI/edit

Hopefully this time, the solutions to the additional problems will be posted in a timely manner >_<

## Week 4 Key Concepts Summary
https://docs.google.com/document/d/1ZZ2ACx84pki5-MNascWcrGXNXXwsQj6hZWL1tjz230M/edit?usp=sharing


