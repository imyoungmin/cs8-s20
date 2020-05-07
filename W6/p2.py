"""
Problem 2: Diamonds.
"""

def diamond( n ):
	"""
	Generate a diamond pattern of a given width (and height).
	Note: We can solve this program by leveraging python's string operations, but the solution here is given the long
	way, with nested loops.
	:param n: Diamond width (expected to be odd).
	:return: Diamond pattern.
	"""
	n = max( 1, n )				# Make sure n is at least 1.
	if n % 2 == 0:				# Fix even numbers, make them odd.
		n += 1
	pattern = ""
	for row in range( n ):				# Controlling the rows.
		nSpaces = abs( n // 2 - row )
		for col in range( nSpaces ):	# Filling in spaces.
			pattern += " "
		nStars = n - 2 * nSpaces
		for col in range( nStars ):		# Filling in stars.
			pattern += "*"
		pattern += "\n"

	return pattern

if __name__ == "__main__":
	print( diamond( 4 ) )