def bruteForce(array):
    maximumSubArraySum = float("-inf")
    for i in range(0,len(array)):
        continuousSum = 0
        for j in range(i,len(array)):
            continuousSum+=array[j]
            if(continuousSum > maximumSubArraySum):
                maximumSubArraySum = continuousSum
    return maximumSubArraySum


def optimizedApproach(array):
    maximumSubArraySum = array[0]
    summ = array[0]
    for i in range(1,len(array)):
        curSum = array[i] + summ
        summ = max(curSum, array[i] )
        maximumSubArraySum = max(summ,maximumSubArraySum)
    return maximumSubArraySum
    
    
    
array = [-2,1,-3,4,-1,2,1,-5,4]
print(optimizedApproach(array))