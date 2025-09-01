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


def optimizedApproach(array,target):
    my_map = {}
    for i in range(0,len(array)):
        requiredElement = target - array[i]
        if requiredElement in my_map:
            return [my_map[requiredElement],i]
        else:
            my_map[array[i]] = i
    return [-1,-1]

nums = [2,7,11,15]
target = 9

print(optimizedApproach(nums,target))