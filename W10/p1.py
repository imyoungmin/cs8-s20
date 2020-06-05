"""
Problem 1. 2D Barcode.
"""

import random

def twoDBarCode( n ):
	"""
	Create a 2D bar code.
	:param n: Side length.
	:return: A two dimensional random 2D code with * and spaces.
	"""
	code = ""
	code += "+" + "-" * n + "+\n"			# Header.
	for _ in range( n ):
		code += "|"
		for _ in range( n ):
			r = random.randrange( 2 )		# Generate a random number between 0 and 1.
			if r == 0:
				code += "*"
			else:
				code += " "
		code += "|\n"
	code += "+" + "-" * n + "+"				# Footer.
	return code

if __name__ == "__main__":
	n = int( input( "Side length: " ) )
	n = max( 2, n )							# Make sure the side length is at least 2.
	print()
	print( twoDBarCode( n ) )