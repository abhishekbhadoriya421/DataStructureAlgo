class Array:
    def __init__(self, array1,array2,size):
        self.array1 = array1
        self.array2 = array2
    
    
def UnionOfSortedArray(array,array2):
    result  = []
    i = 0 
    j = 0
    while(i<len(array) and j<len(array2)):
        if(array[i] == array2[j]):
            # print(array,array2,i,j,result)
            result.append(array[i])
            i+=1
            j+=1
        elif(array[i]<array2[j]):
            result.append(array[i])
            i+=1
        else:
            result.append(array2[j])
            j+=1
              
        while(0 != i and i<len(array) and array[i] == array[i-1]):
            i+=1
        while(0 != j and j<len(array2) and array2[j] == array2[j-1]):
            j+=1
    
    while(i < len(array)):
        result.append(array[i])
        i+=1
        while(0 != i and i<len(array) and array[i] == array[i-1]):
            i+=1
    
    while(j < len(array2) ):
        result.append(array2[j])
        j+=1
        while(0 != j and j<len(array2) and array2[j] == array2[j-1]):
            j+=1
            
    return result
    

array = [4, 6, 6, 9, 10, 11, 11, 11]
array2 = [1, 1 ,1 ,3 ,3]

print(UnionOfSortedArray(array,array2))
