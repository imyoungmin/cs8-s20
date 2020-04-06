"""
Problem 4
"""

import math

# Read in 4 inputs - string inside input(...) represents message 
# to prompt user
x1 = int(input("Enter x coordinate for Point P1:"))
y1 = int(input("Enter y coordinate for Point P1:"))
x2 = int(input("Enter x coordinate for Point P2:"))
y2 = int(input("Enter y coordinate for Point P2:"))

# Calculate distance using sqrt and pow functions
dist = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

# Print distance
print(dist)