def reverseAnArrayBruteForce(arr,index):
	if(index == len(arr)-1):
		return arr

	arr = reverseAnArrayBruteForce(arr,index+1)
	for i in range(index,len(arr)-1):
		temp = arr[i]
		arr[i] = arr[i+1] 
		arr[i+1] = temp
	return arr


def optimizedReverseArray(arr,s,e):
	if(s>=e):
		return arr

	temp = arr[s]
	arr[s] = arr[e]
	arr[e] = temp
	return bestReverseArray (arr,s+1,e-1)

def bestReverseArray(arr,index):
	if(i>=(n/2)):
		return arr

	temp = arr[len()]
	arr[s] = arr[e]
	arr[e] = temp
print(bestReverseArray([1,2,3,4,5,6,7,8,9],0))