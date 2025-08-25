def moveZero(array):
    i = 0
    j = 0
    while(j<len(array) and i < len(array)):
        if(array[j] != 0):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i+=1
            j+=1
        else:
            j+=1
            
    return array

array = [0,1,4,0,5,2]
moveZero(array)
print(array)