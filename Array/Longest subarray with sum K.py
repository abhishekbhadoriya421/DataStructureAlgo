def longestSubarrayBruteForce(nums, k):
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
            


def longestSubarrayBetter(nums,k):
    preFixSum = {}
    sum = 0
    length = 0
    for i in range(0,len(nums)):
        sum+=nums[i]
        if(sum == k):
            length +=1
        else:
            if (sum - k) in preFixSum:
              length = max([i - preFixSum[sum-k],length])
              
        preFixSum[sum] = i
    return length


# nums = [10, 5, 2, 7, 1, 9]
# k=15

nums = [-1,1,1]
k = 1
print(longestSubarrayBetter(nums,k))