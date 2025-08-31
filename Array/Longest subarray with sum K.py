def longestSubarray(nums, k):
    ans = 0
    for i in range(0,len(nums)-1):
        count = nums[i]
        length = 1
        for j in range(i+1,len(nums)):
            if count == k:
                if(ans < length):
                    ans = length
                break
            else:
               length+=1
               count+=nums[j]
        if count == k:
            if(ans < length):
                ans = length
    return ans
            



nums = [10, 5, 2, 7, 1, 9]
k=15

# nums = [-1,1,1]
# k = 1
print(longestSubarray(nums,k))