def printN(num):
	if(num ==0):
		return
	print(num)
	printN(num-1)
	

printN(5)