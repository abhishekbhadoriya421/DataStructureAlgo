
def helper(arr,index):
	if(index == len(arr)-1):
		return arr[index]+1

	if(arr[index+1]-arr[index] >1):
		return arr[index] +1

	return helper(arr,index+1)




def  findMissingNumber(arr):
	arr.sort()
	return helper(arr,0)


print(findMissingNumber([8, 2, 4, 5, 3, 7, 1,6]))