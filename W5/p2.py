"""
Problem 2: Binary to Decimal.
"""

# Reading in a number and making sure it is at least 0.
n = max( 0, int( input( "Provide binary number: " ) ) )

# Assuming that the number contains only 0s and 1s, convert it to decimal.
decimal = 0
power = 0
while n > 0:
	decimal += ( n % 10 ) * ( 2 ** power )
	power += 1
	n //= 10

print( "Number in decimal is: {}".format( decimal ) )