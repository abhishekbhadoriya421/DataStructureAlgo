# Sort Colors

#  sort 0,1,and 2

def bruteForce(array):
    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            if(array[i]>array[j]):
                array[i],array[j] = array[j] ,array[i]
    print(array)
    

def better(array):
    zero = 0
    one = 0
    two = 0
    for i in array:
        if i == 0:
            zero+=1
        elif i == 1:
            one+=1
        else:
            two+=1
    
    i = 0
    index = 0
    while(i<zero):
        array[index] = 0
        index+=1
        i+=1
    i = 0
    while(i<one):
        array[index] = 1
        index+=1
        i+=1
    
    i = 0   
    while(i<two):
        array[index] = 2
        index+=1
        i+=1
    print(array)
    

def optimize(array):
    low = 0
    mid = 0
    high = len(array)-1
    while(low<=high and mid<=high):
        if(array[mid]==0):
            array[low],array[mid] = array[mid],array[low]
            low+=1
            mid+=1
        elif(array[mid]==1):
            mid+=1
        else:
            array[high],array[mid] = array[mid],array[high]
            high-=1
    print(array)
    
# nums = [2,0,2,1,1,0]
nums = [2,0,1]
optimize(nums)