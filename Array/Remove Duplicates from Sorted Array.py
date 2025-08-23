def removeDuplicate(array):
    result = []
    result.append(array[0])
    for i in range(1,len(array)):
        if array[i-1] != array[i]:
            result.append(array[i])
    return result

def removeDup(array):
    i = 1 # replace value
    j = i +1
    while(i<len(array)-1 and j <len(array)-1 ):
        while( j < len(array)-1  and array[j] == array[j+1]):
            j+=1
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        i+=1
        j+=1
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return array
    

def bestApproach(array):
    i = 1
    j = i+1
    maxi = array[0]
    while(j<len(array)):
        if(array[i-1]<array[i]):
            i+=1
            j+=1
        elif(array[i]<array[j] and maxi < array[j]):
            maxi = array[j]
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i+=1
            j+=1
        else:
            j+=1
    return array


# array = [0,0,1,1,1,2,3,3,4,4,5]
# array = [0,1,2,3,3,4,5]
array= [1,2,2,3]
print(array)
print(bestApproach(array))
