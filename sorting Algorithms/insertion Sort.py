def insertionSort(array):
    size = len(array)
    for i in range(0,size):
        j = i
        while(j>0 and array[j]<array[j-1]):
            temp = array[j]
            array[j] = array[j-1]
            array[j-1] = temp
            j-=1
    return array


array = [9,6,1,9,4,6,3,2,7,6,4,3,12,5]
print("Array Before Insertion Sorting: ")
print(array,end=" ")
array2 = insertionSort(array)
print("\nArray After Insertion Sorting: ")
print(array2,end=" ")

        