def findTarget(arr,target):
	if(len(arr) == 0):
		return False

	if(arr[0]==target):
		return True

	newArray = [];
	for i in range(1,len(arr)):
		newArray.append(arr[i])
	return findTarget(newArray,target)


def findTargetOptimize(arr,index,target):
	if(index == len(arr)):
		return -1
	if(arr[index] == target):
		return index

	return findTargetOptimize(arr,index+1,target)

def printNumbers(num):
	if(num==0):
		return num
	printNumbers(num-1)
	print(num)


# https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&difficulty=Basic,Easy&sortBy=submissions


printNumbers(5)
# print(findTargetOptimize([1,2,3,4,5,6,7],0,1))