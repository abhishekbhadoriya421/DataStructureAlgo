def findMaxCongOnesBruteForce(array):

    maxConsicutive = 0
    for i in range(0,len(array)):
        count = 0
        for j in range(i,len(array)):
            if(array[j]==1):
                count +=1
            else:
                break
        if maxConsicutive < count:
            maxConsicutive = count
            
    return maxConsicutive
        
def findMaxCongOneBest(array):
    maxConsicutive = 0
    count = 0
    for i in range(0,len(array)):
        if(array[i] == 1):
            count += 1
        else:
            count = 0
        if ( maxConsicutive < count ):
            maxConsicutive = count
    return maxConsicutive
    
    
    

array = [0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,1,1,1]
print(findMaxCongOneBest(array))