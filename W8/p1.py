"""
Problem 1: RGB Triplets.
"""

def hexToDec( hexStr ):
	decimal = 0
	power = 0
	hexStr = hexStr[::-1].upper()		# Reverse string so that least significant digit is the leftmost.
	for digit in hexStr:
		if "0" <= digit <= "9":			# Digit from 0 to 9?
			decDigit = int( digit )
		else:							# Digit from A to F?
			decDigit = 10 + ord( digit ) - ord( "A" )
		decimal += decDigit * 16 ** power
		power += 1

	return decimal


def rgbToDecimal( rgb ):
	decimalTriplet = []
	for i in range( 3 ):
		color = rgb[i * 2 : i * 2 + 2]				# Extract color channel.
		decimalTriplet.append( hexToDec( color ) )	# Convert hex to decimal.

	return tuple( decimalTriplet )


if __name__ == "__main__":
	print( rgbToDecimal( "003660" ) )