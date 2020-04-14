#WEEK 3
#The Supermarket

#Sample catalog
catalog = {'milk':3.09, 'bread':4.19, 'eggs':3.99, 'apples':2.79}

#Create a list to store the three items
shopping_list = []

#Create another list, to store the number of units of each item
units_list = []

#Add items to the shopping list, and units to the units list
item = input("Enter the first item: ")
shopping_list.append(item)	
unit = int(input("Enter the number of units of this item: "))
units_list.append(unit)

item = input("Enter the second item: ")
shopping_list.append(item)
unit = int(input("Enter the number of units of this item: "))
units_list.append(unit)

item = input("Enter the third item: ")
shopping_list.append(item)
unit = int(input("Enter the number of units of this item: "))
units_list.append(unit)

#Compute the total cost
total = catalog[shopping_list[0]]*units_list[0] + catalog[shopping_list[1]]*units_list[1] +  catalog[shopping_list[2]]*units_list[2]

#For Bonus #1, include this line:
# total = total + 0.05*total

#Display the output
print('Receipt')
print('{} cost {}'.format(shopping_list[0], catalog[shopping_list[0]]*units_list[0]))
print('{} cost {}'.format(shopping_list[1], catalog[shopping_list[1]]*units_list[1]))
print('{} cost {}'.format(shopping_list[2], catalog[shopping_list[2]]*units_list[2]))
print('Total: {:.2f}'.format(total))

