"""
Problem 2: Median and Mode.
"""

def mode( theList ):
	freqs = {}					# A dictionary to hold frequencies.
	for i in theList:
		if i not in freqs:		# Create an entry for current number in frequencies dictionary.
			freqs[i] = 0
		freqs[i] += 1			# Accumulate frequency.

	# Now find the maximum frequency.
	maxFreq = -1
	for i in freqs:
		if freqs[i] > maxFreq:	# Found an element with maximum frequency?
			maxFreq = freqs[i]

	# Since we now know the maximum frequency, now collect those elements with that maximum frequency.
	return [i for i in freqs if freqs[i] == maxFreq]


def median( theList ):
	theList = sorted( theList )		# Sorted copy of original list!
	half = len( theList ) // 2
	if len( theList ) % 2 == 0:		# Two values are used for the median.
		return sum( theList[half - 1 : half + 1] ) / 2
	return theList[half]			# If not, the median is a single element.


def medianAndMode( theList ):		# This function just collects results from two subordinate functions.
	return median( theList ), mode( theList )


if __name__ == "__main__":
	myList = [9, 2, 3, 1, 1, 3]
	print( medianAndMode( myList ) )
	print( myList )					# Verify that we didn't modify the original list.