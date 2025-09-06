def bruteForce(array):
    maximumSubArraySum = float("-inf")
    for i in range(0,len(array)):
        continuousSum = 0
        for j in range(i,len(array)):
            continuousSum+=array[j]
            if(continuousSum > maximumSubArraySum):
                maximumSubArraySum = continuousSum
    return maximumSubArraySum
            
    
    
    
array = [2, 3, -8, 7, -1, 2, 3]
print(bruteForce(array))