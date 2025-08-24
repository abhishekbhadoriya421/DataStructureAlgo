def removeDuplicate(array):
    i = 0
    sec = 1
    for j in range(1,len(array)):
        if array[i] != array[j]:
            i+=1
            array[i] = array[j]
            sec = 1
        elif(i+1<j and array[i] > array[i+1]):
            i+=1
            array[i] = array[j]
            sec += 1
        elif sec < 2:
            i+=1
            sec+=1
            
    helper = 1
    count =  0
    for i in range(1,len(array)):
        if helper >=2 and  array[i] == array[i-1]:
            return i
        if array[i] == array[i-1]:
            helper+=1
        else:
           helper = 1
        count = i 
    return count


# array  = [0,0,1,1,1,2,2,3,3,4]
# array  = [1,2,3,4,5,6]
# array  = [1,1,1,1,2,3,4,5,6]
# array = [1,1,1,2]
# array = [1,1,1,2,2]
# array = [1,1]
# array = [1,1,1,1,2,3,3,3,3,4,4]
array = [0,1,2,2,2,2,2,3,4,4,4,4]
# print(array)
index = removeDuplicate(array)
print(index)
for i in range(0,index):
    print(array[i],end=" ")
