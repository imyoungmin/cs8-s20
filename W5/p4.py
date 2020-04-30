"""
Problem 4: Monte Carlo Approximation of π
"""

import random

# Read and validate that at least one sample is requested.
n = max( 1, int( input( "Provide number of samples: " ) ) )

nInside = 0			# Number of samples falling on or inside the circle of radius 1/2, centered at the origin.
r2 = 1 / 4			# Radius squared.

for i in range( n ):
	x = random.uniform( -0.5, 0.5 )		# Cartesian coordinates.
	y = random.uniform( -0.5, 0.5 )
	d = x ** 2 + y ** 2					# Left-hand side of circle implicit function x^2 + y^2 = r^2.
	if d <= r2:
		nInside += 1

pi = 4 * nInside / n
print( "Approximated value of π is ", pi )		# We start getting meaningul approximations for n ~ 5,000,000