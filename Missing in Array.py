
def helper(arr,index):
	if(index == len(arr)-1):
		return arr[index]+1

	if(arr[index+1]-arr[index] >1):
		return arr[index] +1

	return helper(arr,index+1)


# def  findMissingNumber(arr):
# 	arr.sort()
# 	return helper(arr,0)


def findMissingNumber2(arr):
	totalSum = 0
	for item in arr:
		totalSum+=item

	actualNum = 0
	for item in range(1,max(arr)+1):
		actualNum+=item

	print(actualNum," ",totalSum)
	if(actualNum - totalSum ==0):
		return max(arr)+1
	else:
		return actualNum - totalSum



print(findMissingNumber2([1,2,3,4,5]))