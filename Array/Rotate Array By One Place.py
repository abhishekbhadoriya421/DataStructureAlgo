def rotateArrayByOne (nums):
        first = nums[0]
        i = 0
        j = i+1
        while(j<len(nums)):
            nums[i] = nums[j]
            i+=1
            j+=1
        
        nums[i] = first
        

array = [1,2,3,4,5]
rotateArrayByOne(array)
print(array)