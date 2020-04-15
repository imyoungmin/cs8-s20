'''
Write a program which takes 5 strings as inputs and appends them to a list l. Swap each element in l with its mirror - that is, for some element at index i, swap l[i] with l[4-i] if i < 3.

For instance, if l = ['Alex', 'Bob', 'Charlie', 'David', 'Ethan'], then after swapping, l should read
['Ethan', 'David', 'Charlie', 'Bob', 'Alex']

Finally, finish the program by creating a dictionary mapping each name to its length.
'''

# Solution here
l = []
while len(l) < 5:
    l.append(input("Enter a name: "))

temp = l[0]
temp1 = l[1]
l[0] = l[4]
l[1] = l[3]
l[3] = temp1
l[4] = temp

print(l)

name_to_length = {}
for name in l:
    name_to_length[name] = len(name)

print(name_to_length)