#WEEK 3
#The Supermarket

#Sample catalog
catalog = {'milk':3.09, 'bread':4.19, 'eggs':3.99, 'apples':2.79}

#Create a list to store the three items
shopping_list = []

#Add items to the shopping list
item = input("Enter the first item: ")
shopping_list.append(item)

item = input("Enter the second item: ")
shopping_list.append(item)

item = input("Enter the third item: ")
shopping_list.append(item)

#Compute the total cost
total = catalog[shopping_list[0]] + catalog[shopping_list[1]] +  catalog[shopping_list[2]]

#For Bonus #1, include this line:
# total = total + 0.05*total

#Display the output
print('Receipt')
print('{} cost {}'.format(shopping_list[0], catalog[shopping_list[0]]))
print('{} cost {}'.format(shopping_list[1], catalog[shopping_list[1]]))
print('{} cost {}'.format(shopping_list[2], catalog[shopping_list[2]]))
print('Total: ', total)
