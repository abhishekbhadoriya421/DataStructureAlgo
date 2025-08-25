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
        
        

# array = [1,2,3,4,5]
# array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
array = [7, 3, 9, 1]
k = 9
rotateArrayByDPlace(array,k)
print(array)