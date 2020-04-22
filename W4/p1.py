"""
Problem 1.  2020 Is a Leap Year, Is It?
"""

year = int( input( "Year: " ) )

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print( "Leap year" )
		else:
			print( "Common year" )
	else:
		print( "Leap year" )
else:
	print( "Common year" )