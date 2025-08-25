
# Brute Force Approach
def rotateArrayByDPlace(nums,k):
        while(k>0):
            i = 0
            j = i+1
            first = nums[0]
            while(j<len(nums)):
                nums[i] = nums[j]
                i+=1
                j+=1
            nums[i] = first
            k-=1
        

# Better Approach

def rotateArrayByDPlaceBetter(array, k):
        if len(array)<k:
            k = k % len(array)
        temp = [0]* k
        i = 0
        while(i<k):
            temp[i] = array[i]
            i+=1
            
        i = 0
        j =  k
        while(j<len(array)):
            array[i] = array[j]
            i+=1
            j+=1
        j=0
        while(i<len(array)):
            array[i] = temp[j]
            i+=1 
            j+=1
    

array = [1,2,3,4,5]
# array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# array = [7, 3, 9, 1]
k = 2
rotateArrayByDPlaceBetter(array,k)
print(array)