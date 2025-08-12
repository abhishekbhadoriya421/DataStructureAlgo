def printN(num):
	if(num ==0):
		return

	printN(num-1)
	print(num)

printN(5)