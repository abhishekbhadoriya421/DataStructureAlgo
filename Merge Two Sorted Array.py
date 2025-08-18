def mergeTwoSortedArray(array1,array2):
    n = len(array1)
    m = len(array2)
    newSortedArray = []
    i = 0 
    j = 0
    while(i<n and j<m):
        if(array1[i]<array2[j]):
            newSortedArray.append(array1[i])
            i+=1
        else:
            newSortedArray.append(array2[j])
            j+=1
    
    while(i<n):
        newSortedArray.append(array1[i])
        i+=1
        
    while(j<m):
        newSortedArray.append(array2[j])
        j+=1
        
    return newSortedArray


array1 = [1,3,5,7,8]
array2 = [2,4,6,9]
newSortedArray = mergeTwoSortedArray(array1,array2)
print(newSortedArray)
