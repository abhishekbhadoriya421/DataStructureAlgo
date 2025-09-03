def findMajorityElement(array):
    for i in range(0,len(array)):
        helperCount = 0
        for j in range(0,len(array)):
            if array[i] == array[j]:
                helperCount+=1
        #  check id array[i] occured more than half length
        if((len(array) // 2 ) + 1 ) <= helperCount:
            return array[i]
    return -1


arr = [2,2,1,1,1,2,2]
print(findMajorityElement(arr))