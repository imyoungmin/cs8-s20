"""
Problem 3: It's Your Birthday!
"""

# Creating the lists for months and days.
monthsStr = ["January", "February", "March", "April", "May", "June",
			 "July", "August", "September", "October", "November", "December"]
daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Reading end user input.
month = int( input( "Input month: " ) )
day = int( input( "Input day: " ) )

# Clampling values.
month = max( 1, min( month, 12 ) ) - 1
day = max( 1, min( day, daysPerMonth[month] ) )

# Output message.
print( "Your birthday is {} {}!".format( monthsStr[month], day ) )