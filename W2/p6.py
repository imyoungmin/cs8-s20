#Problem 6
#Computing savings

#Input all required information
wage = int(input("Enter your hourly wage: "))
hrs = int(input("Enter the no. of hours worked this month: "))
expenses = int(input("Enter your monthly expenses: "))

#Compute the savings
savings = wage*hrs - expenses

#Print out the savings
print(savings)
