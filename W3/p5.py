"""
Problem 5: Complex Numbers.
"""

from collections import namedtuple
import math

# Defining the Complex tuple type.
Complex = namedtuple( "Complex", ["r", "i"] )

c1 = Complex( r = 1, i = 1 )			# Test instances.
c2 = Complex( r = 1, i = -1 )

# Conjugates.
c1Conj = Complex( r = c1.r, i = -c1.i )
c2Conj = Complex( r = c2.r, i = -c2.i )
print( "Conjugates: {} and {}".format( c1Conj, c2Conj ) )

# The norm of c1 - c2
print( "Norm of c1 - c2: {}".format( math.sqrt( ( c1.r - c2.r ) ** 2 + ( c1.i - c2.i ) ** 2 ) ) )

# Rotating c1 by 90 degrees w.r.t. real axis.
theta = math.pi / 2
c1R = Complex( r = c1.r * math.cos( theta ) - c1.i * math.sin( theta ),
			   i = c1.r * math.sin( theta ) + c1.i * math.cos( theta ) )
print( "Rotating c1: {}".format( c1R ) )