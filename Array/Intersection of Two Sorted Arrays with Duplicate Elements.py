def IntersectionOfTwoSortedArraysWithDuplicateElements(array,array2):
    result = []
    i = 0
    j = 0
    while(i<len(array) and j<len(array2)):
        if(len(result)>1):
            lastValue = result[-1]
            while(i<len(array) and array[i]==lastValue):
                i+=1
            while(j<len(array2) and array2[j]==lastValue):
                j+=1
        
        if(array[i]==array2[j]):
            result.append(array[i])
            i+=1
            j+=1
        elif(array[i]<array2[j]):
            i+=1
        else:
            j+=1
    return result

# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 6, 7]

a = [1, 2, 2, 3, 5]
b = [1, 2, 7]

print(IntersectionOfTwoSortedArraysWithDuplicateElements(a,b))