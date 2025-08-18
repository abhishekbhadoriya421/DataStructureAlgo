def bubbleSort(array):
    size = len(array)
    for i in range(0,size):
        swapped_perform = False
        for j in range(0,size-i-1):
            if array[j]>array[j+1]:
                item = array[j]
                array[j] = array[j+1]
                array[j+1] = item
                swapped_perform = True

        if not swapped_perform:
            break
    return array

array = [9,6,1,9,4,6,3,2,7,6,4,3,12,5]
print("Array Before Bubble Sorting: ")
print(array,end=" ")
array2 = bubbleSort(array)
print("\nArray After Bubble Sorting: ")
print(array2,end=" ")
