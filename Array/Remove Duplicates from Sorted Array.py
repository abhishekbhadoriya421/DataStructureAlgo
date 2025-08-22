def removeDuplicate(array):
    result = []
    result.append(array[0])
    for i in range(1,len(array)):
        if array[i-1] != array[i]:
            result.append(array[i])
    return result


array = [0,0,1,1,1,2,3,3,4]
print(removeDuplicate(array))