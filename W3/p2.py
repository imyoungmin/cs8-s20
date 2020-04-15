'''
Consider a vending machine represented as a dictionary with candy items (represented by their names)
mapped to prices. The names of the candy items are also stored in *names*, a list of strings. 
Write a program which outputs all candy names and their prices in the following form. 

* The price of [*name*] is [*price*]

As the vending machine was not profitable enough, the administrators decided to up the prices
by 150%. Implement these changes to the dictionary mapping *names* to *prices*.

Test your code in both of the above questions by creating your own dictionaries and names.

'''

vending_machine = {'kit-kat':1.99, 'twix':0.99}
names = ['kit-kat', 'twix']
for name in names:
    print("The price of " + name + ' is $' + str(vending_machine[name]))
#Alternatively, print(vending_machine) works too

for name in names:
    vending_machine[name] *= 1.5