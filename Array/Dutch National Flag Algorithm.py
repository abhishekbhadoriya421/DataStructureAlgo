# Sort Colors

#  sort 0,1,and 2

def bruteForce(array):
    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            if(array[i]>array[j]):
                array[i],array[j] = array[j] ,array[i]
    print(array)
    

nums = [2,0,2,1,1,0]
nums = [2,0,1]
bruteForce(nums)