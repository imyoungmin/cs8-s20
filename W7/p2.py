"""
Problem 2: In Place Reversion.
"""

def reverse( theList ):
	"""
	Reverse a list in place.
	:param theList: Input list.
	"""
	L = len( theList )
	for i in range( L // 2 ):
		theList[i], theList[L - i - 1] = theList[L -i - 1], theList[i]		# Note the unfolding in the assignment.

if __name__ ==  "__main__":
	title = "The Importance of Being Earnest"
	myList = title.split()
	reverse( myList )
	print( myList )