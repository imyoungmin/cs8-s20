"""
Problem 1: Linear Search.
"""

def linearSearch( theList, query ):
	"""
	Search for a query number in a list of numbers and returns the indices where it is found.
	:param theList: List of numbers.
	:param query: Number to search.
	:return: List of indices.
	"""
	result = []
	for idx, val in enumerate( theList ):
		if val == query:
			result.append( idx )

	return result

if __name__ == "__main__":
	myList = [1, 2, 3, 4, 2, 3, 1, 0, 1]

	print( linearSearch( myList, 1 ) )