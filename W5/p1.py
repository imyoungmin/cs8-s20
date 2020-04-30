"""
Problem 1: Squares.
"""

# Reading in a number and making sure it is at least 1.
n = max( 1, int( input( "Provide square length: " ) ) )

# Printing the hollow square.
for i in range( n ):
	for j in range( n ):
		if j == 0 or j == n - 1:		# First and last columns are always printed.
			print( "*", end="" )
		elif i == 0 or i == n - 1:		# First and last rows are full of *'s.
			print( "*", end="" )
		else:
			print( " ", end="" )		# Hollow part.
	print()