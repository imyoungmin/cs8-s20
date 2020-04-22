"""
Problem 2: Triangles
"""

import math

# Reading in a, b, and c.
a = float( input( "Side a: " ) )
b = float( input( "Side b: " ) )
c = float( input( "Side c: " ) )

# Validation: We arbitrarily have chosen 1 as the minimum side length.
a = max( 1.0, math.fabs( a ) )
b = max( 1.0, math.fabs( b ) )
c = max( 1.0, math.fabs( c ) )

# Checking conditions.
if a < b + c and b < a + c and c < a + b:
	print( "Valid side lengths of a: {:.2f}, b: {:.2f}, c: {:.2f}".format( a, b, c ) )
else:
	print( "Privided sides of a: {:.2f}, b: {:.2f}, c: {:.2f} cannot make up a triangle".format( a, b, c ) )