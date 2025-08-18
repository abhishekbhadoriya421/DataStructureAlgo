
def SelectionSort(array):
    size = len(array)
    for i in range(0,size-1):
        minIndex = i
        for j in range(i+1,size):
            if (array[minIndex]>=array[j]):
                minIndex = j
        item = array[i]
        array[i] = array[minIndex]
        array[minIndex] = item
        
    return array
        




array = [9,6,1,9,4,6,3,2,7,6,4,3,12,5]
print("Array Before Sorting: ")
print(array,end=" ")
array2 = SelectionSort(array)
print("\nArray After Sorting: ")
print(array2,end=" ")
