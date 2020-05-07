"""
Problem 3: Inverting Numbers
"""
import math

def invertNumber( n ):
	"""
	Invert the digits of an integer value.
	:param n: The number to revert.
	:return: The number with sign preserved but in reversed order.
	"""
	sign = +1								# We need to preserve the sign.
	if n < 0:
		sign = -1
	n = abs( n )
	power = int( math.log10( n ) )			# We need no know the positional value of the left-most digit.
	result = 0
	while n > 0:
		digit = n % 10
		result += digit * ( 10 ** power )	# The right-most digit is multiplied by the highest positional value of the
		n //= 10							# original number.  Then, we move to the next digit (to the left), and reduce the
		power -= 1							# power of 10 we have to use with it.  We proceed iteratively until n is depleted.

	return sign * result

if __name__ == "__main__":
	print( invertNumber( -7630 ) )