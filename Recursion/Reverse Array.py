def reverseAnArrayBruteForce(arr,index):
	if(index == len(arr)-1):
		return arr

	arr = reverseAnArrayBruteForce(arr,index+1)
	for i in range(index,len(arr)-1):
		temp = arr[i]
		arr[i] = arr[i+1] 
		arr[i+1] = temp
	return arr

print(reverseAnArrayBruteForce([1],0))