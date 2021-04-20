# Create a method take that accepts a list/array and a number n, and returns a list/array array of the first n elements from the list/array.

def take(arr,n):
	print(arr[:n])
	return arr[:n]


take([0, 1, 2, 3, 5, 8, 13], 3)# [0, 1, 2]
take([0, 1, 2, 3, 5, 8, 13], 0)# []
take([], 3)# []