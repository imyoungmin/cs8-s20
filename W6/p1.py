"""
Problem 1: Perfect Numbers.
"""

def perfectNumber( number ):
	"""
	Determines whether a number is perfect or not.
	If the number is perfect, the function yields, for example, "6: 1 2 3".
	:param number: Testing number.
	:return: The perfect number and its factors as a string, None otherwise.
	"""
	result = str( number ) + ": "
	total = 0
	for i in range( 1, number ):
		if number % i == 0:		# A factor?
			total += i
			result += str( i ) + " "

	if total != number:			# Perfect number?
		return None
	return result

if __name__ == "__main__":
	for n in range( 1, 1001 ):
		perfect = perfectNumber( n )
		if perfect is not None:
			print( perfect )