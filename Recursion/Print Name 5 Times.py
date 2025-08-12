def printName(name,index):
	if(index==0):
		return
	print(name)
	printName(name,index-1)
	return


printName("Abhishek",5);