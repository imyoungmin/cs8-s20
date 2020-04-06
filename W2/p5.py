import math

# Take inputs
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter thirde number:"))

# Calculate remainder
r = (a*b - c * (a*b//c))

print(r)