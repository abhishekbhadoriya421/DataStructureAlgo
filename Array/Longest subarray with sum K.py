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
            length = max([i+1,length])
        else:
            if (sum - k) in preFixSum:
              length = max([i - preFixSum[sum-k],length])
              
        if (sum) not in preFixSum:
            preFixSum[sum] = i
    
    return length


# If non nagative integer dose not exist then this is the optimal solution

def longestSubarrayOptimal(nums,k):
    sum = 0
    ans = 0
    i = j = 0
    while( i < len(nums) and j < len(nums)):
        sum+=nums[j]
        if(sum == k):
            ans = max([ j-i+1,ans])
        elif(sum>k):
            sum-=nums[i]
            i+=1
        j+=1
    return ans 
        

nums = [10, 5, 2, 7, 1, 9]
k=15

# nums = [94, -33, -13, 40, -82, 94, -33, -13, 40, -82]
# k = 52
print(longestSubarrayOptimal(nums,k))