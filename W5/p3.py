"""
Problem 3: Euler's Number.
"""

# Reading in number of terms and making sure it is at least 0.
n = max( 0, int( input( "Provide number of terms: " ) ) )

e = 1.0							# The Euler's number.
factorial = 1					# Cumulative factorial.
for i in range( 1, n + 1 ):		# From 1 to n.
	factorial *= i
	e += 1 / factorial

print( "e ≈ {}".format( e ) )