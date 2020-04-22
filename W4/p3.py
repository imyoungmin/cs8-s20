"""
Problem 3: Cyphering and Decyphering
"""

# Cyphering.

original = int( input( "Original number: " ) ) % 10000		# Ensuring at most 4 digits.
originalStr = "{:04d}".format( original )					# Leading 0 if original has fewer than 4 digits.

firstDigit = ( int( originalStr[0] ) + 7 ) % 10				# First step: modifying digits.
secondDigit = ( int( originalStr[1] ) + 7 ) % 10
thirdDigit = ( int( originalStr[2] ) + 7 ) % 10
fourthDigit = ( int( originalStr[3] ) + 7 ) % 10

cyphered = thirdDigit * 1000 + fourthDigit * 100 + firstDigit * 10 + secondDigit	# Swapping digits.

print( "Cyphered number: {:04d}".format( cyphered ) )

# Decyphering.

cypheredStr = "{:04d}".format( cyphered )					# We need again the string version with leading zeros.
firstDigit = int( cypheredStr[0] ) - 7						# The long way, yet more explanatory.
if firstDigit < 0:
	firstDigit += 10
firstDigit %= 10
secondDigit = ( int( cypheredStr[1] ) - 7 ) % 10			# Succint way.  Python handles modulo of negative numbers as given in
thirdDigit = ( int( cypheredStr[2] ) - 7 ) % 10				# https://stackoverflow.com/questions/3883004/the-modulo-operation-on-negative-numbers-in-python
fourthDigit = ( int( cypheredStr[3] ) - 7 ) % 10

decyphered = thirdDigit * 1000 + fourthDigit * 100 + firstDigit * 10 + secondDigit	# Swapping digits.

print( "Decyphered number: {:04d}".format( decyphered ) )

if original == decyphered:
	print( "Success!" )

