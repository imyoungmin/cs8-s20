"""
Problem 1
"""

person1 = input( "First name: " )       # Reading first person's data.
age1 = int( input( "First age: " ) )

person2 = input( "Second name: " )      # Reading second person's data.
age2 = int( input( "Second age: " ) )

meanAge = ( age1 + age2 ) / 2

# Outputting information.
print( "{} is {} years old and".format( person1, age1 ) )
print( "{} is {} years old.".format( person2, age2 ) )
print( "Their mean age is {} years.".format( meanAge ) )
