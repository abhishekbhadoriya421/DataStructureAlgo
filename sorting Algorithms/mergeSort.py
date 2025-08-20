def mergeTwoSortedArray(array,start,mid,end):
    n1 = mid - start +1
    n2 = end - mid
    
    helperArray1 = [0]*n1
    helperArray2 = [0]*n2
    
    # Store Array 
    index1 = 0
    index2 = 0

    for item in range(start,n1+start):
        helperArray1[index1] = array[item]
        index1+=1
    for item in range(mid+1,end+1):
        helperArray2[index2] = array[item]
        index2+=1
        
    start1 = 0
    start2 = 0
    index = start
    while(start1 < n1 and start2 < n2):
        if(helperArray1[start1] < helperArray2[start2]):
            array[index] = helperArray1[start1]
            index+=1
            start1+=1
        else:
            array[index] = helperArray2[start2]
            index+=1
            start2+=1
    
    while(start1 < n1):
        array[index] = helperArray1[start1]
        index+=1
        start1+=1
    
    while(start2 < n2):
        array[index] = helperArray2[start2]
        index+=1
        start2+=1 
    
    
    
    
def mergeSort(array,s,e):
    if(s<e):
        mid = s + (e - s)//2
        mergeSort(array,s,mid)
        mergeSort(array,mid+1,e)
        mergeTwoSortedArray(array,s,mid,e)



array = [5,3,4,2,1,9,7]

mergeSort(array,0,len(array)-1)
print(array)

     
    
    