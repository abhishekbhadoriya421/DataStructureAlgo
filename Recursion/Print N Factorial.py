def findFactorial(num):
	if num <= 1:
		return 1

	result = num * findFactorial(num-1)
	print(result)
	return result


findFactorial(5)

