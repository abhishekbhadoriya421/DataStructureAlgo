def lowestAndHighestFreqNum(arr,size):
	unordered_map = {} 
	for i in range(0,size):
		if arr[i] in unordered_map:
			unordered_map[arr[i]]= unordered_map[arr[i]] + 1
		else:
			unordered_map[arr[i]]= 1
	
	maxFreq = 0
	minFreq = 123456789
	maxAns = 0
	minAns = 0
	for key in unordered_map:
		if(unordered_map[key]>maxFreq):
			maxFreq = unordered_map[key]
			maxAns = key
		if(unordered_map[key]<minFreq):
			minFreq = unordered_map[key]
			minAns = key

	return [maxAns,minAns]




arr = [1,2,3,3,4,1,1,3,5,6,7,3,1,2,19,1]
print(lowestAndHighestFreqNum(arr,len(arr)))