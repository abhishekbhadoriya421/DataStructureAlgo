def bruteForceFindTwoSum(array,target):
    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]+array[j] == target:
                return [i,j]
    return [-1,-1]



nums = [2,7,11,15]
target = 9
print(bruteForceFindTwoSum(nums,target))