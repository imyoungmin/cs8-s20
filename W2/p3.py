"""
Problem 3
"""

import math

# Reading in ladder length and angle with respect to ground.
length = float( input( "Length (m): " ) )
length = max( 1.0, length )
angle = float( input( "Angle (degrees): " ) )
angle = max( 0.0, min( angle, 89.0 ) )

# Make angle to radians.
radians = math.pi * angle / 180

# Computing height.
height = math.sin( radians ) * length

print( "The height is {}m".format( height ) )
