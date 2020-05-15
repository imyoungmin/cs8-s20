"""
Problem 3: Text Analysis.
"""

def histogram( text ):
	"""
	Print a histogram of alphanumeric characters in a (possibly multiline) input text.
	:param text: The string to analyze.
	"""
	myMap = {}
	for c in text:
		c = c.lower()				# Normalizing chars to lowercase.
		if c.isalnum():				# Only letters and numbers.  Ignore anything else.
			if c in myMap:
				myMap[c] += 1
			else:
				myMap[c] = 1		# First entry in map.

	# Find the maximum frequency
	myMax = 0
	for key in myMap:
		if myMap[key] > myMax:
			myMax = myMap[key]

	# Printing the histogram.
	for key in myMap:
		val = myMap[key]
		print( ( "{} |{:.<" + str( myMax ) + "}" ).format( key, "*" * val ) )	# If myMax is 7, formatter is "{} |{:.<7}"

if __name__ == "__main__":
	myText = """To be, or not to be: 
				that is the question...
				Still in 2020"""
	histogram( myText )