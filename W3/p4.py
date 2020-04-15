"""
Problem 4: Your Initials Here, Please...
"""

# Reading in first and surename.
name = input( "Input name: " )

# Splitting and retrieving initials.
splitAt = name.find( " " )
print( "Hello {}!".format( name[0].upper() + name[splitAt+1].upper() ) )