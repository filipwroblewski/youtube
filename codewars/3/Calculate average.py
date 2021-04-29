def find_average(numbers):
    if len(numbers) == 0:
    	print(0)
    	return 0
    n_sum = 0
    for num in numbers:
    	n_sum += num

    print(n_sum/len(numbers))
    return n_sum/len(numbers)


find_average([1, 2, 3])#, 2)
find_average([])#, 0)