def partition(array,s,e): # my s is pivote 
    pivoteValue = array[s]
    
    countOfSmallerThanPivote = 0
    for i in range(s+1,e+1):
        if array[i] < pivoteValue:
            countOfSmallerThanPivote+=1
    
    # place pivote at right position 
    pivotIndex = s + countOfSmallerThanPivote
    array[s], array[pivotIndex] = array[pivotIndex], array[s]
   
    
    # place all smaller value less then pivote value at its left and greater value at its right
    index1 = s
    index2 = e
    while(index1<pivotIndex and index2 > pivotIndex):
        while(array[index1]<pivoteValue):
            index1+=1
        while(array[index2]>pivoteValue):
            index2-=1
        
        if(index1<pivotIndex and index2 > pivotIndex):
            temp2 = array[index1]
            array[index1] = array[index2]
            array[index2] = temp2
            index1+=1 
            index2-=1
            
    return pivotIndex
        

def QuickSort(array,s,e):
    if s >= e:
        return
    pivoteCurrectIndex = partition(array,s,e)
    QuickSort(array,s,pivoteCurrectIndex-1)
    QuickSort(array,pivoteCurrectIndex+1,e)

    
    
array = [2,4,1,5,6,3,8]

QuickSort(array,0,len(array)-1)
print(array)