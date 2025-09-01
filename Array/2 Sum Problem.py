def bruteForceFindTwoSum(array,target):
    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]+array[j] == target:
                return [i,j]
    return [-1,-1]


def betterAproach(array,target):
    array.sort()
    s = 0
    e = len(array) -1
    while(s < e):
        sum = array[s] + array[e]
        if(sum == target):
            return True
        elif(sum > target):
            e=-1
        else:
            s+=1
    return False

nums = [3,2,4]
target = 6

print(betterAproach(nums,target))