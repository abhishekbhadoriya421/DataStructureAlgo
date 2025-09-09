def bruteForce(array):
    positiveArray = []
    nagetiveArray = []
    
    for i in range(0,len(array)):
        if(array[i]<0):
           nagetiveArray.append(array[i])
        else:
           positiveArray.append(array[i])
    i = 0
    j = 0
    k = 0
    while(i<len(array)):
        array[i] = positiveArray[j]
        i+=1
        j+=1
        array[i] = nagetiveArray[k]
        k+=1
        i+=1
    
    
def optimized(array):
    result = [0]*len(array)
    posIndex = 0
    negIndex = 1
    for i in range(0,len(array)):
        if(array[i] < 0):
            result[negIndex] = array[i]
            negIndex+=2
        else:
            result[posIndex] = array[i]
            posIndex+=2
    return result 
            
    
    


nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
result = optimized(nums)
print(result)